# 语音播放
## 一、项目主题及设计目的 
        主题：通过利用百度的API来将文本信息转化为语音  
        目的：可以方便人们没办法看文字的时候来听这些语音，比如在导航的时候，通常都是听语音的；眼睛不方便的人可以通过语音来“看书”等等  
## 二、软件简介
       1、开发工具  
        环境：Windows 10  
        软件：Pycharm  
        语言：Python  
       2、作品运行环境  
         Windows 10 x64  
       3、使用的方法  
         （1）打开方式：在路径”dist\baidu\”下找到baidu.exe;双击之后即可运行；或者使用pycharm运行该项目，在baidu.py的文件中来run 程序也可以运行；  
         （2）运行：在文本地址中填写你要播放的文本的地址，（注：地址中的斜杠要改为反斜杠）；然后进行发音人的选择：选择你想要的发音人；点击“开始合成”来进行合成音频播放  
 ## 三、实现过程
 1、利用百度的API将文字转化为语音，生成mp3格式的音频    
       先定义好秘钥，进行初始化：  
       调用百度的API：
 2、将mp3格式转化为wav格式的音频，这样就有两种音频格式    
 3、制作GUI的界面方便运行程序  
 （详细文档可以在release中看到）
 ## 四、运行视频
       运行视频在release里。运行视频有两个，一个是用exe运行的，一个是用pycharm运行的  
