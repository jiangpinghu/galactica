import rsa

from rsa import common, transform, core

import os
'''
私钥加密,公钥解密
'''
def _pad_for_encryption(message, target_length):

    max_msglength = target_length - 11

    msglength = len(message)

    if msglength > max_msglength:

        raise OverflowError(

        "%i bytes needed for message, but there is only"

        " space for %i" % (msglength, max_msglength)

        )

    padding = b""

    padding_length = target_length - msglength - 3

    while len(padding) < padding_length:

        needed_bytes = padding_length - len(padding)

        new_padding = os.urandom(needed_bytes + 5)

        new_padding = new_padding.replace(b"\x00", b"")

        padding = padding + new_padding[:needed_bytes]

    assert len(padding) == padding_length

    return b"".join([b"\x00\x02", padding, b"\x00", message])

def decrypt(data: bytes, d, n):

    num = transform.bytes2int(data)

    decrypto = core.decrypt_int(num, d, n)

    out = transform.int2bytes(decrypto)

    sep_idx = out.index(b"\x00", 2)

    out = out[sep_idx + 1 :]

    return out

def encrypt(data: bytes, d, n):

    keylength = common.byte_size(n)

    padded = _pad_for_encryption(data, keylength)

    num = transform.bytes2int(padded)

    decrypto = core.encrypt_int(num, d, n)

    out = transform.int2bytes(decrypto)

    return out

if __name__ == '__main__':

    pubkey, privkey = rsa.newkeys(512)

    data = '123456789'

    data2b = data.encode('utf8')

    edata = encrypt(data2b, pubkey.e, pubkey.n)
    print('私钥加密:',edata)
    ddata = decrypt(edata, privkey.d, privkey.n)
    print('公钥解密:', ddata)



