from Common.api_request import Api_Request
from Common.get_data import Get_Data
from Common.get_excel import Get_Excel
from Common.write_excel import Write_Excel
from Common.get_path import *
import logging
from Common.get_mysql import Get_mysql
from Common.get_regular import Get_Regular
from Common.setup_data import Setup_Data
from Common.request_assertion import Request_Assertion
import pytest

Header_form = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}
Header_json = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Content-Type': 'application/json;charset=UTF-8'}
Header_text = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Content-Type': 'text/plain;charset=UTF-8'}
test_case = Get_Excel().get_excel(test_case_path)
cookie = None  # 申明全局变量


class Test_cast():
    def setup_class(cls) -> None:
        setattr(Get_Data, "variable_data", Get_Excel().get_excel_variable(test_case_path))

    def teardown_class(cls) -> None:
        Write_Excel().write_excel(case_config_path, test_case_path)

    @pytest.mark.parametrize("item", test_case)
    def test_api(self, item):
        global cookie, res
        logging.info("执行的用例{}".format(item["case_id"]))
        # 数据初始化
        Setup_Data().setup_data(url=item["url"], data=item["data"], assertion=item["assertion"],
                                regular=item["regular"], sql=item["sql"], sql_assertion=item["sql_assertion"])
        if item["header"] == "form":
            if str(getattr(Get_Data, "data")).find("{") != -1:
                res = Api_Request().api_request_data(url=getattr(Get_Data, "url"), method=item["method"],
                                                     cookie=cookie, data=eval(getattr(Get_Data, "data")),
                                                     header=Header_form)
            else:
                res = Api_Request().api_request_data(url=getattr(Get_Data, "url"), method=item["method"],
                                                     cookie=cookie, data=getattr(Get_Data, "data"), header=Header_form)
        if item["header"] == "json":
            if str(getattr(Get_Data, "data")).find("{") != -1:
                res = Api_Request().api_request_json(url=getattr(Get_Data, "url"), method=item["method"],
                                                     cookie=cookie, data=eval(getattr(Get_Data, "data")),
                                                     header=Header_json)
            else:
                res = Api_Request().api_request_json(url=getattr(Get_Data, "url"), method=item["method"],
                                                     cookie=cookie, data=getattr(Get_Data, "data"), header=Header_json)
        if item["header"] == "text":
            res = Api_Request().api_request_data(url=getattr(Get_Data, "url"), method=item["method"], cookie=cookie,
                                                 data=getattr(Get_Data, "data"), header=Header_text)
        if res.cookies:  # 更新cookie
            cookie = res.cookies
        request_data = res.text
        if item["assertion"] != None:  # 断言
            Request_Assertion().assertion(request_data, item["case_id"])
        if item["regular"] != None:  # 正则匹配
            Get_Regular().get_regular_data(getattr(Get_Data, "variable_data"), request_data)
        if item["sql"] != None:  # 执行sql
            Get_mysql().sql_assertion(getattr(Get_Data, "variable_data"), item["case_id"])
