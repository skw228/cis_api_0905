import os
import datetime

nowTime = datetime.datetime.now().strftime('%Y-%m-%d')  # 获取当前时间戳
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]  # 指定文件顶级目录
GET_PATH = os.path.dirname(os.path.abspath(__file__))
test_case_path = os.path.join(project_path, 'Test_Data', 'Test_Data.xlsx')  # 指定测试用例目录
case_config_path = os.path.join(project_path, "Configure", "Configure.config")  # 指定Config目录

resultPath = os.path.join(project_path, "Result")
if not os.path.exists(resultPath):
    os.mkdir(resultPath)
html_Path = os.path.join(resultPath, "html")
if not os.path.exists(html_Path):
    os.mkdir(html_Path)
result_html_Path = os.path.join(html_Path, str(nowTime))
if not os.path.exists(result_html_Path):
    os.mkdir(result_html_Path)
html = "test_api${var1}.html".replace("${var1}", str(nowTime))
test_report_path = os.path.join(result_html_Path, html)  # 指定html结果写回目录
log_Path = os.path.join(resultPath, "log")
if not os.path.exists(log_Path):
    os.mkdir(log_Path)
result_log_Path = os.path.join(log_Path, str(nowTime))
if not os.path.exists(result_log_Path):
    os.mkdir(result_log_Path)
log = "${var}.txt".replace("${var}", str(nowTime))
test_logging_path = os.path.join(result_log_Path, log)  # 指定html结果写回目录
