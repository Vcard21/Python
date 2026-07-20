# elif判斷第二個、第三個、第n個條件，直到都沒有通過的條件，再行else
# ctl+/ = 新增/解除注視
# height =int(input("請輸入你的身高"))
# vip_level =int(input("請輸入你的vip等級(1-5)"))
# day = int(input("請告訴我，今天幾號"))
# 通過if判斷，可以使用多條件判斷的語法
# 第一個條件就是if
if  int(input("請輸入你的身高"))< 120:
    print("身高小於120cm，可以免費")
# 條件的判斷是互斥的，if = ture時，elif就不能用
elif int(input("請輸入你的vip等級(1-5)")) > 3:
    print("vip級別大於3，可以免費")
elif int(input("請告訴我，今天幾號")) == 1:
    print("今天是1號免費日，可以免費")
else:
  print("不好意思，條件都不滿足，需要買票10元")
print("謝謝光臨")
""" 
可以不定義，用input語句直接放入if判斷裡面
判斷是互斥具有順序的
由上至下
滿足1將不會理會2和3
滿足2將不會滿足3
123均不滿足，進入else
else也可以省略不寫，效果等同3個獨立if判斷
不管是if,elif,else都要縮排
"""
# 1.定義一個變量，數字類型，內容隨意
# 2.基於input語句輸入猜想的數字，通過if,elif的組合判斷猜想數字是否和心理數字一致
num1 = 55
if int(input("請輸入第一次猜想的數字:")) == num1:
    print("猜對囉你這個心理學家")
elif int(input("不對，再猜一次")) == num1:
    print("猜對囉你這個心理學家")
elif int(input("不對，再猜最後一次")) == num1:
    print("猜對囉你這個心理學家")
else:
    print(f"Sorry,全都猜錯了，我想的是:{num1}")