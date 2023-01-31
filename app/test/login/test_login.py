import requests
import urllib3
import allure
import ddddocr
import urllib
from urllib.request import urlretrieve
from common.severity import TestCaseSeverity
from app.test.common.apiurl import ApiUrl
from app.test.common.common_http import httpheader



@allure.epic('')
@allure.feature('登录')
class TestLogin:

    @allure.story('获取图片验证码')
    @allure.title("验证码")
    @allure.severity(TestCaseSeverity.CRITICAL.get_severity())
    def test_captcha(self):

        with allure.step("步骤1：调用验证码接口，获取图片"):
            resp = requests.get(url=ApiUrl.captcha,headers=httpheader,verify=False)
            image = resp.json()["data"]["image"]
            auth =  resp.json()["data"]["auth"]
            urllib.request.urlretrieve(image, "code.png")
            ocr = ddddocr.DdddOcr()
            res = ""
            with open("code.png", "rb") as f:  # 打开图片
                img_bytes = f.read()  # 读取
            code = ocr.classification(img_bytes)  # 识别
            print("返回code: " + code)

        with allure.step("步骤2：接口断言"):
            assert resp.json()["code"] == "SUCCESS" and resp.json()["msg"] == "成功","接口返回失败：{}".format(resp.json()["msg"])

        with allure.step("步骤3：返回验code和auth"):
            return code,auth


    @allure.story('用户登录')
    @allure.title("登录")
    @allure.severity(TestCaseSeverity.CRITICAL.get_severity())
    def test_login(self):

        with allure.step("步骤1：输入用户名、密码"):
            headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
            code = self.test_captcha()[0]
            captchaAuth = self.test_captcha()[1]
            data = {"adid": "test-cm-admin",#用户名
                    "password": "test@mcd",#密码
                    "captcha":code,#验证码
                    "captchaAuth":captchaAuth#用户身份验证
                    }
            print(data)
            urllib3.disable_warnings()

        with allure.step("步骤2：调用登录接口"):
            resp = requests.post(url=ApiUrl.user_login, json=data, headers=headers, verify=False)
            # authorization = resp.json()["data"]["authorization"]
            # print(authorization)

        with allure.step("步骤3：接口断言"):
            assert resp.json()["code"] == "SUCCESS" and resp.json()["msg"] == "成功",'接口请求失败：错误码{}，错误文案{}'.format(resp.json()["code"],resp.json()["msg"])

        # with allure.step("步骤4：返回authorization"):
        #     return authorization





