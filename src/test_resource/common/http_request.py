# -*- coding: utf-8 -*-
# @Author  :  'zyx'
# @Email   : 458757014@qq.com
# @File    : http_request.py
# @Software: PyCharm Community Edition

import requests
from src.utils.my_logger import logger

class HttpRequests:
    def http_request(self,url,method,args):
        if method.lower() == 'get':
            try:
                logger.info('发起get请求')
                result = requests.get(url,args)
            except Exception as e:
                logger.exception('发起get请求出错啦，错误为：%s',e)
                raise e
        elif method.lower()== 'post':
            try:
                logger.info('发起post请求')
                result = requests.post(url,args)
            except Exception as e:
                logger.exception('发起post请求出错啦，错误为：%s',e)
                raise e
        else:
            logger.exception('请求类型错误，发起请求失败')
        return result

if __name__ == '__main__':
    url='http://test.lemonban.com/futureloan/mvc/api/member/recharge'
    param = {'mobilephone':'13311111111','amount':''}
    res=HttpRequests().http_request(url,'get',param)
    print(res.json())