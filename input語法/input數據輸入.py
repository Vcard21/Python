#
print("告訴我你是誰?")
name =input()
print("我知道了，你是:%s" % name)

# input可以直接寫在括號後面，相當於在後面放一個print
name_1 = input("第二次你是誰")
print("知道了，你是%s" % name_1)

# 輸入數字類型
num = input("請告訴我的你銀行卡密碼")
# 數據類型轉換
num =int(num)
print("你的銀行卡密碼的類型是:  ", type(num))

# input 默認接收字符串，有需要的話自己轉變成其他類型
