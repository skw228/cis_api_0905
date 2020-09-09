# import logging
# from Common.get_path import *
#
#
# class Log():
#     def my_log(self, msg, level):
#         my_log = logging.getLogger()  # 设置日志器
#         my_log.setLevel(logging.DEBUG)  # 设置日志输出等级
#         formatter = logging.Formatter(
#             "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")  # 设置格式化器
#         sh = logging.StreamHandler()  # 设置控制台处理器
#         fh = logging.FileHandler(logging_path, encoding="utf-8")  # 设置文件处理器
#         # 将格式化器添加到文件处理器和控制台处理当中
#         sh.setFormatter(formatter)
#         fh.setFormatter(formatter)
#         # 将文件处理器和控制台处理器添加到日志器当中
#         my_log.addHandler(sh)
#         my_log.addHandler(fh)
#
#         if level == "DEBUG":  # 创建一条严重级别为DEBUG的日志记录
#             my_log.debug(msg)
#         elif level == "INFO":  # 创建一条严重级别为INFO的日志记录
#             my_log.info(msg)
#         elif level == "WARNING":  # 创建一条严重级别为WARNING的日志记录
#             my_log.warning(msg)
#         elif level == "ERROR":  # 创建一条严重级别为ERROR的日志记录
#             my_log.error(msg)
#         elif level == "CRITICAL":  # 创建一条严重级别为CRITICAL的日志记录
#             my_log.critical(msg)
#         my_log.removeHandler(fh)
#
#     def debug(self, msg):
#         self.my_log(msg, "DEBUG")
#
#     def info(self, msg):
#         self.my_log(msg, "INFO")
#
#     def warning(self, msg):
#         self.my_log(msg, "WARNING")
#
#     def error(self, msg):
#         self.my_log(msg, "ERROR")
#
#     def critical(self, msg):
#         self.my_log(msg, "CRITICAL")
