"""
    檔案基本介紹
電腦中有許多可用編碼：
UTF-8
GBK
Big5
等等
每種編碼編出來的二進制語言不一樣

編碼有許多，所以要使用正確的編碼，才能對檔案進行正確的讀寫操作
UTF-8是目前全球通用的編譯格式
除非有特殊需求，否則一律以UTF-8形式進行編碼

總結：

1,編碼就是一種規則集合，紀錄了內容和二進制間進行相互轉換的邏輯。
編碼有許多，最常用的是UTF-8編碼
2,為什麼需要使用編碼
電腦只認識0和1，所以需要將內容翻譯成0和1才能保存在計算機中。
同時也需要編碼，將電腦保存的0和1，反向翻譯回可以識別的內容。
"""

"""
    檔案操作步驟
平常對檔案的基本操作大概可以分為三個步驟
1,打開檔案
2,讀寫檔案
3,關閉檔案
    注意：可以只打開和關閉檔案，不進行讀寫

open函數，可以打開一個已經存在的檔案，或者創建一個新文件
    語法：
open(name,mode,encoding)
示範：f = open('python.txt','r',encoding = "UTF-8)  # 注意，這邊'r'是指唯讀模式


mode三種基礎訪問模式為：
    r(唯讀，默認的模式)
    w(只寫入內容，如果該文件不存在就創建新文件)
    a(更新內容，，新內容將會被寫入已有內容，如果該文件不存在就創建新文件)


name：是要打開目標文件夾名的字符串(可以包含文件所在的具體路徑)
mode：設置打開檔案的模式（訪問模式）：只讀、寫入、追加等
encoding：編碼格式(常用utf-8)

    注意：
此時的'f'是'open'函數的文件對象，對象是python中一種特殊的數據類型，擁有屬性和方法，可以使用對象.屬性
或對象.方法對其進行訪問。
"""

# 打開檔案
f = open('E:/test.txt','r',encoding = "UTF-8")
# encoding的順序不是第三位，所以不能用位置參數，用關鍵字參數指定
print(type(f))


# 讀取檔案 語法1：
# 檔案對象.read(num)，num表示要從檔案中讀取的數據長度，如果沒有傳入num，表示讀取所有數據
# print(f"{f.read(10)}") 如果不傳入數字(num)，那就會傳入所有內容
# print(f"{f.read()}")
# 需要注意的是如果連續讀入read，那就會接著上次read讀取到的內容接續往下

print("--------------------------------")

# 語法2：
# readlines()方法，按照行的方式把整個文件中的內容進行一次性讀取，並且返回列表容器，其中每一行數據為一個元素
# lines = f.readlines()
# print(f"lines的類型及結果是{type(lines)},{lines}")
# 結果是list類型，然後空內容，為什麼?因為上面說過如果多次傳入read，那麼就會接到上次結尾處接續
# 還會讀到\n，讀取到去下一行的意思

# 讀取文件單行 語法：readline()
# line1 = f.readline()
# line2 = f.readline()
# line3  = f.readline()
# print(line1)
# print(line2)
# print(line3)

# for循環讀取文件行
for line in open('E:/test.txt','r',encoding = "UTF-8"):
    print(f"每一行數據{line}")

# 檔案的關閉 close()關閉檔案
# f.close()
# time.sleep(50000) # 尚未學習，只需知道是持續占用檔案的意思

# with.open 自動完成對檔案close
with open('E:/test.txt','r',encoding = "UTF-8") as f: # f就是檔案對象的名稱
    for line in f:
        print(f"每一行數據是{line}")



"""
總結：
1,操作檔案需要通過open函數打開

2,檔案對象有如以下方法：
檔案對象 = open(name,mode,encoding) 打開檔案獲得對象
檔案對象.read(num) 讀取指定長度或不指定讀取全部
檔案對象.readline() 讀取一行
檔案對象.readlines() 讀取全部行，得到「列表」
for line in 檔案對象 for循環檔案，一次循環得到一行數據
檔案對象.close() 關閉檔案對象
with open() as f 通過with open語法打開文件，可以自動關閉

3,檔案讀取完成後要使用close關閉，否則檔案會一直被占用

"""

"""
小練習：
通過.txt，將如下內容複製並保存到:word.txt，文件存儲任意位置
itheima itcast python
itheima python itcast
beiijing shanghai itheima
shenzhen guzngzhou itheima
wuhan hangzhou itheima
zhengzhou bigdata itheima
通過文件讀取操作，讀取此文件，統計itheima單詞出現次數
"""
with open('F:\測試.txt','r',encoding="utf-8") as f_test:
    # 方式1
    # content = f_test.read()
    # count = content.count("itheima") # 可以使用count函數指定內容

    # 方式2
    count = 0  # 使用count變量統計出現次數
    for line in f_test:
        line = line.strip() # 使用strip去除開頭和結尾的空格以及換行符
        # 注意，這邊還可以使用replace代替空格

        words = line.split(" ")
        for word in words:
            if word == "itheima":
                count += 1 # 如果單詞是itheima，進行數量累加1
    print(count)
# f_test.close() ，如果是單純使用open函數記得最後要加close函數