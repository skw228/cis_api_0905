import logging
from Common.get_path import *
from logging import handlers


# 1 首先定义一个初始化日志的函数
def init_logging():
    # 2 在函数中，设置日志器
    logger = logging.getLogger()
    # 3 设置日志等级
    logger.setLevel(logging.DEBUG)
    # 4 设置控制台处理器
    sh = logging.StreamHandler()
    # 5 设置文件处理器
    fh = logging.handlers.TimedRotatingFileHandler(project_path + "/log/cis.log",
                                                   when='M',  # S秒M分H小时D天W每星期（interval==0时代表星期一）midnight 每天凌晨
                                                   interval=1,  # 间隔
                                                   backupCount=3,  # 保留
                                                   encoding='utf-8')
    # 6 设置格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 7 将格式化器添加到文件处理器和控制台处理当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 8 将文件处理器和控制台处理器添加到日志器当中
    logger.addHandler(sh)
    logger.addHandler(fh)
