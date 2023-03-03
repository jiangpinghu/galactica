import RsaUtil
from SignatureUtil import Signature

cer_path = "D:\\********.cer"
pfx_path = "D:\\*******.pfx"
pfx_pwd = "*****"

desc = "把导出私钥及设置的密码和下载的配到生产环境"
print(desc)
print("私钥加密>>>")
pub_en_str = RsaUtil.RsaUtil.En_Private(desc, pfx_path, pfx_pwd)
print(pub_en_str)
print("公钥解密>>>")
pri_de_str = RsaUtil.RsaUtil.De_Public(pub_en_str, cer_path)
print(pri_de_str)

print("公钥加密>>>")
pub_en_str = RsaUtil.RsaUtil.En_Public(desc, cer_path)
print(pub_en_str)

print("私钥解密>>>")
pri_de_str = RsaUtil.RsaUtil.De_Private(pub_en_str, pfx_path, pfx_pwd)
print(pri_de_str)