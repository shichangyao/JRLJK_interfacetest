from common.Log import Logger
import unittest,time
from pathlib import Path
from readconfig import ReadConfig
from common.cofingHttp import  TestRequest
from common.ServiceLayerInterface import Service_Layer

class Test_api_04_14(unittest.TestCase):
    '''
    用例名称：请求使用正确的炉子编号和区域编号可以正常得到温度数据
    用例描述：使用正确的炉子编号和区域编号进行请求可以得到正确的响应
    用例编号：api_04_14
    '''

    def setUp(self):
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ======== test  start ========"))
        #预置条件
        self.url = Service_Layer().get_url(0,0,3)
        Logger().logger.info(self.url)
        self.pasrms_furnaceNo = ReadConfig().get_pasrms("furnaceNo")[11]
        self.pasrms_areaNo = ReadConfig().get_pasrms("areaNo")[5]
        self.pasrms = {"furnaceNo": int(self.pasrms_furnaceNo),
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
        if str(self.data_text[1]['data']['furnaceNo']) == self.pasrms_furnaceNo \
                and str(self.data_text[1]['data']['areaNo']) == self.pasrms_areaNo:
                Logger().logger.info("炉编号和区域编号验证成功")
        else:
            Logger().logger.info("炉编号和区域编号验证失败")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        #时间效验

        #温度效验
        if self.data_text[1]['data']['content'] != '':
            for content_list  in range(len(self.data_text[1]['data']['content'])):
                if len(self.data_text[1]['data']['content'][content_list]) == 2:
                    Logger().logger.info("温度时间列表长度为2")
                else:
                    Logger().logger.info("温度时间列表长度不为2")
                    Logger().logger.info(str(Path(__file__).name + " : " + self.File))
                    return False
                if len(str(self.data_text[1]['data']['content'][content_list][0])) == 13:
                    Logger().logger.info("区域时间戳长度符合期望"+ str(content_list))
                else:
                    Logger().logger.info("区域时间戳长度不符合期望")
                    Logger().logger.info(str(Path(__file__).name + " : " + str(content_list)))
                    return False
                if type(self.data_text[1]['data']['content'][content_list][0]) == int  and \
                    type(self.data_text[1]['data']['content'][content_list][1]) == int or float:
                    Logger().logger.info("区域温度和时间 type 符合期望 ")
                else:
                    Logger().logger.info("区域温度和时间 type 不符合期望")
                    Logger().logger.info(str(Path(__file__).name + " : " + self.File))
                    return False
                oldtime = str(self.data_text[1]['data']['content'][content_list][0])
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
        else:
            Logger().logger.info("温度数据为空")
            Logger().logger.info(str(Path(__file__).name + " : " + self.File))
            return False
        Logger().logger.info("接口测试用例：" + str(Path(__file__).name + "  ========= test  end ========"))
    def tearDown(self):
        pass
if __name__ == '__main__':
        a = unittest.main()