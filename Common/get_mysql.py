import pymysql
from Common.get_config import Get_Config
from Common.get_path import *
from Common.get_data import Get_Data
import re
import unittest
import logging


class Get_mysql(unittest.TestCase):
    def get_mysql(self, sql_name):  # 获取变量读数据库
        cis_8 = eval(Get_Config.get_config(case_config_path, "MYSQL", "cis_8"))
        cnn = pymysql.connect(**cis_8)
        cursor = cnn.cursor(cursor=pymysql.cursors.DictCursor)
        cursor.execute(sql_name)
        res = cursor.fetchone()
        cursor.close()
        cnn.close()
        el = sql_name.lower()
        if el.find('select * from') != -1:
            return res
        else:
            sql_data = re.search("select (.+?) from", el).group(1)
            return res[sql_data]

    def sql_assertion(self, variable_data, case_id):  # 执行SQL获取数据并断言
        sql_Result = {}  # 创建断言是否通过的容量池
        sql_Rrequest = {}  # 创建sql返回结果容量池
        try:
            sql_value = eval(getattr(Get_Data, "sql"))
            i = 0
            j = -1
            sql_data = {}
            for sql_key in sql_value:  # 遍历SQL语句
                i = i + 1
                if type(sql_key) is dict:  # 判断是否为字典类型数据
                    for key in sql_key.keys():  # 遍历SQL语句
                        sql = self.get_mysql(sql_key[key])  # 执行SQL
                        variable_data[key] = str(sql)  # 将SQL语句返回结果存入变量池variable_data
                        sql_data[str(i)] = str(sql)  # 将SQL语句返回结果存入sql_data
                        logging.info("SQL查询结果{}".format(sql))
                        setattr(Get_Data, "variable_data", variable_data)  # 反射变量池
                else:
                    assertion = eval(getattr(Get_Data, "sql_assertion"))  # 获取断言
                    j = j + 1
                    sql = self.get_mysql(sql_key)  # 执行SQL
                    logging.info("SQL查询结果{}".format(sql))
                    if sql != None:  # SQL断言
                        try:
                            self.assertIn(assertion[j], str(sql))
                            setattr(Get_Data, "Result", "pass")
                            logging.info("SQL断言正确")
                        except AssertionError as e:
                            setattr(Get_Data, "Result", "fail")
                            raise e
                        finally:
                            sql_data[str(i)] = str(sql)  # 将SQL语句返回结果存入sql_data
                    else:
                        try:
                            self.assertEqual(assertion[j], 'None')
                            setattr(Get_Data, "Result", "pass")
                            logging.info("SQL断言正确")
                        except AssertionError as e:
                            setattr(Get_Data, "Result", "fail")
                            raise e
                        finally:
                            sql_data[str(i)] = str(sql)  # 将SQL语句返回结果存入sql_data
            return sql_data
        except Exception as e:
            logging.error("SQL执行错误")
            raise e
        finally:
            sql_Result[str(int(case_id) + 2)] = getattr(Get_Data, "Result")  # 将断言结果存入sql_Result
            Get_Data.sql_assertion_Result.append(sql_Result)  # 将断言结果存入sql_assertion_Result
            sql_Rrequest[str(int(case_id) + 2)] = str(sql_data)  # 将SQL语句返回结果存入sql_Rrequest
            Get_Data.sql_assertion_Request.append(sql_Rrequest)  # 将SQL语句返回结果存入sql_assertion_Request


if __name__ == '__main__':
    res = Get_mysql().get_mysql("select * FROM other_cost_type WHERE cost_name = '太谷补卡费'")
    res1 = Get_mysql().get_mysql("select oct_id FROM other_cost_type WHERE cost_name = '太谷补卡费'")
    print(res)
    print(res1)
