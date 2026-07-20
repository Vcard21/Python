"""
如果沒有使用return返回的話，實際上返回了
只是返回的是NONE這個語法
本質上其實就是返回空白
"""

# 無return語法的返回值
def say_hi():
    print("Hello World")

result = say_hi()
print(f"返回內容是{result}")
print(f'返回的內容類型是{type(result)}')

# 主動返回none的函數
def say_hi2():
    print("Hello World")
    return None
result = say_hi2()
print(f"返回內容是{result}")
print(f'返回的內容類型是{type(result)}')

# 可以用在函數無返回值的狀況
# 也可以用在if判斷上，if判斷中None等同於False
def check_age(age):
    if age >= 18:
        return "sucess"
    else:
        return None
result =check_age(16)
if not result:
    # 進入if表示result是None值，也就是False
    print("未成年不可進入")

# None可用於暫時聲明無初始內容的變量
name = None

# 通常用於函數返回值、if判斷、變量定義