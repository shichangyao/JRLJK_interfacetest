from common.Log import Logger
import unittest,time
from pathlib import Path
from readconfig import ReadConfig
from common.cofingHttp import  TestRequest
from common.ServiceLayerInterface import Service_Layer

class Test_api_04_06(unittest.TestCase):
    '''
    用例名称：请求使用正确的炉子编号和区域编号以及sign值和错误的dur_time的值不能得到最近时间段温度数据
    用例描述：使用正确的炉子编号和区域编号以及sign值和错误的dur_time的值进行请求不能得到正确的响应并且得到相应数据
    用例编号：api_04_06
    '''

    def setUp(self):
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ======== test  start ========"))
        #预置条件
        self.url = Service_Layer().get_url(0,0,3)
        Logger().logger.info(self.url)
        self.pasrms_furnaceNo = ReadConfig().get_pasrms("furnaceNo")[11]
        self.pasrms_areaNo = ReadConfig().get_pasrms("areaNo")[5]
        self.dur_time = ReadConfig().get_pasrms("dur_time")[4]
        self.pasrms = {"furnaceNo": int(self.pasrms_furnaceNo),
                       "areaNo":int(self.pasrms_areaNo),
                       "dur_time":self.dur_time}
        Logger().logger.info(self.pasrms)
        self.File = "File"
        self.Success = "Success"
    def test_Case(self):
        #发起请求
        self.data_text = TestRequest().get(self.url,params=self.pasrms)
        Logger().logger.info(str(self.data_text))
        if self.data_text == 500:
            Logger().logger.info(str(self.data_text))
        else:
            Logger().logger.info(str(self.data_text))
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False

        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ========= test  end ========"))
    def tearDown(self):
        pass
if __name__ == '__main__':
        a = unittest.main()