from enum import Enum

# from app.micgenERP.operation.common.common_http import http_base_url

http_base_url = 'http://192.168.2.128:8089' #运营系统
# http_base_url = 'http://192.168.2.129:8688' #主系统

class ApiUrl(Enum):
    login: str = {'/fpi/login': '用户登录'}
    captcha: str = {'/fpi/captcha': '获取验证码'}


    def get_url(self):
        return list(self.value.keys())[0]

    def get_desc(self):
        return list(self.value.values())[0]

    def __str__(self):
        return '{0}{1}'.format(http_base_url, self.get_url())
