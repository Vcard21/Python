"""
無限次機會，直到猜中為止
每一次猜不中，提示大或小
猜完數字後提示猜了幾次
隨機數可以使用improt random num = random.randint(1,100)
"""
# 獲取範圍在1-100的隨機數字
import random


num = random.randint(1,100)
# 通過一個布爾類型的變量，判斷循環是否繼續的標記
guess = True

# 定義一個變量去做次數的計算
count = 0

while guess  :
    guess_num = int(input("輸入數字"))
    count += 1
# 定義不用先寫，可以寫在while判斷裡
    if guess_num == num :
        print("猜中了")
        # 設置為False就是終止循環的條件
        guess = False
    else:
        if guess_num > num :
            print("大了")
        else:
            print("小了")
print(f"你總共猜測了{count}次")