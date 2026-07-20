"""
json 是一種輕量級的數據交互格式。可以按json指定的格式去組織和封裝數據
json本質上是一個帶有特定格式的字符串

主要功能：json就是一種在各個編程語言中流通的數據格式，負責不同編程語言中的數據傳遞
和交互，類似於:
國際通用語文英語
中國56個民族不同地區的通用語言-普通話

json就是為了因應各種程式語言存儲數據的容器不同問題而使用的交互格式，
在python中有字典dict這樣的數據類型，而其他語言可能沒有對應的字典
為了讓不同的語言都能夠相互通用的互相傳遞數據，json就是一種非常良好的中轉數據格式

"""
# 導入json模塊
import json

# dumps = 轉出
# 準備列表，列表內每一個元素都是字典，將其轉換json
data = [{"name":"張大山","age":11},{"name":"王大槌","age":13},{"name":"趙小虎","age":16}]
json_str = json.dumps(data,ensure_ascii=False) # ensure_ascii = False 這段是為了把內容用原文打出來
print(type(json_str))
print(json_str)

# 準備字典，將字典轉換為json
d ={"name":"周杰倫","addr:":"台北"}
json_str = json.dumps(d,ensure_ascii=False)
print(type(json_str))
print(json_str)

# loads = 轉入
# 將json字符串轉換為python數據類型[{k:v,k:v},{k:v,k:v}]
s = '[{"name":"張大山","age":11},{"name":"王大槌","age":13},{"name":"趙小虎","age":16}]'
l = json.loads(s)
print(type(l))
print(l)

# 將json字符串轉換為python數據類型{k:v,k:v}
s ='{"name":"周杰倫","addr:":"台北"}'
d = json.loads(s)
print(type(d))
print(d)

"""
 python使用json有優勢，python文法能夠直接轉換成json格式
 json就是字符串，json無非就是一個單獨的字典或一個內部元素都是字典的列表
 所以json可以直接和python的字典或列表進行無縫轉換
 
 json格式數據轉化:
 通過json.dumps(data)方法把python數據轉化為了json數據
    data = json.dumps(data)
    如果有中文可以戴上:ensure_ascii = False參數來確保中文正常轉換
 通過json.loads(data)方法把json數據轉化為了python列表或字典。
"""