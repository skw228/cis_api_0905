from Common.Http_Request import HttpRequest
from Common.Get_Data import get_data
from Common.Du_Excel_Case import Du_Excel_Case
from Common.Write_Excel_Data import Write_Excel_Data
from Common.Project_Path import *
from Common.Write_Log import Log
from Common.Du_Mysql import Du_Pymasql
from Common.Obtain_Regular import Obtain_Regular
from Common.Setup_Data import Setup_Data
from Common.Request_Assertion import Request_Assertion
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
test_case = Du_Excel_Case().get_case(test_case_path)
cookie = None  # 申明全局变量


class Test_cast():
    def setup_class(cls) -> None:
        setattr(get_data, "variable_data", Du_Excel_Case().get_variable(test_case_path))

    def teardown_class(cls) -> None:
        Write_Excel_Data().set_data(case_config_path, test_case_path)

    @pytest.mark.parametrize("item", test_case)
    def test_api(self, item):
        global cookie, res
        Log().info("执行的用例{}".format(item["case_id"]))
        # 数据初始化
        Setup_Data().setup_data(url=item["url"], data=item["data"], assertion=item["assertion"],
                                regular=item["regular"], sql=item["sql"], sql_assertion=item["sql_assertion"])
        if item["header"] == "form":
            if str(getattr(get_data, "data")).find("{") != -1:
                res = HttpRequest().http_request_data(url=getattr(get_data, "url"), method=item["method"],
                                                      cookie=cookie, data=eval(getattr(get_data, "data")),
                                                      header=Header_form)
            else:
                res = HttpRequest().http_request_data(url=getattr(get_data, "url"), method=item["method"],
                                                      cookie=cookie, data=getattr(get_data, "data"), header=Header_form)
        if item["header"] == "json":
            if str(getattr(get_data, "data")).find("{") != -1:
                res = HttpRequest().http_request_json(url=getattr(get_data, "url"), method=item["method"],
                                                      cookie=cookie, data=eval(getattr(get_data, "data")),
                                                      header=Header_json)
            else:
                res = HttpRequest().http_request_json(url=getattr(get_data, "url"), method=item["method"],
                                                      cookie=cookie, data=getattr(get_data, "data"), header=Header_json)
        if item["header"] == "text":
            res = HttpRequest().http_request_data(url=getattr(get_data, "url"), method=item["method"], cookie=cookie,
                                                  data=getattr(get_data, "data"), header=Header_text)
        if res.cookies:  # 更新cookie
            cookie = res.cookies
        request_data = res.text
        if item["assertion"] != None:  # 断言
            Request_Assertion().assertion(request_data, item["case_id"])
        if item["regular"] != None:  # 正则匹配
            Obtain_Regular().Regular_data(getattr(get_data, "variable_data"), request_data)
        if item["sql"] != None:  # 执行sql
            Du_Pymasql().sql_assertion(getattr(get_data, "variable_data"), item["case_id"])
