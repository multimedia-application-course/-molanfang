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
 #### 1、利用百度的API将文字转化为语音，生成mp3格式的音频
 ###### 先定义好秘钥，进行初始化：
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
 ###### 调用百度的API：
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
    result = aipSpeech.synthesis(n, 'zh', 1, {'spd': spd, 'pit': pit,  'vol': vol, 'per': per, })
        print(result)
  #### 2、将mp3格式转化为wav格式的音频，这样就有两种音频格式
 ###### def starttool(mp3path, output, form="wav"):
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
   #### 3、制作GUI的界面方便运行程序
  ###### root = Tk()
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

 ## 四、运行视频
       运行视频在release里。运行视频有两个，一个是用exe运行的，一个是用pycharm运行的  
