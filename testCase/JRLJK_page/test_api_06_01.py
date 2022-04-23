from common.Log import Logger
import unittest
from pathlib import Path
from readconfig import ReadConfig
from common.cofingHttp import  TestRequest
from common.ServiceLayerInterface import Service_Layer

class Test_api_06_01(unittest.TestCase):
    '''
    用例名称：请求使用正确的炉子编号可以正常得到近两个小时的报警数据
    用例描述：请求使用正确的炉子编号可以正常响应且拿到近两小时的报警数据
    用例编号：api_06_01
    '''

    def setUp(self):
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ======== test  start ========"))
        #预置条件
        self.url = Service_Layer().get_url(0,0,6)
        Logger().logger.info(self.url)
        self.pasrms_furnaceNo = ReadConfig().get_pasrms("furnaceNo")[0]
        self.pasrms = {"furnaceNo":self.pasrms_furnaceNo}
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
        if  "errcode" and "data" in  self.data_text[1].keys():
            Logger().logger.info("errcode/data  字段存在")
        else:
            Logger().logger.info("errcode/data 字段不存在")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #错误码
        if self.data_text[1]['errcode'] == 0:
            Logger().logger.info("errcode  == 0")
        else:
            Logger().logger.info("errcode != 0")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #炉、区域编号
        if str(self.data_text[1]['data']['furnaceNo']) == self.pasrms_furnaceNo:
                Logger().logger.info("炉编号验证成功")
        else:
            Logger().logger.info("炉编号验证失败")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #温度效验

        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ========= test  end ========"))
    def tearDown(self):
        pass
if __name__ == '__main__':
        a = unittest.main()