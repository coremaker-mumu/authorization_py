# ---
# @File: autorization_ui.py
# @Author: Jason
# @Time: 9月 03, 2020
# ---

from tkinter import *
import tkinter.messagebox
import authorization
import wmi
import os


def main():
    # 根据手动输入的CPU序列号生成lic
    def generate_lic_manual():
        mechanCode = E1.get()
        if mechanCode:
            cipher = authorization.RSACipher()
            cipher.__init__()
            cipherCode = cipher.encrypt_with_public_key(mechanCode)
            save_lic(cipherCode)
        else:
            tkinter.messagebox.askokcancel('温馨提示', '请输入CPU序列号')

    # 读取当前CPU序列号自动生成lic
    def generate_lic_auto():
        c = wmi.WMI()
        cipher = authorization.RSACipher()
        cipher.__init__()
        for cpu in c.Win32_Processor():
            mechineCode = cpu.ProcessorId.strip()
        cipherCode = cipher.encrypt_with_public_key(mechineCode)
        # 打印私钥用来解密
        # print(cipher.get_private_key())
        save_lic(cipherCode)

    # 保存lic文件
    def save_lic(cipherCode):
        path = E2.get()
        if os.path.exists(path):
            # 由于是bytes类型，必须使用wb，读取的时候使用rb
            f = open(path + '/license.lic', 'wb')
            f.write(cipherCode)
            f.close()
        else:
            tkinter.messagebox.askokcancel('温馨提示', '请输入生成地址')

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
            top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('220x150')
    # 设置窗口标题
    top.title('lic生成器')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='手动请输入CPU序列号!', font='Arial -18', fg='red')
    label.pack(expand=1)
    E1 = Entry(top, bd=5)
    E1.pack(expand=1)
    label2 = tkinter.Label(top, text='请输入生成地址!', font='Arial -18', fg='red')
    label2.pack(expand=1)
    E2 = Entry(top, bd=5)
    E2.pack(expand=1)

    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='手动', command=generate_lic_manual)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='自动', command=generate_lic_auto)
    button2.pack(side='left')
    button3 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button3.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
