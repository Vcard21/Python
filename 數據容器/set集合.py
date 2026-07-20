"""
集合:
集合最主要的特點就是不支持重複的元素，自帶去重功能，並且內容無序
列表使用[]
tupl使用()
字符串使用""
集合使用{}

集合是無序的，所以集合不支持下標索引訪問
但是和列表一樣是允許修改的
"""


# 定義集合
my_set = {"傳智教育","黑馬程序員","itheima","傳智教育","黑馬程序員","itheima","傳智教育","黑馬程序員","itheima"}
my_set_empty = set()
print(f"my_se的內容是{my_set}，類型是{type(my_set)}") #不允許重複的，順序無法保證
print(f"my_se的內容是{my_set_empty}，類型是{type(my_set_empty)}")

# 添加新元素(語法：set.add())
my_set.add("python")
my_set.add("傳智教育") #即使增加也只會有一個，因為去重
print(f"添加元素後的結果是{my_set}")

# 移除元素(語法：set.remove())
my_set.remove("黑馬程序員")
print(f"my_set移除元素後的結果是{my_set}")

# 隨機取出一個元素(語法：set.pop())
my_set = {"傳智教育","黑馬程序員","itheima"}
element = my_set.pop()
print(f"集合被取出元素是{element}，取出後還有{my_set}")

# 清空集合(語法：set.clear())
my_set.clear()
print(f"集合被清空了，結果是{my_set}")

# 取兩個集合的差集
# 語法：集合1.difference(集合2)，功能：取出集合1和集合2的差集(集合1有而集合2沒有的)
# 結果：得到一個新集合，集合1和集合2不變
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2) #意思就是找差集1有，但差集2沒有的元素
print(f"取差集的結果是{set3}")

# 消除差集
# 語法：集合1.difference_update(集合2)
# 功能：對比集合1和集合2，在集合1內，刪除和集合2相同的元素。
# 結果：集合1被修改，集合2不變
set4 = {1,2,3}
set5 = {1,3,5}
set4.difference_update(set5) #修改4的結果而不是得到一個新集合
print(f"消除差集後的集合4結果是{set4}，而未被消除的集合5則是{set5}")
# 其含義就是消除兩個集合中相同的元素，並且更新到選擇的第一個集合

# 2個集合合併
# 語法：集合1.union(集合2)
# 功能：將集合1和集合2組合成新集合
# 結果：得到新集合，集合1和集合2不變
set6 ={1,2,3,4,5,6}
set7 = {1,3,5,7,8,9}
set8 = set6.union(set7)
print(f"2集合合併結果為{set8}")
print(f"合併後集合1{set6},集合2{set7}")
# 兩個集合合1時並不會消除原本的，而是得到一個新集合

# 統計集合元素數量 len()
set9 ={1,2,3,4,5,1,2,3,4,5} #就算重複，也會去重完後再輸出
num = len(set9)
print(f"集合總數量{num}")

# 集合的遍歷
# 集合不支持下標索引所以不能用while循環
# 但能夠用for循環
set1 = {1,2,3,4,5,6}
for element in set1:
    print(f"集合的元素有{element}")

"""
總結:
add增加一個元素
remove去除一個元素
pop隨機取出一個元素
clear清空集合
difference找集合1有集合2沒有的
difference_update找集合1跟集合2都有的並刪除後更新至集合1
union將兩個集合合起來產生一個新集合
len統計元素數量

特點:
可以容納多個數據
可以容納不同類型數據
不支持下標索引(無序存儲)
不允續重複元素存在
可以修改
只支持for循環
"""

"""
練習：
my_list = {"黑馬程序員","傳智教育","黑馬程序員","傳智教育","itheima","itcast","itheima","itcast","best"]

請定義一個空集合
通過for循環遍歷
在for循環中將列表的元素添加至集合
最終得到元素去重後的集合對象並打印出來

"""
my_list = {"黑馬程序員","傳智教育","黑馬程序員","傳智教育","itheima","itcast","itheima","itcast","best"}
taskset = set()
for emlement in my_list:
    taskset.add(emlement)
print(taskset)