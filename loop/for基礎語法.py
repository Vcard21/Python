"""
while的循環可以自定義
for循環是對一批內容逐個進行處理，總共5的話就從1開始2.3.4.5，逐個處理，直到5結束
簡單比喻就是對一個代辦事項一個一個進行處理，直到沒有代辦事項。\

程式公式
for 【臨時變量】 in 【待處理數據集】:
每一次循環就將當前【待處理數據集】的數據賦值到【臨時變量】中

EX:
name = "itheima"
for x in name:
    print(x)
運行結果是:
i
t
h
e
i
m
a
"""
name = "itheima"
for x in name:
    print(x)
# 注意點是for循環是無法定義條件的，所以理論上for循環是無法無限循環的
# 循環內的語句一樣需要縮進。

# 練習題：定義字符串變量為name,內容為:"itheima is a brand of itcast"
# 通過for循環，遍歷此字符串，統計有多少個英文字母a。
# 提示:記數可以在循環外定義一個整數類型用來做累加，判斷是否為a可以使用if
example = "itheima is a brand of itcast"
count = 0
for j in example:
    if j == "a":
        count += 1
print(f"總共有{count}個a")
