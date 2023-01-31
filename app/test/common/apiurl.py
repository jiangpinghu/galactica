from enum import Enum

from app.test.common.common_http import http_base_url


class ApiUrl(Enum):
    user_login: str = {'/login': '用户登录'}
    captcha: str = {'/api/inner/boss-api/foundation/web/captcha': '获取验证码'}


    def get_url(self):
        return list(self.value.keys())[0]

    def get_desc(self):
        return list(self.value.values())[0]

    def __str__(self):
        return '{0}{1}'.format(http_base_url, self.get_url())
