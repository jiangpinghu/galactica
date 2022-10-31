from enum import Enum

httpheader = {'Content-Type': 'application/json',
              'cookie': 'cookie'
              }

http_base_url = 'https://www.baidu.com'


class HttpStatus(Enum):
    HTTP_SUCCESS: int = 200
