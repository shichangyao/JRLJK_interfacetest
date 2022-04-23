from common.Log import Logger
import unittest,time
from pathlib import Path
from common.cofingHttp import  TestRequest
from common.ServiceLayerInterface import Service_Layer
class Test_api_01_01(unittest.TestCase):
    '''
    用例名称：请求使用正确的炉子编号和区域编号可以正常得到温度数据
    用例描述：使用正确的炉子编号和区域编号进行请求可以得到正确的响应
    用例编号：api_01_01
    '''
    def setUp (self):
        #预置条件
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ====== test  starts ========"))
        self.url = Service_Layer().get_url(0,0,0)
        self.pasrms = Service_Layer().get_pasrms(0,0)
        self.File = "File"
        self.Success = "Success"
    def test_Case(self):
        #发起请求
        self.data_text = TestRequest().get(self.url,params=self.pasrms)
        Logger().logger.info(self.data_text)
        #状态码
        if self.data_text[0] == 200:
            Logger().logger.info("code："+str(self.data_text[0]))
        else:
            Logger().logger.info("code ！= 200 ",str(self.data_text[0]))
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #错误码
        if self.data_text[1]['errcode'] == 0:
            Logger().logger.info("errcode：" + str(self.data_text[1]['errcode']))
        else:
            Logger().logger.info("errcode ! = 0")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #炉名
        if self.data_text[1]['data']['furnaceNo'] == "2":
            Logger().logger.info("furnaceNo：" +self.data_text[1]['data']['furnaceNo'])
        else:
            Logger().logger.info("furnaceNo ! = 2")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #炉区域
        if self.data_text[1]['data']['areaNo'] == "5":
            Logger().logger.info("areaNo：" +self.data_text[1]['data']['areaNo'])
        else:
            Logger().logger.info("areaNo ! = 5")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #温度和时间效验

        if self.data_text[1]['data']['content'] != [ ] :
            Logger().logger.info("温度和时间不为空")
        else:
            Logger().logger.info("content[0] = []")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        for temp_list in self.data_text[1]['data']['content']:
            #content第一个列表长度
            if len(temp_list) == 2:
                Logger().logger.info("len(temp_list) =2")
            else:
                Logger().logger.info("len(temp_list)")
                Logger().logger.info(str(Path(__file__).name + " : " + self.File))
                return False
            #时间戳长度
            if len(str(temp_list[0])) == 13:
                Logger().logger.info("时间戳长度符合期望")
            else:
                Logger().logger.info("len(temp_list[0]) ! = 13")
                Logger().logger.info(str(Path(__file__).name + " : " + self.File))
                return False
        #type
            if type(temp_list[0]) == int and  type(temp_list[1]) == int or float:
                Logger().logger.info("type 符合期望 ")
            else:
                Logger().logger.info("type  " + self.File)
                Logger().logger.info(str(Path(__file__).name + " : " + self.File))
                return False
            #时间戳处理和判断
            oldtime = str(temp_list[0])
            newtime = oldtime[:-3]
            time_local = time.localtime(int(newtime))
            Logger().logger.info(time_local)
            Logger().logger.info(type(time_local))
            if type(time_local) == time.struct_time:
                Logger().logger.info("时间戳符合期望")
            else:
                Logger().logger.info("time_local 类型不是时间戳")
                Logger().logger.info(str(Path(__file__).name + " : " + self.File))
                return False

        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ====== test  end ========"))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
