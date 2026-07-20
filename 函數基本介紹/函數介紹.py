"""
函數的特點是
1.提前寫好
2.可以重複使用
3.實現一特定功能的代碼
"""

str1 = "itheima"
str2 = "itcast"
str3 = "python"

# 定義一個記數的變量
# count = 0
# for i in str1:
#     count = count + 1
# print(f"字符串{str1}的長度是:{count}")
#
# count = 0
# for i in str2:
#     count = count + 1
# print(f"字符串{str2}的長度是:{count}")
#
# count = 0
# for i in str3:
#     count = count + 1
# print(f"字符串{str3}的長度是:{count}")

# 可以使用函數來優化重複代碼的過程

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的長度是{count}")

my_len(str1)
my_len(str2)
my_len(str3)