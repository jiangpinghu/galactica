import requests
import urllib3
from common.severity import TestCaseSeverity
from app.test.common.apiurl import ApiUrl

@allure.epic('')
@allure.feature('登录')
class TestLogin:

    @allure.story('巡检中心')
    @allure.title("查询全部的巡检任务结果")
    @allure.severity(TestCaseSeverity.CRITICAL.get_severity())
    def test_login(self):

        with allure.step("步骤1："):
            header = {}
            data = {"username": "test",
                    "password": "test"}
            urllib3.disable_warnings()

        with allure.step("步骤2："):
            resp = requests.post(url=ApiUrl.user_login, json=data, header=header, verify=False)
            cookie = resp.headers['cookie']

        with allure.step("步骤3："):
            assert resp.status_code == 200,'接口请求失败'.format(resp.status_code)

        with allure.step("步骤4："):
            return cookie





