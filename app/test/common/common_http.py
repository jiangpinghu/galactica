from enum import Enum

httpheader =  {
    # ":authority": "boss.sit.mcd.com.cn",
    # ":method": "GET",
    # ":path":"/api/inner/boss-api/foundation/web/captcha",
    # ":scheme": "https",
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "mcd-site": "McD-BOSS;PC",
    "referer": "https://boss.sit.mcd.com.cn/login",
    "sec-ch-ua-mobile": "?0",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

# http_base_url = 'https://www.baidu.com'
http_base_url = 'https://boss.sit.mcd.com.cn'


class HttpStatus(Enum):
    HTTP_SUCCESS: int = 200
