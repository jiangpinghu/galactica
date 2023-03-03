from enum import Enum
from app.micgenERP.operation.login.test_login import TestLogin

Authorization = TestLogin

httpheader =  {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9",
    "Authorization":"",
    "Connection":"keep-alive",
    "Cookie":"isChecked=false; name=; password=",
    "Host":"192.168.2.129:8688",
    "referer": "http://192.168.2.129:8688/front/login",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
}

# http_base_url = 'http://192.168.2.128:8089' #运营系统
# http_base_url = 'http://192.168.2.129:8688' #主系统


class HttpStatus(Enum):
    HTTP_SUCCESS: int = 200
