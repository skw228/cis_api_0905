import configparser

class Get_Config():
    @staticmethod
    def get_config(file_path, section, option):
        cf = configparser.ConfigParser()  # 创建配置分析器
        cf.read(file_path)  # 打开配置文件
        return cf[section][option]  # 返回对应的section中的option的值