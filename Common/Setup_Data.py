from Common.Get_Data import get_data


class Setup_Data():  # 请求数据初始化
    def setup_data(self, url=None, data=None, assertion=None, regular=None, sql=None, sql_assertion=None):
        variable_data = getattr(get_data, "variable_data")
        setattr(get_data, "sql", sql)
        setattr(get_data, "sql_assertion", sql_assertion)
        setattr(get_data, "assertion", assertion)
        setattr(get_data, "regular_variable", regular)
        setattr(get_data, "url", url)
        setattr(get_data, "data", data)
        if getattr(get_data, "sql_assertion") != None:  # 替换变量
            if getattr(get_data, "sql_assertion").find("${") != -1:
                for key in variable_data.keys():
                    if getattr(get_data, "sql_assertion").find(key) != -1:
                        regular = getattr(get_data, "sql_assertion").replace(str(key), str(variable_data[key]))
                        setattr(get_data, "sql_assertion", regular)
        if getattr(get_data, "sql") != None:  # 替换变量
            for sql_value in eval(sql):
                if type(sql_value) is dict:
                    for sql_key in sql_value.keys():
                        if sql_value[sql_key].find("${") != -1:
                            for data_key in variable_data.keys():
                                if sql_value[sql_key].find(data_key) != -1:
                                    sql = getattr(get_data, "sql").replace(str(data_key), str(variable_data[data_key]))
                                    setattr(get_data, "sql", sql)
                else:
                    if sql_value.find("${") != -1:
                        for data_key in variable_data.keys():
                            if sql_value.find(data_key) != -1:
                                sql = getattr(get_data, "sql").replace(str(data_key), str(variable_data[data_key]))
                                setattr(get_data, "sql", sql)
        if getattr(get_data, "assertion") != None:  # 替换变量
            if str(assertion).find("${") != -1:
                for key in variable_data.keys():
                    if getattr(get_data, "assertion").find(key) != -1:
                        assertion = str(getattr(get_data, "assertion")).replace(key, str(variable_data[key]))
                        setattr(get_data, "assertion", assertion)
        if getattr(get_data, "regular_variable") != None:  # 替换变量
            for a in eval(regular).keys():
                if eval(getattr(get_data, "regular_variable"))[a].find("${") != -1:
                    for key in variable_data.keys():
                        if eval(regular)[a].find(key) != -1:
                            regular_data = getattr(get_data, "regular_variable").replace(str(key),
                                                                                         str(variable_data[key]))
                            setattr(get_data, "regular_variable", regular_data)
        if getattr(get_data, "url") != None:  # 替换变量
            if url.find("${") != -1:
                i = 0
                for key in variable_data.keys():
                    i = i + 1
                    if getattr(get_data, "url").find(key) != -1:  # 匹配是否有相同变量名
                        url = getattr(get_data, "url").replace(str(key), str(variable_data[key]))  # 替换变量
                        setattr(get_data, "url", url)
                        if key.find("${int") != -1:  # 匹配是否有自增变量
                            variable_data[key] = str(int(variable_data[key]) + 1)
        if getattr(get_data, "data") != None:  # 替换变量
            if str(data).find("${") != -1:
                i = 0
                for key in variable_data.keys():
                    i = i + 1
                    if getattr(get_data, "data").find(key) != -1:
                        data = str(getattr(get_data, "data")).replace(key, str(variable_data[key]))
                        setattr(get_data, "data", data)
                        if key.find("${int") != -1:
                            variable_data[key] = str(int(variable_data[key]) + 1)