import base64
import rsa
import os
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

# 生成密钥
pubkey, privkey = rsa.newkeys(512)


# 将公钥以PKCS#1格式写入文件
with open('pub_1.pem', 'w+') as f:
    f.write(pubkey.save_pkcs1().decode('utf-8'))
# 将私钥以PKCS#1格式写入文件
with open('pri_1.pem', 'w+') as f:
    f.write(privkey.save_pkcs1().decode('utf-8'))

# 将公钥由PKCS#1格式转为PKCS#8格式
os.system('openssl rsa --RSAPublicKey_in -in {}.pem -out {}.pem'.format('pub_1', 'pub_8'))

#   将pkcs8公钥转pkcs1公钥
#   openssl rsa -pubin -in pub_8.pem -RSAPublicKey_out -out pub_1.pem

#   将私钥由PKCS#1格式转为PKCS#8格式
os.system('openssl pkcs8 -topk8 -inform PEM -in {}.pem -outform pem -nocrypt -out {}.pem'.format('pri_1', 'pri_8'))

#   将PKCS8格式私钥再转换为PKCS1格式
#   openssl rsa -in pri_8.pem -out pri_1.pem

#导入密钥
# with open('public.pem' ,'r') as f:
#     pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
# with open('private.pem' ,'r') as f:
#     privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

"""
加密 RSA
"""
def rsa_encrypt(message):
    #方法一
    # """
    # 通过读取pem文件来处理RSA加密
    # :param message:
    # :return:crypto_text_base64
    # """
    # with open('public.pem', 'r') as f:
    #     pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
    # crypto_text = rsa.encrypt(message.encode('utf-8'), pubkey)
    # crypto_text_base64 = base64.b64encode(crypto_text).decode()
    # return crypto_text_base64

    #方法二
    """
    采用了Crypto库来实现RSA的加密，引用了PKCS1_v1_5的padding模式，与java Cipher类中的RSA/ECB/PKCS1Padding 等同。
    """
    with open('pub_1.pem', 'rb') as f:
        pubkey = f.read()
    public_key = RSA.importKey(pubkey)
    cipher = PKCS1_v1_5.new(public_key)
    encrpt = base64.b64encode(cipher.encrypt(str(message).encode())).decode()
    return encrpt


"""
解密
"""
def rsa_decrypt(message):
    with open('pri_1.pem', 'r') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())
    message_base64 = base64.b64decode(message.encode('utf-8'))
    message_str = rsa.decrypt(message_base64,privkey).decode()
    return message_str



if __name__ == '__main__':
    message = "Python RSA PKCS#1 转 PKCS#8"
    # 加密
    encrypt = rsa_encrypt(message)
    print('密文：', encrypt)
    # 解密
    decrypt = rsa_decrypt(encrypt)
    print('明文：', decrypt)