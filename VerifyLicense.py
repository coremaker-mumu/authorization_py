# ---
# @File: VerifyLicense.py
# @Author: Jason
# @Time: 9月 04, 2020
# ---
import codecs
import authorization

def main():
    # 读取文件
    def read_lic(file):
        try:
            # 此处不可以用os，会报错noneType
            f = codecs.open(file)
            plainText = f.read()
            f.close()
            return plainText;
        except:
            print('读取文件异常!')

    try:
        # 文件地址
        file = r'G:\license.lic'
        plainText = read_lic(file)
        # 生成的密钥
        privateKey = b'-----BEGIN RSA PRIVATE KEY-----\nMIICXgIBAAKBgQCz7nzmmpYAmE9T0FMhnJJEa1ECJD989nMgIRpLLLdfykHaCFE4' \
                     b'\nqvY3hyQnHTaCPI9QAAntc86xAQ4OMBJTkQQadChofr4n1loVbOXLacuevwNaOt9g\nIG7mKENsDyr6' \
                     b'/rBTXbWpr23lSU8jfxLm2PyoxvPxaUlL0v8Vuv5EZfCV9wIDAQAB\nAoGBAIggkCIvJflBQhLY82vkdsyInHsQTXAPTD4sjSX' \
                     b'+qKUx8ewwirJitXCBL5rg\nARM7GfmebeRVzzQe5jFZsSPD/ON3lSuqL5dT63cLi1A/uxKZQIyw7VPjP8bUFh1l' \
                     b'\nRWIpEXSTKUugnBIdmx25nHGdHyJkWkvFUzCFBbDIm/iaNaSBAkEAvmU7eVdv6ypv\n7tGvVqm7mMfGUefMCRkv' \
                     b'+1WvSWqPzJZJB9UcSiuY3kjmFG5I4PQdU/IwEtrTwE+8\nC2x0ttVHoQJBAPHuPZPYsU' \
                     b'/3jIIFd872Igj2RItpFM5MZZmRLMPBL5G0cQRsevaq' \
                     b'\nYlev56m5x5tcbZFHtIOn56XazfVvAVpLlpcCQG8gzzHn4x8zydlu8hR3RVPLZunv' \
                     b'\njZvR47ujK4iCdiRHo6C6tqRkBfnYOtK5/DewxF13ArA+oVGiOHPCfe0pV4ECQQCU\nvQgWsY6xv1wfRAVYtHJQWDfkDgLAoq' \
                     b'+ELoD7CPaZ+fnR4m/m3vH/PyKKcrGJjtW+\nD/unRb9hdJhTYJ' \
                     b'/QR9CZAkEAq8zLN6mvmNoY6cx4EvL2lTwQ7shF3wQHa11QgQLi\nfgxYxUkfFCUqycLAA0wRrSIAoOhuXaPGTdDQL6Rw4Exl8A' \
                     b'==\n-----END RSA PRIVATE KEY----- '
        cipher = authorization.RSACipher()
        cipher._private_pem = privateKey
        mechineCode = cipher.decrypt_with_private_key(plainText)
        print(mechineCode)
    except:
        print('程序异常')


if __name__ == '__main__':
    main()
