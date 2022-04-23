from readconfig import ReadConfig
from common.Log import Logger
from common.cofingHttp import  TestRequest

class Service_Layer():
    def __init__(self):
        pass
        self.furnaceNo = "furnaceNo"
        self.areaNo = "areaNo"
        self.url = ["JRL_url"]
        self.path = ["JRLJK_page_path","JRLJK_set_path"]
        self.sign = 'sign'
        self.dur_time = 'dur_time'
        self.interval = "interval"
        self.Ordinary_password = "Ordinary_password"
        self.Advanced_password = "Advanced_password"
    def get_furnaceNo(self,number):
        '''
        读取config.ini中 furnaceNo
        :param number:  config.ini 中[Pasrms]下furnaceNo的下标数(type:int)
        :return: config.ini 中 furnaceNo对应number下标的值（type:str）
        '''
        furnaceNo = ReadConfig().get_pasrms(self.furnaceNo)[number]
        return furnaceNo

    def get_areaNo(self,number):
        '''
        读取config.ini中 areaNo
        :param number:  config.ini 中[Pasrms]下areaNo的下标数(type:int)
        :return: config.ini 中 areaNo对应number下标的值（type:str）
        '''
        areaNo = ReadConfig().get_pasrms(self.areaNo)[number]
        return areaNo

    def get_url(self,url_number,path_number,number):
        '''
        获取url
        :param url_number: self.url下标数(type:int)
        :param path_number: self.path下标数(type:int)
        :param number: config.ini 中[path]下的下标数(type:int)
        :return: url（type:str）
        '''
        url = ReadConfig().get_http(self.url[url_number]) + ReadConfig().get_path(self.path[path_number])[number]
        if url ==  "":
            Logger().logger.info("url返回值为空")
            return False
        else:
            return url

    def get_pasrms(self,furnaceNo_number,areaNo_number):
        '''
        :param furnaceNo_number: config.ini 中[Pasrms]下furnaceNo的下标数(type：int)
        :param areaNo_number: config.ini 中[Pasrms]下areaNo的下标数(type：int)
        :return: pasrms
        '''
        return {self.furnaceNo: Service_Layer().get_furnaceNo(furnaceNo_number),self.areaNo: Service_Layer().get_areaNo(areaNo_number)}

    def get_sign(self,number):
        '''
        :param number: sign 下标数(type: int)
        :return: sign 的值 (type: str)
        '''
        sign =  ReadConfig().get_pasrms(self.sign)[number]
        return sign

    def get_dur_time(self,number):
        '''
        :param number: dur_time下标数(type: int)
        :return: dur_time的值(type: str)
        '''
        dur_time = ReadConfig().get_pasrms(self.dur_time)[number]
        return  dur_time

    def get_interval(self,number):
        '''
        :param number: dur_time下标数(type: int)
        :return: dur_time的值(type: str)
        '''
        interval = ReadConfig().get_pasrms(self.interval)[number]
        return  interval
    def get_page(self,number):
        '''
        :param number: page下标数(type: int)
        :return: dur_time的值(type: str)
        '''
        page = ReadConfig().get_pasrms(self.interval)[number]
        return  page

    def get_password(self,data):
        '''
        :param data: 为1时代表高级密码，其他为普通密码默认0代表普通面膜
        :return: password (type: string)
        '''
        if data == 1:
            password = ReadConfig().get_pasrms(self.Advanced_password)[0]
        else:
            password = ReadConfig().get_pasrms(self.Ordinary_password)[0]
        return password

    def get_area_count(self,number):
        '''
        :param number: 指定炉号下标
        :return:指定炉的区域温度
        '''
        url = Service_Layer().get_url(0, 0, 3)
        pasrms = ReadConfig().get_pasrms("furnaceNo")[number]
        nepasrms = {"furnaceNo":pasrms}
        area_count = TestRequest().get(url, params=nepasrms)
        Logger().logger.info(area_count)
        if area_count == "":
            Logger().logger.info("area_count返回值为空")
            return False
        if area_count[1] == "":
            Logger().logger.info("area_count[1]返回值为空")
            return False
        if "errmsg" in area_count[1].keys():
                Logger().logger.info(area_count[1]['errmsg'])
                return  False
        else:
            area_count = area_count[1]['data']['area_count']
            Logger().logger.info("所获取指定炉的炉区域为： "+str(area_count))
            return area_count

if __name__ == "__main__":
    print (Service_Layer().get_sign(0),Service_Layer().get_dur_time(0))
    pass


