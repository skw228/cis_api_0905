import unittest
import logging
from Common.get_data import Get_Data


class Request_Assertion(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.Result = None

    def assertion(self, request_data, case_id):
        assertion_list = []
        assertion_dict = {}
        assertion = getattr(Get_Data, "assertion")
        try:
            self.assertIn(str(assertion), request_data)
            self.Result = "pass"
            logging.info("断言正确")
        except AssertionError as e:
            self.Result = "fail"
            logging.error("断言错误")
            raise e
        finally:
            assertion_list.append(request_data)
            assertion_list.append(self.Result)
            assertion_dict[str(int(case_id) + 2)] = assertion_list
            Get_Data.assertion_data.append(assertion_dict)
