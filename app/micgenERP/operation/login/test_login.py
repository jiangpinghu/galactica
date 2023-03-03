import requests
import urllib3
import allure
import ddddocr
import urllib
from faker import Faker
from urllib.request import urlretrieve
from common.severity import TestCaseSeverity
from app.micgenERP.operation.common.apiurl import ApiUrl


fake = Faker('zh_CN')  # 设置语种
requestRandom = fake.pystr(min_chars=None, max_chars=19)  # 随机生成字符串,限制长度

@allure.epic('micgenERP(运营系统)')
@allure.feature('用户登录')
class TestLogin():


    @allure.story('获取图片验证码')
    @allure.title("验证码")
    @allure.severity(TestCaseSeverity.CRITICAL.get_severity())
    def test_captcha(self):

        with allure.step("步骤1：调用验证码接口，获取图片"):
            headers = {
                "accept": "application/json, text/plain, */*",
                "accept-encoding": "gzip, deflate",
                "accept-language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "referer": "http://192.168.2.129:8688/front/login",
                "Host": "192.168.2.129:8688",
                "Cookie": "isChecked=false; name=; password=",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            }

            data = {
                "length":150,
                "width":40,
                "requestRandom":requestRandom
            }
            urllib3.disable_warnings()
            resp = requests.get(url=ApiUrl.captcha,headers=headers,params=data,verify=False)

        with allure.step("步骤2：接口断言"):
            assert resp.json()["msg"] == "OK","接口请求失败：{}".format(resp.json()["msg"])

        with allure.step("步骤3:识别验证码"):
            image = resp.json()["data"]
            urllib.request.urlretrieve(image, "../login/data/code.png")
            ocr = ddddocr.DdddOcr()
            res = ""
            with open("../login/data/code.png", "rb") as f:  # 打开图片
                img_bytes = f.read()  # 读取
            code = ocr.classification(img_bytes)  # 识别
            print("返回code: " + code)

        with allure.step("步骤4：返回验code"):
            return code


    @allure.story('手机号密码登录')
    @allure.title("手机号密码登录")
    @allure.severity(TestCaseSeverity.CRITICAL.get_severity())
    def test_login(self):

        with allure.step("步骤1：输入用户名,密码,验证码"):
            headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-encoding": "gzip, deflate",
                "Accept-language": "zh-CN,zh;q=0.9",
                "Connection": "keep-alive",
                "Referer": "http://192.168.2.129:8688/front/login",
                "Origin": "http://192.168.2.129:8688",
                "Host": "192.168.2.129:8688",
                "Content-Length":"103",
                "Content-Type":"application/json;charset=UTF-8",
                "Cookie": "isChecked=false; name=; password=",
                "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
            }
            code = self.test_captcha()
            data = {"username": "13900000004",#用户名
                    "password": "admin123!",#密码
                    "captcha":123456,#验证码---测试环境暂时写死
                    "requestRandom":requestRandom
                    }

        with allure.step("步骤2：调用登录接口"):
            urllib3.disable_warnings()
            resp = requests.post(url=ApiUrl.login, json=data, headers=headers, verify=False)

        with allure.step("步骤3：接口断言"):
            assert  resp.json()["msg"] == "登录成功",'接口请求失败：错误码{}，错误文案{}'.format(resp.json()["errno"],resp.json()["msg"])

        with allure.step("步骤4：返回access_token"):
            access_token = resp.json()["data"]["access_token"]
            # print(access_token)
            return access_token





