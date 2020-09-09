class Get_Data():
    data = None  # 请求入参替换
    url = None  # 请求url替换
    regular = None  # 正则提取出来的变量值
    assertion = None  # 断言数据替换
    variable_data = None  # 变量初始化化数据
    regular_variable = None  # 正则数据替换
    sql = None  # SQL数据替换
    sql_assertion = None  # SQL断言数据替换
    Result = None  # 断言结果
    assertion_data = []  # 请求结果和断言写回
    sql_assertion_Request = []  # sql查询结果写回
    sql_assertion_Result = []  # sql断言结果写回
