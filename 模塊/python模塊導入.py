"""
模塊其實就是一個python文件
也可以認為是一個工具包
模塊就是一個python文件，裡面有類、函數、變量等，我們可以導入模塊後拿來用
模塊導入的語法為：
import 模塊名，但這個語法會把整個模塊的所有功能都帶過來
如果只要其中一個方法，那就如下
[from 模塊名] import [模塊 | 類 | 變量 | 函數 | *] [as 別名 ]
使用方式：
模組名.內部功能
"""

#   使用import導入time模塊使用sleep功能(函數)
# import time # 導入python內置的time模塊(time.py這個代碼文件)
# print("您好")
# time.sleep(5)  # 模組名.內部功能，通過 . 使用模塊內部的全部功能
# print("我好")


#   使用from導入time的sleep功能
# from time import sleep
# print("您好")
# sleep(5) # 上面是帶整個模塊所以用其中一個功能時要指定模塊名
# print("我好")

#   使用 * 導入time的所有功能，星號代表所有的意思
# from time import *
# # * 號表示全部的意思
# # 注意，此語法與單純import的功能一樣都是導入全部，只是寫法不一樣。此寫法跟from的一樣可以不指定模塊名使用
# print("您好")
# sleep(5)
# print("我好")

# 使用 as 給特定功能加上別名
# 就是可以把導入進來的模塊改個名字，導入進來的模塊可能名字太長不好寫，改個名字能看懂而且簡短
# import time as t
# print("您好")
# t.sleep(2)
# print("我好")

from time import sleep as sl
print("")
print("您好")
sl(2)
print("我好")

"""
總結：
1,模塊就是一個python文件，內含類、函數、變量等，可以導入進行使用。
2,如何導入模塊?
import
[from 模塊名] import [模塊 | 類 | 變量 | 函數 | *] [as 別名 ]

3,注意：
    from可以省略，直接import
    as別名可以省略
    通過 . 來確定層級關係
    模塊的導入一般寫在代碼文件的開頭
"""