import requests
import logging


class Api_Request():
    def api_request_json(self, url=None, method=None, cookie=None, data=None, header=None, ):  # 封装json请求
        logging.info(
            "请求的入参url:{}...method:{}...cookie:{}...data:{}...header:{}".format(url, method, cookie, data, header))
        if method.upper() == "GET":
            try:
                res = requests.get(url, json=data, cookies=cookie, headers=header)
            except Exception as e:
                logging.error("get请求错误：{}".format(e))
                raise e
            return res
        elif method.upper() == "POST":
            try:
                res = requests.post(url, json=data, cookies=cookie, headers=header)
            except Exception as e:
                logging.error("post请求错误：{}".format(e))
                raise e
            return res
        else:
            logging.error("输入的请求方法不对")


    def api_request_data(self, url=None, method=None, cookie=None, data=None, header=None):  # 封装data请求
        logging.info(
            "请求的入参url:{}...method:{}...cookie:{}...data:{}...header:{}".format(url, method, cookie, data, header))
        if method.upper() == "GET":
            try:
                res = requests.get(url, data=data, cookies=cookie, headers=header)
            except Exception as e:
                raise e
            return res
        elif method.upper() == "POST":
            try:
                res = requests.post(url, data=data, cookies=cookie, headers=header)
            except Exception as e:
                raise e
            return res
        else:
            logging.error("输入的请求方法不对")
