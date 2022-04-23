import unittest
from common.Log import Logger
from pathlib import Path
from common.ServiceLayerInterface import Service_Layer
from common.cofingHttp import  TestRequest

class Test_api_01_02(unittest.TestCase):
    '''
    用例名称：请求使用超出数据库数据的炉子编号和区域编号不可以正常得到温度数据
    用例描述：使用超出数据库数据的炉子编号和区域编号进行请求会提示错误信息
    用例编号：api_01_02
    '''
    def setUp (self):
        # 预置
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ====== test  start ========"))
        self.url = Service_Layer().get_url(0,0,0)
        self.pasrms = Service_Layer().get_pasrms(1,1)
        self.File = "File"
        self.Success = "Success"
    def test_Case(self):
        #发起请求
        self.data_text = TestRequest().get(self.url,params=self.pasrms)
        Logger().logger.info(self.data_text)

        #请求码判别
        if self.data_text[0] == 200:
            Logger().logger.info("请求码为： "+str(self.data_text[0]))
        else:
            Logger().logger.info("请求码 != 200 ",str(self.data_text[0]))
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #返回值字段效验
        if  "errcode" and "errmsg" in  self.data_text[1].keys():
            Logger().logger.info("errcode errmsg 字段存在")
        else:
            Logger().logger.info(" errcode errmsg 字段不存在")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #返回值内容效验
        if self.data_text[1]['errcode'] == 101 and self.data_text[1]['errmsg'] == "不存在的炉子编号11!":
            Logger().logger.info("errcode = 101, errmsg == 不存在的炉子编号11! ")
        else:
            Logger().logger.info("errcode,errmsg 内容效验失败 ",self.data_text[1]['errcode'],self.data_text[1]['errmsg'])
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ====== test  end ========"))

    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()

