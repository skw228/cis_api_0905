import configparser
import os
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]  # 指定文件顶级目录
case_config_path = os.path.join(project_path, "Configure", "Configure.config")  # 指定Config目录
class Readconfig():
    @staticmethod
    def get_config(file_path, section, option):
        cf = configparser.ConfigParser()  # 创建配置分析器
        cf.read(file_path)  # 打开配置文件
        return cf[section][option]  # 返回对应的section中的option的值