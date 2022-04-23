from common.Log import Logger
import unittest
from pathlib import Path
from readconfig import ReadConfig
from common.cofingHttp import  TestRequest
from common.ServiceLayerInterface import Service_Layer

class Test_api_04_19(unittest.TestCase):
    '''
    用例名称：请求使用错误的炉子编号和区域编号不可以正常得到温度数据
    用例描述：使用错误的炉子编号和区域编号进行请求会提示错误信息
    用例编号：api_04_19
    '''

    def setUp(self):
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ======== test  start ========"))
        #预置条件
        self.url = Service_Layer().get_url(0,0,3)
        Logger().logger.info(self.url)
        self.pasrms_furnaceNo = ReadConfig().get_pasrms("furnaceNo")[4]
        self.pasrms_areaNo = ReadConfig().get_pasrms("areaNo")[5]
        self.pasrms = {"furnaceNo": self.pasrms_furnaceNo,
                       "areaNo":int(self.pasrms_areaNo)}
        Logger().logger.info(self.pasrms)
        self.File = "File"
        self.Success = "Success"
    def test_Case(self):
        #发起请求
        self.data_text = TestRequest().get(self.url,params=self.pasrms)
        Logger().logger.info(self.data_text)
        if self.data_text[0] == 200:
            Logger().logger.info("请求码为： "+str(self.data_text[0]))
        else:
            Logger().logger.info("请求码为 != 200 ",str(self.data_text[0]))
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        # #返回值字段
        if  "errcode" and "errmsg" in  self.data_text[1].keys():
            Logger().logger.info("errcode/errmsg  字段存在")
        else:
            Logger().logger.info("errcode/errmsg 字段不存在")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #错误码
        if self.data_text[1]['errcode'] == 101:
            Logger().logger.info("errcode  == 101")
        else:
            Logger().logger.info("errcode != 101")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        if self.data_text[1]['errmsg'] == "不存在的炉子编号aaa!":
            Logger().logger.info("不存在的炉子编号aaa!")
        else:
            Logger().logger.info("存在的炉子编号aaa!")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ========= test  end ========"))
    def tearDown(self):
        pass
if __name__ == '__main__':
        a = unittest.main()