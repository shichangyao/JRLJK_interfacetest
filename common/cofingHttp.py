import requests
import json
import common.Log
class TestRequest:
    def __init__(self):
        self.log = common.Log.logger
    def get(self, url, **kwargs):
        '''
        :param url: url
        :param kwargs: **kwargs
        :return: code response or code
        '''
        r = requests.get(url=url,**kwargs)
        if r.status_code == 200:
            response = json.loads(r.text)
            return r.status_code, response
        else:
            return r.status_code

    def post(self,url, **kwargs):
        '''
        :param url:url
        :param kwargs: **kwargs
        :return: code response or code
        '''
        r = requests.post(url=url,**kwargs)
        if r.status_code == 200:
            response = json.loads(r.text)
            return r.status_code, response
        else:
            return r.status_code

if __name__ == '__main__':
    a = TestRequest()
    a.get("http://10.168.2.93:3000/mock/42/api/set_timing/")
