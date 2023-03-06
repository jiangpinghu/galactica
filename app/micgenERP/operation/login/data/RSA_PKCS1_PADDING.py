import json
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


class documentRsa():
    # __public_key = "MEgCQQCmdtNguZBVB222S6fEmbRjcPLr9pMS0XY3F8NCYmhOeb1VbfAVYaB+by7WD1DI0aHmtIx3ex+ntgIVBUtoJIZFAgMBAAE="
    # __private_key = "MIIBPAIBAAJBAKZ202C5kFUHbbZLp8SZtGNw8uv2kxLRdjcXw0JiaE55vVVt8BVhoH5vLtYPUMjRoea0jHd7H6e2AhUFS2gkhkUCAwEAAQJAeNxnZp/0UjgdiTDu80hh951HUtlpOU2JlkCTjXxi/VMYQg8msttZj4ul0NQaJ11gynjbzB0h/7klM6Wlc33FFQIjANws6hTUzKkTp/qMKoNdW/95i1J5pFQOgHDj90wkoUoXLnMCHwDBjKV/9y0VZNmH7Vqm0GARGig1Ivpwa839TrhQUmcCIg7BU86hlDWgg5le21qCXy/3zUZxsHmRnznxjRklO0nj09ECHgkXF/bInx9wGx9dMHLBOqHS/qxwNh7tkUEiX1m2ZQIjALpyBKUeuL+tbJYuFHdycQe7WadRQGtBP3OwYeR9oLrAwnw="

    def __init__(self, rsa_publicKey, rsa_privateKey):
        """
        类初始化，传入config对象内配置的俩字段，内部储存的公钥私钥为不带开头的文本
        :param rsa_publicKey: config.rsa_publicKey
        :param rsa_privateKey: config.rsa_privateKey
        """
        self._public_key = rsa_publicKey
        self._private_key = rsa_privateKey

    def get_public_key(self):
        """
        公开获取拼接完整的公钥
        :return:
        """
        return "-----BEGIN PUBLIC KEY-----\n" + self._public_key + "\n-----END PUBLIC KEY-----"

    def get_private_key(self):
        """
        公开获取拼接完整的私钥
        :return:
        """
        return "-----BEGIN RSA PRIVATE KEY-----\n" + self._private_key + "\n-----END RSA PRIVATE KEY-----"

    @staticmethod
    def _rsa_decrypt(priv_key_str, msg):
        """
        静态方法，根据私钥解密字符串
        :param priv_key_str: 私钥完整
        :param msg: 公钥加密字符串
        :return:
        """

        msg = base64.b64decode(msg)
        length = len(msg)
        #default_length = 128
        default_length = 64 #1024bit的证书用128，2048bit证书用256位
        # 私钥解密
        priobj = Cipher_pkcs1_v1_5.new(RSA.importKey(priv_key_str))
        # 长度不用分段
        if length < default_length:
            return b''.join(priobj.decrypt(msg, b' '))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(priobj.decrypt(msg[offset:offset + default_length], b' '))
            else:
                res.append(priobj.decrypt(msg[offset:], b' '))
            offset += default_length

        return b''.join(res)

    @staticmethod
    def _rsa_encrypt(pub_key_str, msg):
        """
        静态方法,根据公钥加密字符串
        :param pub_key_str: 公钥完整
        :param msg: 待加密json文本
        :return:
        """
        msg = msg.encode('utf-8')
        length = len(msg)
        #单次加密串的长度最大为 (key_size/8)-11,1024bit的证书用100， 2048bit的证书用 200
        default_length = 53
        # default_length = 100
        # 公钥加密
        pubobj = Cipher_pkcs1_v1_5.new(RSA.importKey(pub_key_str))
        # 长度不用分段
        if length < default_length:
            return base64.b64encode(pubobj.encrypt(msg))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(pubobj.encrypt(msg[offset:offset + default_length]))
            else:
                res.append(pubobj.encrypt(msg[offset:]))
            offset += default_length
        byte_data = b''.join(res)

        return base64.b64encode(byte_data)

    def rsa_decrypt(self, msg):
        """
        解密文本到b’二进制值
        :param msg:
        :return:
        """
        return self._rsa_decrypt(self.get_private_key(), msg)

    def rsa_decrypt2str(self, msg):
        """
        获取解密文本
        :param msg: 加密后的文本
        :return:
        """
        return self.rsa_decrypt(msg).decode("utf-8")  # 解密成byte并转为utf-8字符串

    def rsa_decrypt2dict(self, msg):
        """
        获取解密json文本到dict
        :param msg: 加密后的文本
        :return:
        """
        return json.loads(self.rsa_decrypt2str(msg))  # 得到传输过来的数据的dict

    def rsa_encrypt(self, msg, pub_key=None):
        """
        加密一段字符串变成 b'二进制
        :param msg: 待加密文本
        :param pub_key: 公钥，不填默认获取初始化的
        :return:
        """
        pub_key = pub_key or self.get_public_key()
        return self._rsa_encrypt(pub_key, msg)

    def rsa_encrypt2str(self, msg):
        """
        加密文本到文本
        :param msg: 待加密文本
        :return:
        """
        return self.rsa_encrypt(msg).decode("utf-8")  # 加密成待传输的字符串

