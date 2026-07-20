"""
任務規格書：

變數：day（從 1 開始）、rose（累積數量）、sunflower（累積數量）。

循環：while day <= 100。

判斷：if day < 50 執行玫瑰累加；else 執行向日葵累加。

最後輸出：兩者的總數。

進階挑戰（給喜歡優化的你）：
如果你不想要寫兩個 print，能不能試著用一個 Dictionary (字典) 來存放結果？
例如：result = {"玫瑰": 0, "向日葵": 0}。
然後在 if 裡面直接操作 result["玫瑰"] += 10。
"""
day = 1

rose_total = 0

sunflower_total = 0

while day <= 100:

    print(f"今天是第{day}天，準備表白")
    if day <= 50:

        rose_total += 10

    else:
        sunflower_total += 10

    print("小美，我喜歡你")
    day += 1
print(f"堅持到第{day - 1}天，總共送了{rose_total}支玫瑰、{sunflower_total}支向日葵")
"""
&&&錯誤示範&&& 錯誤很重要，這樣才知道自己邏輯哪邊有問題
day = 1
rose = 10
rose_total = 0
sunflower = 10
sunflower_total = 0
while day <= 100:
    print(f"今天是第{day}天，準備表白") 
    day += 1   
    if day <= 50:       
        rose += 10        
        rose_total += rose
    else:
        sunflower +=10
        sunflower_total += sunflower       
   print("小美，我喜歡你")  
print(f"堅持到第{day - 1}天，總共送了{rose_total}支玫瑰、{sunflower_total}支向日葵")，玫瑰及向日葵的輸出結果太大了，為什麼?

問題出在你的 rose += 10 和 rose_total += rose 這兩行
讓我們模擬一下程式的執行過程：

第 1 天： rose 變成了 20（原本是 10），rose_total 變成了 20。

第 2 天： rose 變成了 30，rose_total 變成了 20 + 30 = 50。

第 3 天： rose 變成了 40，rose_total 變成了 50 + 40 = 90。

"""