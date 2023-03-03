from Crypto.Cipher import PKCS1_v1_5 as PKCS1_v1_5_cipper
from Crypto.PublicKey import RSA

import binascii
import base64
import RsaReadUtil


class RsaUtil:
    @staticmethod
    def En_Core(srcdata, publick_keys):
        rsakey = RSA.importKey(publick_keys)
        cipher = PKCS1_v1_5_cipper.new(rsakey)
        block_size = int(rsakey.n.bit_length() / 8 - 11)
        en_code_data = base64.b64encode(str(srcdata).encode("utf-8"))
        print(en_code_data)
        en_data = bytes()
        while en_code_data:
            input_data = en_code_data[:block_size]
            en_code_data = en_code_data[block_size:]
            en_data += cipher.encrypt(input_data)
        return en_data.hex()

    @staticmethod
    def En_Public(src_data, cer_key_path):
        # ---公钥加密---#
        return RsaUtil.En_Core(src_data, RsaReadUtil.RsaReadUtil.get_public_key(cer_key_path))

    @staticmethod
    def En_Private(src_data, pfx_key_path, pfx_pwd):
        # ---私钥加密---#
        return RsaUtil.En_Core(src_data, RsaReadUtil.RsaReadUtil.get_private_key(pfx_key_path, pfx_pwd))

    @staticmethod
    def De_Core(srcdata, private_kes):
        rsakey = RSA.importKey(private_kes)
        cipher = PKCS1_v1_5_cipper.new(rsakey)
        block_size = int(rsakey.n.bit_length() / 8)

        de_code_data = binascii.unhexlify(srcdata)
        out_data = bytes()
        while de_code_data:
            input_data = de_code_data[:block_size]
            de_code_data = de_code_data[block_size:]
            out_data += cipher.decrypt(input_data, '')
        return str(base64.b64decode(out_data), encoding="utf-8")

    @staticmethod
    def De_Private(src_data, pfx_key_path, pfx_pwd):
        # ---私钥解密---#
        return RsaUtil.De_Core(src_data, RsaReadUtil.RsaReadUtil.get_private_key(pfx_key_path, pfx_pwd))

    @staticmethod
    def De_Public(src_data, cer_key_path):
        # ---公钥解密---#
        return RsaUtil.De_Core(src_data, RsaReadUtil.RsaReadUtil.get_public_key(cer_key_path))

