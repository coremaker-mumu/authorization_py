# ---
# @File: mechineCode.py
# @Author: Jason
# @Time: 9月 03, 2020
# ---
import wmi

c = wmi.WMI()

# # 硬盘序列号
for physical_disk in c.Win32_DiskDrive():
    print(physical_disk.SerialNumber)

# CPU序列号
for cpu in c.Win32_Processor():
    print(cpu.ProcessorId.strip())

# 主板序列号
for board_id in c.Win32_BaseBoard():
    print(board_id.SerialNumber)

# mac地址
for mac in c.Win32_NetworkAdapter():
    print(mac.MACAddress)

# bios序列号
for bios_id in c.Win32_BIOS():
    print(bios_id.SerialNumber.strip)