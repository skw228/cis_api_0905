import logging
from Common.Project_Path import *


class Log():
    def my_log(self, msg, level):
        my_log = logging.getLogger("case_log")  # 创建日志工作台
        my_log.setLevel("DEBUG")  # 设置日志输出等级
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-log:%(message)s")  # 设置日志输出格式
        cf = logging.FileHandler(test_logging_path, encoding="utf-8")  # 路径、格式
        cf.setLevel('DEBUG')  # 设置日志输出等级
        cf.setFormatter(formatter)
        my_log.addHandler(cf)
        if level == "DEBUG":  # 创建一条严重级别为DEBUG的日志记录
            my_log.debug(msg)
        elif level == "INFO":  # 创建一条严重级别为INFO的日志记录
            my_log.info(msg)
        elif level == "WARNING":  # 创建一条严重级别为WARNING的日志记录
            my_log.warning(msg)
        elif level == "ERROR":  # 创建一条严重级别为ERROR的日志记录
            my_log.error(msg)
        elif level == "CRITICAL":  # 创建一条严重级别为CRITICAL的日志记录
            my_log.critical(msg)
        my_log.removeHandler(cf)

    def debug(self, msg):
        self.my_log(msg, "DEBUG")

    def info(self, msg):
        self.my_log(msg, "INFO")

    def warning(self, msg):
        self.my_log(msg, "WARNING")

    def error(self, msg):
        self.my_log(msg, "ERROR")

    def critical(self, msg):
        self.my_log(msg, "CRITICAL")
