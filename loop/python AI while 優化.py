day = 1
# 用字典存放資料，結構更清晰
flowers = {"玫瑰": 0, "向日葵": 0}

while day <= 100:
    if day <= 50:
        flowers["玫瑰"] += 10
    else:
        flowers["向日葵"] += 10
    day += 1

print(f"堅持到第{day - 1}天")
print(f"清單如下：{flowers}")
# 如果嫌有中括號跟冒號太難看也可以像下面這樣寫
print(f"玫瑰總數:{flowers['玫瑰']}支")
print(f"向日葵總數:{flowers['向日葵']}支")