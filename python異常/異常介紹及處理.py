"""
異常就是bug
bug的來由：
1945年9月9日，曾經的電腦(馬克二號計算機)無法正常工作，發現飛蛾在其中且被電死了
自此以後，導致軟體無法工作時就稱為bug
"""
# 通過open，讀取一個不存在的文件
# f = open("D:/abc.txt",'r',encoding = "utf-8")

"""
總結：
1,什麼是異常：
異常就是程序運行的過程中出現了錯誤
2,bug是什麼意思：
bug就是指異常/錯誤的意思，歷史上因為小蟲子導致電腦失靈的案例，所以延續至今
"""

""""
        基本語法：
try:
    可能發生錯誤的代碼
except:
    如果出現異常執行的代碼
"""

# # 基本捕獲語法
# try:
#     F_catch = open("D:/abc.txt",'r',encoding = "utf-8")
# except:
#     print("出現bug了，因為文件不存在，我將模式改為w")
#     F_catch = open("F:/abc.txt",'w',encoding = "utf-8")
#
# # 捕獲指定bug
# # 語法 except NameError as e:
# # 後面的e就是個變量，把錯誤資訊存到變量中
# try:
#      print(name)
# except NameError as e:
#     print("出現變量未定義的bug")
#     print(e)
#
# # 捕獲多個異常
# # 語法 except(NameError,ZeroDivisionError): 把要捕獲的bug類型名字放到except後，用元組的方式進行輸出
# try:
#     print(name)
# except (NameError, ZeroDivisionError) as e:
#     print("出現了變量未定義或者除以0的bug")
#
# 捕獲所有bug
try:
    f=open("F:/123.txt",'r',encoding='utf-8')
except Exception as e: # 不指定bug類型或是使用關鍵字Exception就都是捕獲全部bug的意思
    # exception 就是最高級的bug，其他bug類型都是except的衍伸
    f=open("F:/123.txt",'w',encoding='utf-8')
else:
    print("好高興，沒有異常")
# 捕獲語法還可以用else，代表如果沒有抓到bug

finally:  # finally代表不管有沒有bug，都要執行的代碼
    print("我是finally，有沒有異常都要執行")
    f.close()

"""
總結：

    1,為什麼要特別抓bug?
在可能發生bug的地方進行捕獲，當bug出現時提供解決方法而不是任其崩潰

    2,捕獲bug的語法
try
except
else
finally

    3,如何捕獲所有異常
直接寫except
或寫關鍵字exception
"""