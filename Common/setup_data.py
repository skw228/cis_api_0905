from Common.get_data import Get_Data


class Setup_Data():  # 请求数据初始化
    def setup_data(self, url=None, data=None, assertion=None, regular=None, sql=None, sql_assertion=None):
        variable_data = getattr(Get_Data, "variable_data")
        setattr(Get_Data, "sql", sql)
        setattr(Get_Data, "sql_assertion", sql_assertion)
        setattr(Get_Data, "assertion", assertion)
        setattr(Get_Data, "regular_variable", regular)
        setattr(Get_Data, "url", url)
        setattr(Get_Data, "data", data)
        if getattr(Get_Data, "sql_assertion") != None:  # 替换变量
            if getattr(Get_Data, "sql_assertion").find("${") != -1:
                for key in variable_data.keys():
                    if getattr(Get_Data, "sql_assertion").find(key) != -1:
                        regular = getattr(Get_Data, "sql_assertion").replace(str(key), str(variable_data[key]))
                        setattr(Get_Data, "sql_assertion", regular)
        if getattr(Get_Data, "sql") != None:  # 替换变量
            for sql_value in eval(sql):
                if type(sql_value) is dict:
                    for sql_key in sql_value.keys():
                        if sql_value[sql_key].find("${") != -1:
                            for data_key in variable_data.keys():
                                if sql_value[sql_key].find(data_key) != -1:
                                    sql = getattr(Get_Data, "sql").replace(str(data_key), str(variable_data[data_key]))
                                    setattr(Get_Data, "sql", sql)
                else:
                    if sql_value.find("${") != -1:
                        for data_key in variable_data.keys():
                            if sql_value.find(data_key) != -1:
                                sql = getattr(Get_Data, "sql").replace(str(data_key), str(variable_data[data_key]))
                                setattr(Get_Data, "sql", sql)
        if getattr(Get_Data, "assertion") != None:  # 替换变量
            if str(assertion).find("${") != -1:
                for key in variable_data.keys():
                    if getattr(Get_Data, "assertion").find(key) != -1:
                        assertion = str(getattr(Get_Data, "assertion")).replace(key, str(variable_data[key]))
                        setattr(Get_Data, "assertion", assertion)
        if getattr(Get_Data, "regular_variable") != None:  # 替换变量
            for a in eval(regular).keys():
                if eval(getattr(Get_Data, "regular_variable"))[a].find("${") != -1:
                    for key in variable_data.keys():
                        if eval(regular)[a].find(key) != -1:
                            regular_data = getattr(Get_Data, "regular_variable").replace(str(key),
                                                                                         str(variable_data[key]))
                            setattr(Get_Data, "regular_variable", regular_data)
        if getattr(Get_Data, "url") != None:  # 替换变量
            if url.find("${") != -1:
                i = 0
                for key in variable_data.keys():
                    i = i + 1
                    if getattr(Get_Data, "url").find(key) != -1:  # 匹配是否有相同变量名
                        url = getattr(Get_Data, "url").replace(str(key), str(variable_data[key]))  # 替换变量
                        setattr(Get_Data, "url", url)
                        if key.find("${int") != -1:  # 匹配是否有自增变量
                            variable_data[key] = str(int(variable_data[key]) + 1)
        if getattr(Get_Data, "data") != None:  # 替换变量
            if str(data).find("${") != -1:
                i = 0
                for key in variable_data.keys():
                    i = i + 1
                    if getattr(Get_Data, "data").find(key) != -1:
                        data = str(getattr(Get_Data, "data")).replace(key, str(variable_data[key]))
                        setattr(Get_Data, "data", data)
                        if key.find("${int") != -1:
                            variable_data[key] = str(int(variable_data[key]) + 1)
