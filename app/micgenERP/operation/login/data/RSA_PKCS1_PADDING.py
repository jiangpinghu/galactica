import json
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


class documentRsa():
    __public_key = "MEgCQQCmdtNguZBVB222S6fEmbRjcPLr9pMS0XY3F8NCYmhOeb1VbfAVYaB+by7WD1DI0aHmtIx3ex+ntgIVBUtoJIZFAgMBAAE="
    __private_key = "MIIBPAIBAAJBAKZ202C5kFUHbbZLp8SZtGNw8uv2kxLRdjcXw0JiaE55vVVt8BVhoH5vLtYPUMjRoea0jHd7H6e2AhUFS2gkhkUCAwEAAQJAeNxnZp/0UjgdiTDu80hh951HUtlpOU2JlkCTjXxi/VMYQg8msttZj4ul0NQaJ11gynjbzB0h/7klM6Wlc33FFQIjANws6hTUzKkTp/qMKoNdW/95i1J5pFQOgHDj90wkoUoXLnMCHwDBjKV/9y0VZNmH7Vqm0GARGig1Ivpwa839TrhQUmcCIg7BU86hlDWgg5le21qCXy/3zUZxsHmRnznxjRklO0nj09ECHgkXF/bInx9wGx9dMHLBOqHS/qxwNh7tkUEiX1m2ZQIjALpyBKUeuL+tbJYuFHdycQe7WadRQGtBP3OwYeR9oLrAwnw="

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
    msg = '123456'
    public_key = "MEgCQQCmdtNguZBVB222S6fEmbRjcPLr9pMS0XY3F8NCYmhOeb1VbfAVYaB+by7WD1DI0aHmtIx3ex+ntgIVBUtoJIZFAgMBAAE="
    private_key = "MIIBPAIBAAJBAKZ202C5kFUHbbZLp8SZtGNw8uv2kxLRdjcXw0JiaE55vVVt8BVhoH5vLtYPUMjRoea0jHd7H6e2AhUFS2gkhkUCAwEAAQJAeNxnZp/0UjgdiTDu80hh951HUtlpOU2JlkCTjXxi/VMYQg8msttZj4ul0NQaJ11gynjbzB0h/7klM6Wlc33FFQIjANws6hTUzKkTp/qMKoNdW/95i1J5pFQOgHDj90wkoUoXLnMCHwDBjKV/9y0VZNmH7Vqm0GARGig1Ivpwa839TrhQUmcCIg7BU86hlDWgg5le21qCXy/3zUZxsHmRnznxjRklO0nj09ECHgkXF/bInx9wGx9dMHLBOqHS/qxwNh7tkUEiX1m2ZQIjALpyBKUeuL+tbJYuFHdycQe7WadRQGtBP3OwYeR9oLrAwnw="

    documentRsa = documentRsa(public_key,private_key)
    rsa_encrypt = documentRsa.rsa_encrypt(msg)
    print('加密:',rsa_encrypt)

#pkcs8格式
"""
-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAKZ202C5kFUHbbZLp8SZtGNw8uv2kxLR
djcXw0JiaE55vVVt8BVhoH5vLtYPUMjRoea0jHd7H6e2AhUFS2gkhkUCAwEAAQ==
-----END PUBLIC KEY-----"""


"""
-----BEGIN PRIVATE KEY-----
MIIBVgIBADANBgkqhkiG9w0BAQEFAASCAUAwggE8AgEAAkEApnbTYLmQVQdttkun
xJm0Y3Dy6/aTEtF2NxfDQmJoTnm9VW3wFWGgfm8u1g9QyNGh5rSMd3sfp7YCFQVL
aCSGRQIDAQABAkB43Gdmn/RSOB2JMO7zSGH3nUdS2Wk5TYmWQJONfGL9UxhCDyay
21mPi6XQ1BonXWDKeNvMHSH/uSUzpaVzfcUVAiMA3CzqFNTMqROn+owqg11b/3mL
UnmkVA6AcOP3TCShShcucwIfAMGMpX/3LRVk2YftWqbQYBEaKDUi+nBrzf1OuFBS
ZwIiDsFTzqGUNaCDmV7bWoJfL/fNRnGweZGfOfGNGSU7SePT0QIeCRcX9sifH3Ab
H10wcsE6odL+rHA2Hu2RQSJfWbZlAiMAunIEpR64v61sli4Ud3JxB7tZp1FAa0E/
c7Bh5H2gusDCfA==
-----END PRIVATE KEY-----
"""