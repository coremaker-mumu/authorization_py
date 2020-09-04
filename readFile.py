# ---
# @File: readFile.py
# @Author: Jason
# @Time: 9月 03, 2020
# ---
path = r"C:\Users\hzx\Desktop\license.lic"
file = open(path, "r", errors='ignore')
content = file.readlines()
file.close()
print(content)