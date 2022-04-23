# -*- coding:utf-8 -*-
import os
import codecs
import configparser
import getpathInfo

proDir = getpathInfo.get_Path()#用于读取配置文件.py文件路径
configPath = os.path.join(proDir, "config.ini")#配置文件路径
class ReadConfig:
    def __init__(self):
        fd = open(configPath,"r",encoding="utf-8")
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8: #处理文件标记BOM b'\xef\xbb\xbf'
            print(data[3:])
            data = data[3:]
            print (data)
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()
        self.cf = configparser.ConfigParser()#  实例化configParser对象
        self.cf.read(configPath,encoding="utf-8")

    def get_http(self, name):
        '''
        :param name: 读取config.ini 下HTTP字段 name对应内容
        :return: 返回config.ini 下HTTP字段 name对应内容
        '''
        value = self.cf.get("HTTP", name)
        return value

    def get_headers(self, name,data = None):
        '''
        :param name: 读取config.ini 下Headers字段 name对应内容
        :param data: 当data = 1 时代表以list形式返回，默认返回str
        :return: 返回config.ini 下Headers字段 name对应内容(str或者列表形式)
        '''
        if data == 1:
            value = self.cf.get("Headers", name)
            value = value.split(",")
        else:
            value = self.cf.get("Headers", name)
        return value

    def get_pasrms(self,name):
        '''
        :param name: 读取 config.ini下Pasrms字段name对应内容
        :return: 返回config.ini 下Pasrms字段 name对应内容(返回形式list)
        '''
        value = self.cf.get("Pasrms",name)
        value = value.split(",")
        return value

    def get_path(self,name):
        '''
        :param name: 读取 config.ini下path字段name对应内容
        :return: 返回config.ini 下path字段 name对应内容(返回形式list)
        '''
        value = self.cf.get("path",name)
        value = value.split(",")
        return value
if __name__ == "__main__":
    print(ReadConfig().get_pasrms("furnaceNo"))

