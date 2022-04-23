from common.Log import Logger
import unittest
from pathlib import Path
from common.cofingHttp import  TestRequest
from common.ServiceLayerInterface import Service_Layer

class Test_api_01_03(unittest.TestCase):
    '''
    用例名称：使用正确的炉子编号和超出数据库数据的区域编号进行请求会提示错误信息
    用例描述：使用正确的炉子编号和超出数据库数据的区域编号进行请求会提示错误信息
    用例编号：api_01_03
    '''
    def setUp (self):
        #预置条件
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ====== test  start ========"))
        self.url = Service_Layer().get_url(0,0,0)
        self.pasrms = Service_Layer().get_pasrms(2,2)
        self.File = "File"
        self.Success = "Success"
    def testCase(self):
        #发起请求
        self.data_text = TestRequest().get(self.url,params=self.pasrms)
        Logger().logger.info(self.data_text)

        if self.data_text[0] == 200:
            Logger().logger.info("请求码为： "+str(self.data_text[0]))
        else:
            Logger().logger.info("请求码 ！= 200 ",str(self.data_text[0]))
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False

        #返回值字段效验
        if  "errcode" and "errmsg" in  self.data_text[1].keys():
            Logger().logger.info("errcode，errmsg 字段存在")
        else:
            Logger().logger.info("errcode，errmsg字段不存在")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #返回值内容效验
        if self.data_text[1]['errcode'] == 101 and self.data_text[1]['errmsg'] == "区域8在4号炉中不存在!":
            Logger().logger.info("self.data_text[1]['errcode/errmsg'] ,内容效验成功")
        else:
            Logger().logger.info("self.data_text[1]['errcode/errmsg'] ,内容效验失败")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ====== test  end ========"))

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()