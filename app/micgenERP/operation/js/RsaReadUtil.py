from OpenSSL import crypto
from Crypto.Cipher import PKCS1_v1_5
import crypto



class RsaReadUtil:

    @staticmethod
    def get_private_key(pfx_file_path, password):
        pfx = crypto.load_pkcs12(open(pfx_file_path, 'rb').read(), password)
        res = crypto.dump_privatekey(crypto.FILETYPE_PEM, pfx.get_privatekey())
        return res.strip()

    @staticmethod
    def get_public_key(cer_file_path):
        cert = crypto.load_certificate(crypto.FILETYPE_PEM, open(cer_file_path, "rb").read())
        res = crypto.dump_publickey(crypto.FILETYPE_PEM, cert.get_pubkey()).decode("utf-8")
        return res.strip()