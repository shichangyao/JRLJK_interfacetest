from common.Log import Logger
import unittest
from pathlib import Path
from readconfig import ReadConfig
from common.cofingHttp import  TestRequest
from common.ServiceLayerInterface import Service_Layer

class Test_api_02_01(unittest.TestCase):
    '''
    用例名称：请求使用正确的炉子编号可以正常得到温度数据
    用例描述：使用正确的炉子编号可以得到正确的响应
    用例编号：api_02_01
    '''

    def setUp(self):
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ====== test  start ========"))
        #预置条件
        self.url = Service_Layer().get_url(0,0,1)
        self.pasrms_furnaceNo = ReadConfig().get_pasrms("furnaceNo")[0]
        self.pasrms = {"furnaceNo": self.pasrms_furnaceNo}
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
        # #返回值字段效验
        if  "errcode" and "data" in  self.data_text[1].keys():
            Logger().logger.info("errcode/data  字段存在")
        else:
            Logger().logger.info("errcode/data 字段不存在")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        if "furnaceNo" and "content" and"furnace_count" in self.data_text[1]['data'].keys():
            Logger().logger.info("furnaceNo/content/furnace_count  字段存在")
        else:
            Logger().logger.info("furnaceNo/content/furnace_count 字段不存在")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #查询炉区域数
        self.area_count = Service_Layer().get_area_count(0)
        #判断温度列表长度
        if str(len(self.data_text[1]['data']['content'])) ==  self.area_count:
            Logger().logger.info("显示对应区域数时间温度数据")
        else:
            Logger().logger.info("未显示对应区域数时间温度数据")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #判断温度列表数据类型
        for temperature_list in self.data_text[1]['data']['content']:
            if type(temperature_list) == int or float:
                Logger().logger.info("温度数据类型正确")
            else:
                Logger().logger.info("温度数据类型不正确")
                Logger().logger.info(str(Path(__file__).name + " : " + self.File))
                return False

        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ====== test  end ========"))
    def tearDown(self):
        pass
if __name__ == '__main__':
        a = unittest.main()