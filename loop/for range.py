"""
for可以說是遍歷循環、序列類型

range(num1,num2)
獲得一個從num1開始，num2結束的數字序列(不含num2本身)
例如，range(5,10)取得的數據是:{5,6,7,8,9}(不含10)

range(num1,num2,step)
step代表間隔
range(5,10,2)
輸出為{5,7,9}
"""
# for x in range(10):
#     print(x)

# 語法2 range(num1,num2)
# for y in range(5,10):
#     print(y)
# # 語法3 range(num1,num2,step)
# for z in range(5,10,2):
#     print(z)
#
# for x in range(10):
#     print("送玫瑰花")
#
"""
小練習。
定義一個數字變量num，內容隨意
並使用range()語句,獲取從1到num的序列，使用for循環遍歷他
在遍歷的過程中，統計有多少偶數出現。
"""
count = 0
for num in range(1,100):
    if num % 2 == 0:
        count +=1
print(f"1到100(不含100本身範圍內，共有:\t{count}個偶數")
# \t就是一次tab縮進。