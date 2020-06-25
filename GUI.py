# -*- coding:UTF-8 -*-
"""
   作者：莫兰芳
   日期：2020/06/24
   功能：测试程序的GUI界面
   版本：1.0
"""

import tkinter
from tkinter import ttk
from tkinter import *

root = Tk()
root.title("文字语音合成")
file = None
num = 1
# root.geometry("600x300")  # 设置框的大小
'''
获得文本地址
'''
Label(root, text='文本地址 :').grid(row=0, column=0)  # 对Label内容进行 表格式 布局
v1 = StringVar()  # 设置变量 .
e1 = Entry(root, textvariable=v1)  # 用于储存 输入的内容
e1.grid(row=0, column=1, padx=10, pady=5)  # 进行表格式布局 .

'''
发音人选择
'''
i = 1
Label(root, text='发音人选择 :').grid(row=i, column=0)  # 对Label内容进行 表格式 布局
xVariable = tkinter.StringVar()  # #创建变量，便于取值
com = ttk.Combobox(root, textvariable=xVariable)  # #创建下拉菜单
com.grid(row=i, column=1)  # #将下拉菜单绑定到窗体
i = i + 1
com["value"] = ("普通女声", "普通男生", "度逍遥", "度丫丫", "小琪琪")  # #给下拉菜单设定值


# com.current(1)  # #设定下拉菜单的默认值为第2个，即普通男生

def xFunc(event):
    per = {"普通女声": 0, "普通男生": 1, "度逍遥": 2, "度丫丫": 3, "小琪琪": 4, }
    print(com.get())  # #获取选中的值方法1
    print(per[xVariable.get()])  # #获取选中的值方法2


com.bind("<<ComboboxSelected>>", xFunc)  # #给下拉菜单绑定事件


def show():
    print("文本地址 :%s" % e1.get())  # get 变量内容


Button(root, text='开始合成', width=10, command=show).grid(row=i, column=0, sticky=W, padx=10,
                                                       pady=5)  # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 .
Button(root, text='退出', width=10, command=root.quit).grid(row=i, column=1, sticky=E, padx=10, pady=5)
mainloop()
