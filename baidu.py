#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
   作者：莫兰芳
   日期：2020/06/20
   功能： 利用百度的API将文字合成为语音并播放出来。
   版本：1.0
"""

import tkinter
from aip import AipSpeech
import wave
import transformer
from tkinter import ttk
from tkinter import *

file_object = None
aipSpeech = None
file_add = None
perNO = 1


def default_init():
    APP_ID = '20364232'
    API_KEY = 'USxm3n8TjtFLMIryxxPgszu0'
    SECRET_KEY = 'jwtn33XnxbL9vIlxrZ7EwoUdeGbzuEa9 '
    global aipSpeech
    aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    global file_object
    global file_add
    #    file_add = 'C:/Users/pooh/Desktop/1.txt'
    file_object = open(file_add)


def playaudio(audio_file):
    global pyadplay
    import pyaudio
    pyadplay = pyaudio
    chunk = 1024  # 2014kb
    wf = wave.open(audio_file, 'rb')
    p = pyadplay.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(
            wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True)
    data = wf.readframes(chunk)  # 读取数据
    while True:
        data = wf.readframes(chunk)
        if len(data) == 0:
            break
        else:
            print(data)
            stream.write(data)
    stream.stop_stream()  # 停止数据流
    stream.close()
    p.terminate()  # 关闭 PyAudio
    print('wav音乐播放play函数结束！')


def start_t2a(spd=5, pit=5, vol=5, per=3):
    """
    :param spd: 合成语音的讲话速度
    :param pit: 合成语言的讲话音调
    :param vol: 合成语言的音量
    :param per: 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫,5为情感合成-小琪琪
    :return:
    """
    global file_object, aipSpeech
    try:
        n = file_object.read()
        print(n)
    finally:
        file_object.close()
    result = aipSpeech.synthesis(n, 'zh', 1, {'spd': spd, 'pit': pit,
                                              'vol': vol, 'per': per,
                                              })
    print(result)
    if not isinstance(result, dict):
        with open('res/txt2audio.mp3', 'wb') as f:
            f.write(result)
            transformer.starttool("res/txt2audio.mp3", "txt2audio.wav")


if __name__ == '__main__':  # 这里GUI界面的文本地址输入，要将地址中的斜杠全都改成反斜杠
    root = Tk()
    root.title("文字语音合成")
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
        global perNO
        perNO = per[xVariable.get()]
        # print(com.get())  # #获取选中的值方法1
        # print(per[xVariable.get()])  # #获取选中的值方法2



    com.bind("<<ComboboxSelected>>", xFunc)  # #给下拉菜单绑定事件


    def show():
        '''
        开始合成
        '''
        global file_add
        file_add = e1.get()
        default_init()  # 加载百度语言应用,使用的是我的秘钥
        start_t2a(per=perNO)  # 开始文字转语音最终生成wav文件
        playaudio("res/txt2audio.wav")  # 播放
        # print("文本地址 :%s" % e1.get())  # get 变量内容
        # print(file_add)
        # print(perNO)


    Button(root, text='开始合成', width=10, command=show).grid(row=i, column=0, sticky=W, padx=10,
                                                           pady=5)  # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 .
    Button(root, text='退出', width=10, command=root.quit).grid(row=i, column=1, sticky=E, padx=10, pady=5)

    mainloop()




