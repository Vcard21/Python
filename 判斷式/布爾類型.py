"""
布爾類型的字面量:
Ture(真)
False(假)
布爾類型不僅可以自行定義，同時也可以通過計算比較運算符得到

== 判斷是否相等
!= 判斷是否不相等
> 是否大於
< 是否小於
>= 是否大於等於
<= 是否小於等於
"""

# 布爾類型字面量定義
bool_1 = True
bool_2 = False
print(f"bool_1變量的內容是:{bool_1},類型是:{type(bool_1)}")
print(f"bool_1變量的內容是:{bool_2},類型是:{type(bool_2)}")
# 比較運算符的運用
# ==,!=,>,<,>=,<=
# 演示進行內容的相等比較
num1 = 10
num2 = 10
print(f"10 == 10的結果是:{num1 == num2}")

num1 = 10
num2 = 15
print(f"10 != 15的結果是:{num1 != num2}")
# 字符串也能使用
name1 = "itcast"
name2 = "itheima"
print(f"itcast == itheima的結果是:{name1 == name2}")
# 演示>=,<=,<,>的比較運算
nmu1 = 10
num2 = 5
print(f"10>5結果是:{num1 > num2}")
print(f"10<5結果是:{num1 < num2}")

num1 =10
num2 = 11
print(f"10>=10的結果是:{num1 >= num2}")
print(f"10<=10的結果是:{num1 <= num2}")
