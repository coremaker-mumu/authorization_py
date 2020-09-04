# ---
# @File: authorization.py
# @Author: Jason
# @Time: 9月 03, 2020
# ---
import base64

from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA


class RSACipher(object):
    _private_pem = None
    _public_pem = None

    def __init__(self):
        _random_generator = Random.new().read
        _rsa = RSA.generate(1024,  _random_generator)
        self._private_pem = _rsa.exportKey()
        self._public_pem = _rsa.publickey().exportKey()

    def get_public_key(self):
        return self._public_pem

    def get_private_key(self):
        return self._private_pem

    #加载密钥对
    def load_keys(self):
        with open('master-public.pem', "r") as f:
            self._public_pem = f.read()
        with open('master-private.pem', "r") as f:
            self._private_pem = f.read()

    #保存密钥对
    def save_keys(self):
        with open('master-public.pem', 'wb') as f:
            f.write(self._public_pem)
        with open('master-private.pem', 'wb') as f:
            f.write(self._private_pem)

    def decrypt_with_private_key(self, _cipher_text):
        _rsa_key = RSA.importKey(self._private_pem)
        _cipher = Cipher_pkcs1_v1_5.new(_rsa_key)
        _text = _cipher.decrypt(base64.b64decode(_cipher_text), "ERROR")
        return _text.decode(encoding="utf-8")

    def encrypt_with_public_key(self, _text):
        _rsa_key = RSA.importKey(self._public_pem)
        _cipher = Cipher_pkcs1_v1_5.new(_rsa_key)
        _cipher_text = base64.b64encode(_cipher.encrypt(_text.encode(encoding="utf-8")))
        return _cipher_text

    # encrypt with private key & decrypt with public key is not allowed in Python
    # although it is allowed in RSA
    def encrypt_with_private_key(self, _text):
        _rsa_key = RSA.importKey(self._private_pem)
        _cipher = Cipher_pkcs1_v1_5.new(_rsa_key)
        _cipher_text = base64.b64encode(_cipher.encrypt(_text.encode(encoding="utf-8")))
        return _cipher_text

    def decrypt_with_public_key(self, _cipher_text):
        _rsa_key = RSA.importKey(self._public_pem)
        _cipher = Cipher_pkcs1_v1_5.new(_rsa_key)
        _text = _cipher.decrypt(base64.b64decode(_cipher_text), "ERROR")
        return _text.decode(encoding="utf-8")

if __name__ == "__main__":
    cipher = RSACipher()

    text = 'Encrypt with public key, and decrypt with private key'

    cipher.__init__()

    # 公钥加密
    cipherText = cipher.encrypt_with_public_key(text)
    print(cipherText)

    # 私钥解密
    plainText = cipher.decrypt_with_private_key(cipherText)
    print(plainText)


