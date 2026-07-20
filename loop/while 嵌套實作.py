# # 補充知識-print 輸出不換行
# print("hello", end = "")
# print("world", end = "")
# # 使用end:''or""就可以不換行
#
# # 補充知識-製表符\t
# # 特殊符號\t，效果等同於Tab鍵，效果為對齊輸出
# print("hello\tword")
# print("itheima\tbest")

# 通過while循環輸出九九乘法表

# 定義外層循環的控制變量
i = 1
while i <= 9:
    # 定義內層循環的控制變量
    j = 1
    while j <= i:
        # 內層循環不換行
        print(f"{j} * {i}={j*i}\t",end='')
        j += 1
    i += 1
    print() #print空內容就是輸出一個換行

# 內層循環就是執行完一次後回頭看while條件，滿足就再繼續一次。不滿足就結束往外層循環走