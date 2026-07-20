""""
continue 關鍵字用於：中斷本次循環，直接進入下一次循環
break 關鍵字直接就結束循環
for while都可以用
只會對當下的縮進中產生效果
continue可以叫做臨時中斷
break可以叫做永久中斷
"""

# for i in range(1,6):
#     print("語句1")
#     continue
#     print("語句2")
"""!!continue 是讓本次循環結束，直接進入"下一個循環"而不是繼續接下來的動作!!"""

""" for 嵌套應用"""
# for i in range(1,2):
#     print("語句1")
#     for j in range(1,7):
#         print("語句2")
#         continue
#         print("語句3")
#     print("語句4")

"""break 執行範例"""
# for i in range(1,101):
#     print("語句1")
#     break
#     print("語句2")
# print("語句3")

"""break 嵌套案例"""
for i in range(1,6):
    print("語句1")
    for j in range(1,6):
        print("語句2")
        break
        print("語句3")
    print("語句4")