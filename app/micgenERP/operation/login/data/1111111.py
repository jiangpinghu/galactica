import sys
# rsa
import base64
import rsa
import os
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from rsa import PublicKey, common, transform, core

pubkey, privkey = rsa.newkeys(512)


# 将公钥以PKCS#1格式写入文件
with open('pub_11.pem' ,'w+') as f:
    f.write(pubkey.save_pkcs1().decode('utf-8'))
# 将私钥以PKCS#1格式写入文件
with open('pri_11.pem' ,'w+') as f:
    f.write(privkey.save_pkcs1().decode('utf-8'))

# 将公钥由PKCS#1格式转为PKCS#8格式
os.system('openssl rsa --RSAPublicKey_in -in {}.pem -out {}.pem'.format('pub_11', 'pub_88'))

# 将私钥由PKCS#1格式转为PKCS#8格式
os.system('openssl pkcs8 -topk8 -inform PEM -in {}.pem -outform pem -nocrypt -out {}.pem'.format('pri_11', 'pri_88'))



#导入密钥
with open('pub_11.pem' ,'rb') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read())
with open('pri_11.pem' ,'rb') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read())
def f(cipher, pubkey):
    public_key = PublicKey.load_pkcs1(pubkey)
    encrypted = transform.bytes2int(cipher)
    decrypted = core.decrypt_int(encrypted, public_key.e, public_key.n)
    text = transform.int2bytes(decrypted)

    if len(text) > 0 and text[0] == '\x01':
        pos = text.find('\x00')
        if pos > 0:
            return text[pos + 1:]
        else:
            return None


if __name__ == '__main__':
    cipher = '123456'
    ff = f(cipher,pubkey)
    print(ff)