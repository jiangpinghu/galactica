from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64

# 私钥
private_key = '''-----BEGIN RSA PRIVATE KEY-----
MIIBOwIBAAJBALw1vpIAQHryzWcmAMNOvjqhH3JH+TpZYmjMlzGQ/VROqzNubd9s
c2+3ts/m8PaM5iU2nNnsz+MbREPf5gVuMIECAwEAAQJAWjiJOgPU5RsvS5r0EqvU
lNZX9Lh7yHTAr+wjLieKbcn2yFjElVk36NG4SPhTSQcvjn3+8RyMODBj6tZxJVPK
gQIjAL2u6qxISSiNtL6NXgmHK/D7b9DjcE3Iql6a89tWqYg8bUUCHwD+AvYfPWd8
3jJCEtjko7hpOqK7zLDK7EAqF4+aVA0CIjnme+HtCs/jOan08yCLb2FXDxG/a1eD
CmZofEmW0ZcxgtUCHgkslDUWo6k34TrPsXO4kg2C56O+xdfeZobeqPoa9QIiaLcr
Tf4NZmIUbemTppqwdU5AjbGTpYMApmYwJ3yQLsnGag==
-----END RSA PRIVATE KEY-----
'''

# 公钥
public_key = '''-----BEGIN RSA PUBLIC KEY-----
MEgCQQC8Nb6SAEB68s1nJgDDTr46oR9yR/k6WWJozJcxkP1UTqszbm3fbHNvt7bP
5vD2jOYlNpzZ7M/jG0RD3+YFbjCBAgMBAAE=
-----END RSA PUBLIC KEY-----
'''
def rsa_encrypt(message):
    """校验RSA加密 使用公钥进行加密"""
    cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(base64.b64decode(public_key)))
    cipher_text = base64.b64encode(cipher.encrypt(message.encode())).decode()
    return cipher_text

def rsa_decrypt(text:str):
    """校验RSA加密 使用私钥进行解密"""
    # padding = 4 - len(text) % 4
    # if padding:
    #     text += b'=' * padding
    cipher = Cipher_pkcs1_v1_5.new(RSA.importKey(base64.b64decode(private_key)))
    retval = cipher.decrypt(base64.b64decode(text), 'ERROR').decode('utf-8')
    return retval


if __name__ == '__main__':
    message = '11111111111111111111111111'
    encrypt = rsa_encrypt(message)
    print('加密:',encrypt)
    # miwen = 'YxK5R9NFCI5L0dlqWYr4rllSTooxj3wpoTjXAHjwHeF13VWeUY1zIblBgUocrOUniQYY7CagnmID+OC7O4bPDg=='
    decrypt = rsa_decrypt(encrypt)
    print('解密:',decrypt)