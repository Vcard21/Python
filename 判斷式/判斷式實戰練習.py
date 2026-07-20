"""
數字隨機產生，範圍1~10
有三次機會猜測數字，通過三層嵌套判斷
每次猜不中，會提示大了或小了
"""
import random
num = random.randint(1,10)
guess = int(input("輸入數字吧"))
# 通過if判斷語句進行數字的猜測
print("猜數字時間")
if guess ==num:
    print("恭喜，第一步就猜中了")
else:
    if guess > num:
        print("你猜測的數字大了")
    else:
        print("你猜的小了")

    guess = int(input("再輸入一次吧"))

    if guess == num:
        print("恭喜第二次猜中了")
    else:
        if guess > num:
            print("你猜測的數字大了")
        else:
            print("你猜的小了")

        guess = int(input("最後再輸入一次吧"))

        if guess == num:
            print("第三次猜中了")
        else:
            print("三次機會用完了，沒有猜中")