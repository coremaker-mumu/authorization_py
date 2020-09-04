# ---
# @File: VerificationCode.py
# @Author: Jason
# @Time: 9月 04, 2020
# ---
import random

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_code(code_len=4):
    """生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    """
    code = ''
    for _ in range(code_len):
        # 产生0到字符串长度减1范围的随机数作为索引
        index = random.randrange(0, len(ALL_CHARS))
        # 利用索引运算从字符串中取出字符并进行拼接
        code += ALL_CHARS[index]
    return code

if __name__ == "__main__":
    for _ in range(2):
        print(generate_code(6))