if __name__ == '__main__':
    msg = 'zzzzzaaaaaa'
    #CS1
    # public_key = "MEgCQQC8Nb6SAEB68s1nJgDDTr46oR9yR/k6WWJozJcxkP1UTqszbm3fbHNvt7bP5vD2jOYlNpzZ7M/jG0RD3+YFbjCBAgMBAAE="
    #CS8
    public_key = "MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBALw1vpIAQHryzWcmAMNOvjqhH3JH+TpZYmjMlzGQ/VROqzNubd9sc2+3ts/m8PaM5iU2nNnsz+MbREPf5gVuMIECAwEAAQ=="
    #CS1
    # private_key = "MIIBOwIBAAJBALw1vpIAQHryzWcmAMNOvjqhH3JH+TpZYmjMlzGQ/VROqzNubd9sc2+3ts/m8PaM5iU2nNnsz+MbREPf5gVuMIECAwEAAQJAWjiJOgPU5RsvS5r0EqvUlNZX9Lh7yHTAr+wjLieKbcn2yFjElVk36NG4SPhTSQcvjn3+8RyMODBj6tZxJVPKgQIjAL2u6qxISSiNtL6NXgmHK/D7b9DjcE3Iql6a89tWqYg8bUUCHwD+AvYfPWd83jJCEtjko7hpOqK7zLDK7EAqF4+aVA0CIjnme+HtCs/jOan08yCLb2FXDxG/a1eDCmZofEmW0ZcxgtUCHgkslDUWo6k34TrPsXO4kg2C56O+xdfeZobeqPoa9QIiaLcrTf4NZmIUbemTppqwdU5AjbGTpYMApmYwJ3yQLsnGag=="
    # CS8
    private_key = "MIIBVQIBADANBgkqhkiG9w0BAQEFAASCAT8wggE7AgEAAkEAvDW+kgBAevLNZyYAw06+OqEfckf5OlliaMyXMZD9VE6rM25t32xzb7e2z+bw9ozmJTac2ezP4xtEQ9/mBW4wgQIDAQABAkBaOIk6A9TlGy9LmvQSq9SU1lf0uHvIdMCv7CMuJ4ptyfbIWMSVWTfo0bhI+FNJBy+Off7xHIw4MGPq1nElU8qBAiMAva7qrEhJKI20vo1eCYcr8Ptv0ONwTciqXprz21apiDxtRQIfAP4C9h89Z3zeMkIS2OSjuGk6orvMsMrsQCoXj5pUDQIiOeZ74e0Kz+M5qfTzIItvYVcPEb9rV4MKZmh8SZbRlzGC1QIeCSyUNRajqTfhOs+xc7iSDYLno77F195mht6o+hr1AiJotytN/g1mYhRt6ZOmmrB1TkCNsZOlgwCmZjAnfJAuycZq"
    documentRsa = documentRsa(public_key,private_key)
    # rsa_encrypt = documentRsa.rsa_encrypt(msg)
    # print('加密:',rsa_encrypt)
    # miwen = "r6nxgVxAX7QmG1P1JINSGopEUc7J40dU-bEG9fnprEK3rBgrKVBeVPAfFWS57mhy2ljhh5flBwzbcAs5WCKd_Q=="
    #java公钥加密生成的密文,解密时需要将'-'和'_'替换成'+'和'/'
    miwen = "r6nxgVxAX7QmG1P1JINSGopEUc7J40dU+bEG9fnprEK3rBgrKVBeVPAfFWS57mhy2ljhh5flBwzbcAs5WCKd/Q=="
    # miwen = "YxK5R9NFCI5L0dlqWYr4rllSTooxj3wpoTjXAHjwHeF13VWeUY1zIblBgUocrOUniQYY7CagnmID+OC7O4bPDg=="
    rsa_decrypt = documentRsa.rsa_decrypt(miwen)
    print('解密:', rsa_decrypt)
