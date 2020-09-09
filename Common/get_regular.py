from Common.get_data import Get_Data
import re
import json
import logging

global null
null = None


class Get_Regular():
    def get_regular(self, regular, ddd):
        global null
        null = None
        if type(ddd) is list:
            for a in ddd:
                el = str(a)
                if re.search(regular, el) != None:
                    setattr(Get_Data, "regular", re.search(regular, el).group(1))
                if type(a) is list:
                    for b in a:
                        el = str(b)
                        if re.search(regular, el) != None:
                            setattr(Get_Data, "regular", re.search(regular, el).group(1))
                        if type(b) is list:
                            for c in b:
                                el = str(c)
                                if re.search(regular, el) != None:
                                    setattr(Get_Data, "regular", re.search(regular, el).group(1))
                        if type(b) is dict:
                            for c in b.keys():
                                d = b[c]
                                el = str(d)
                                if re.search(regular, el) != None:
                                    setattr(Get_Data, "regular", re.search(regular, el).group(1))
                if type(a) is dict:
                    for b in a.keys():
                        c = a[b]
                        el = str(c)
                        if re.search(regular, el) != None:
                            setattr(Get_Data, "regular", re.search(regular, el).group(1))
                        if type(c) is list:
                            for d in c:
                                el = str(d)
                                if re.search(regular, el) != None:
                                    setattr(Get_Data, "regular", re.search(regular, el).group(1))
                        if type(c) is dict:
                            for d in c.keys():
                                e = c[d]
                                el = str(e)
                                if re.search(regular, el) != None:
                                    setattr(Get_Data, "regular", re.search(regular, el).group(1))
        if type(ddd) is dict:
            for a in ddd.keys():
                b = ddd[a]
                el = str(b)
                if re.search(regular, el) != None:
                    res = re.search(regular, el).group(1)
                    setattr(Get_Data, "regular", res)
                if type(b) is list:
                    for c in b:
                        el = str(c)
                        print("kaishile3")
                        print(el)
                        if re.search(regular, el) != None:
                            res = re.search(regular, el).group(1)
                            print("kaishile4")
                            setattr(Get_Data, "regular", res)
                        if type(c) is list:
                            for d in c:
                                el = str(d)
                                if re.search(regular, el) != None:
                                    res = re.search(regular, el).group(1)
                                    setattr(Get_Data, "regular", res)
                        if type(c) is dict:
                            for d in c.keys():
                                print("kaishile5")
                                e = c[d]
                                el = str(e)
                                if re.search(regular, el) != None:
                                    res = re.search(regular, el).group(1)
                                    setattr(Get_Data, "regular", res)
                if type(b) is dict:
                    for c in b.keys():
                        d = b[c]
                        el = str(d)
                        if re.search(regular, el) != None:
                            res = re.search(regular, el).group(1)
                            setattr(Get_Data, "regular", res)
                        if type(d) is list:
                            for e in d:
                                el = str(e)
                                if re.search(regular, el) != None:
                                    res = re.search(regular, el).group(1)
                                    setattr(Get_Data, "regular", res)
                        if type(d) is dict:
                            for e in d.keys():
                                f = d[e]
                                el = str(f)
                                if re.search(regular, el) != None:
                                    res = re.search(regular, el).group(1)
                                    setattr(Get_Data, "regular", res)

    def get_regular_data(self, variable_data, res_request):
        try:
            for a in eval(getattr(Get_Data, "regular_variable")).keys():  # 遍历正则匹配数据
                self.get_regular(eval(getattr(Get_Data, "regular_variable"))[a],
                                 json.loads(res_request))  # 调用字典列表拆解获取唯一结果
                variable_data[a] = str(getattr(Get_Data, "regular"))  # 将正则返回结果存入变量中
                logging.info("正则获取到的变量{}".format(getattr(Get_Data, "regular")))
                setattr(Get_Data, "variable_data", variable_data)  # 反射变量
        except Exception as e:
            logging.error("正则执行失败{}".format(e))
            raise e


if __name__ == '__main__':
    ddd = {'recordsFiltered': 2, 'data': [{'addrCodeId': '110101"001', 'codeId': '110101', 'addrCodeLevel': '4',
                                           'addrCodeDes': '\\u4e1c\\u57ce\\u533a"2222', 'nodeName': None,
                                           'pinyinCode': None, 'addrCodeLng': None, 'addrCodeLat': None,
                                           'tenantId': 'ITQ8m46H1FpoaC2brNC52vLr06lv24LA', 'orgId': '075703',
                                           'openCustFeePrice': None, 'remark': None, 'telphone': None},
                                          {'addrCodeId': '110101013', 'codeId': '110101', 'addrCodeLevel': '4',
                                           'addrCodeDes': '\\u4e1c\\u57ce\\u533a"批量开户', 'nodeName': None,
                                           'pinyinCode': None, 'addrCodeLng': 116.39578, 'addrCodeLat': 39.932173,
                                           'tenantId': 'ITQ8m46H1FpoaC2brNC52vLr06lv24LA', 'orgId': '075703',
                                           'openCustFeePrice': None, 'remark': None, 'telphone': None}], 'draw': 0,
           'recordsTotal': 2}
    el111 = "addrCodeId': '(.+?)', 'codeId': '110101', 'addrCodeLevel': '4', 'addrCodeDes"
    Get_Regular().get_regular(el111, ddd)
    print(getattr(Get_Data, "regular"))
