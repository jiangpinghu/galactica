from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
import base64

# 私钥
private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIBPAIBAAJBAIkZFxKDhpm2s/chAy+S7jh3yjoQHs9Wp7waAxg6SEH/6BQWDOlc
0K7KXyCn3yXTXueQ3ey2n1fweLqV6xz57BMCAwEAAQJAfEoIxroCjtw57zM4hiq4
WO0Qou72X5X53ufeIlrDeDlat2DgTgAoHb2vExLRc++KVi7gWvLELeY9JJYSLbjq
oQIjALyoVNwY4HzB4gAMbStoFULBQIrmJh99AIQKpvu7aNKWTYsCHwC6CTWZBM3c
UX0Ce0H4kz4GxIw1uG+hn+PGOFYLPJkCIhOtq0xZ+/CHeL9wjGKetLkF12mloAxg
yZD8W3aekcyFiQkCHwCqSBGyLU6M0l3dbprU/1lv8mnwJhCv3N0tK5W+lUkCIg3q
xnRfXR5SYkXvjmdVgOyB9AOSPO+kCB7Q/OzOSBv326w=
-----END RSA PRIVATE KEY-----
'''

# 公钥
public_key = '''-----BEGIN RSA PUBLIC KEY-----
MEgCQQCJGRcSg4aZtrP3IQMvku44d8o6EB7PVqe8GgMYOkhB/+gUFgzpXNCuyl8g
p98l017nkN3stp9X8Hi6lesc+ewTAgMBAAE=
-----END RSA PUBLIC KEY-----
'''
def rsa_encrypt(message):
    """校验RSA加密 使用公钥进行加密"""
    cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(public_key))
    cipher_text = base64.b64encode(cipher.encrypt(message.encode())).decode()
    return cipher_text


def rsa_decrypt(text):
    """校验RSA加密 使用私钥进行解密"""
    cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(private_key))
    retval = cipher.decrypt(base64.b64decode(text), 'ERROR').decode('utf-8')
    return retval


if __name__ == '__main__':
    # message = '111111111111111111111111111111111111111111111111111'
    encrypt = rsa_encrypt(message)
    print('加密:',encrypt)
    decrypt = rsa_decrypt(encrypt)
    print('解密:',decrypt)