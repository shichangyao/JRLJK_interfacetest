from common.Log import Logger
import unittest,time
from pathlib import Path
from readconfig import ReadConfig
from common.cofingHttp import  TestRequest
from common.ServiceLayerInterface import Service_Layer

class Test_api_06_03(unittest.TestCase):
    '''
    用例名称：请求使用超出错误数据的炉子编号不可以正常得到数据
    用例描述：请求使用超出错误数据的炉子编号不能获得正确的响应
    用例编号：api_06_03
    '''

    def setUp(self):
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ======== test  start ========"))
        #预置条件
        self.url = Service_Layer().get_url(0,0,6)
        Logger().logger.info(self.url)
        self.pasrms_furnaceNo = ReadConfig().get_pasrms("furnaceNo")[5]
        self.pasrms = {"furnaceNo":self.pasrms_furnaceNo}
        Logger().logger.info(self.pasrms)
        self.File = "File"
        self.Success = "Success"
    def test_Case(self):
        #发起请求
        self.data_text = TestRequest().get(self.url,params=self.pasrms)
        Logger().logger.info(self.data_text)
        if self.data_text  == 500:
            Logger().logger.info("请求码为： "+str(self.data_text))
        else:
            Logger().logger.info("请求码为 != 500 ",str(self.data_text))
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False

        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ========= test  end ========"))
    def tearDown(self):
        pass
if __name__ == '__main__':
        a = unittest.main()