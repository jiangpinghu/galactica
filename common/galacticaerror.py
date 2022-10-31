from enum import Enum, unique


@unique
class GError(Enum):
    HTTP_CALL_ERROR = {'1000': 'http请求出错'}

    def get_code(self):
        return list(self.value.keys())[0]

    def get_msg(self):
        return list(self.value.values())[0]

    def __str__(self):
        return '错误代码:{0} 错误信息:{1}'.format(self.get_code(), self.get_msg())


class GException(Exception):
    def __init__(self, error: GError):
        self.__init__(error, '')

    def __init__(self, error: GError, message: str):
        self.message = '{0} 附属信息:{1}'.format(str(error), message)
        self.code = error.get_code()
        super().__init__(self.message, error.get_code())
