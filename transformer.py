#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
"""
   作者：莫兰芳
   日期：2020/06/20
   功能： 将MP3格式的音频转化为WAV格式
   版本：1.0
"""

import sys
import os

pypath = sys.executable
print(pypath)


def pipsetup(packname):
    packcmd = "%s -m pip install %s" % (pypath, packname)
    try:
        p = os.popen(packcmd)
    except UnicodeDecodeError:
        print("返回文本的格式编码有问题！")
    try:
        print(p.read())  # 执行cmd并得到返回的字符串
    except UnicodeDecodeError:
        print("读取返回值失败，大概意思是编码不对，不过已经执行完毕了")


def starttool(mp3path, output, form="wav"):
    if os.path.exists("ffmpeg.exe") and os.path.exists(
            "ffplay.exe") and os.path.exists("ffprobe.exe"):
        try:
            from pydub import AudioSegment
        except BaseException:
            print("本地不存在音乐处理支持库，开始安装pydub...")
            pipsetup("pydub")
            from pydub import AudioSegment

        # AudioSegment.converter = r"D:\ffmpeg\bin\ffmpeg.exe"

        def trans_mp3_to_wav(filepath):
            if os.path.exists(mp3path):
                song = AudioSegment.from_mp3(filepath)
                print(song)
                song.export("res/%s" % output, format=form)
            else:
                print("mp3目标文件不存在!")

        trans_mp3_to_wav(mp3path)


if __name__ == '__main__':
    # pipsetup("pydub")
    starttool(r"C:\Users\pooh\Desktop\1.mp3", "music.wav")   # 测试
    # starttool("res/txt2audio.mp3", "txt2audio.wav")
