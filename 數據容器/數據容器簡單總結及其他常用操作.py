"""
    分類：

支持下標索引的有：列表、元組、字符串 - 序列類型
不支持的有：集合、字典　- 非序列類型

    是否支持重複元素：
支持：列表、元組、字符串 - 序列類型
不支持：集合、字典 - 非序列類型

    是否可以修改：
支持：列表、集合、字典
不支持：元組、字符串

    基於各類數據容器的特點，應用場景如下：
1,列表：一批數據,可修改,可重複的存儲
2,元組：一批數據,不可修改,可重複的存儲
3,字符串：一串字符串的存儲
4,集合：一批數據,去重的存儲
5,字典：一批數據,可用key檢索value的存儲

    遍歷：
五大內容都支持for循環
列表、元組、字符串支持while循環，集合、字典不支持(無法下標索引)

儘管遍歷的形式各有不同，但是，!它們都支持遍歷操作!


    除了遍歷共通以外，數據容器可以通用非常多的功能方法，例如：
len(容器) 統計容器的元素
max(容器) 統計容器的最大元素
min(容器) 統計容器的最小元素
"""
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdefg"
my_set = {1,2,3,4,5}
my_dict = {"key1":1, "key2":2, "key3":3, "key4":4}

# len
print("len內容\n",len(my_list))
print(len(my_tuple))
print(len(my_str))
print(len(my_set))
print(len(my_dict))

# max
print("max內容\n",max(my_list))
print(max(my_tuple))
print(max(my_str))
print(max(my_set))
print(max(my_dict))

# min
print("min內容\n",min(my_list))
print(min(my_tuple))
print(min(my_str))
print(min(my_set))
print(min(my_dict))

"""
除了上述的統計功能以外
還可以使用容器的通用轉換功能
使用list(容器)、tuple(容器)、str(容器)、set(容器)函數將容器更改為指定數據容器
"""
print(f"列表轉列表的結果是:{list(my_list)}")
print(f"元組轉列表的結果是:{list(my_tuple)}")
print(f"字符串轉列表的結果是:{list(my_str)}")
print(f"集合轉列表的結果是:{list(my_set)}")
print(f"集合轉列表的結果是:{list(my_dict)}")
# 字符串跟字典轉列表的時候，字符串會分開來、字典會拋棄value只剩key



print(f"列表轉元組的結果是:{tuple(my_list)}")
print(f"元組轉元組的結果是:{tuple(my_tuple)}")
print(f"字符串轉元組的結果是:{tuple(my_str)}")
print(f"集合轉元組的結果是:{tuple(my_set)}")
print(f"集合轉元組的結果是:{tuple(my_dict)}")
# 字符串跟字典轉元組的時候，字符串會分開來、字典會拋棄value只剩key

print(f"列表轉字符串的結果是:{str(my_list)}")
print(f"元組轉字符串的結果是:{str(my_tuple)}")
print(f"字符串轉字符串的結果是:{str(my_str)}")
print(f"集合轉字符串的結果是:{str(my_set)}")
print(f"集合轉字符串的結果是:{str(my_dict)}")
# 字符串轉列表的實際輸出內容長這樣"[1, 2, 3, 4, 5]"，同理其他的也是，所以字典不會丟失內容

print(f"列表轉集合的結果是:{set(my_list)}")
print(f"元組轉集合的結果是:{set(my_tuple)}")
print(f"字符串轉集合的結果是:{set(my_str)}")
print(f"集合轉集合的結果是:{set(my_set)}")
print(f"集合轉集合的結果是:{set(my_dict)}")
# 字符串的輸出內容會亂掉，因為集合的特性是無序且去重的。字典同樣也是會丟失value

"""
通用排序功能
sorted(容器,[reverse = Ture])
將指定容器進行排序
"""
my_list = [3,1,2,5,4]
my_tuple = (3,1,2,5,4)
my_str = "bacefga"
my_set = {3,1,2,5,4}
my_dict = {"key3":1, "key1":2, "key2":3, "key5":4, "key4":5}
print(f"列表對象的排序結果:{sorted(my_list)}")
print(f"元組對象的排序結果:{sorted(my_tuple)}")
print(f"字符串對象的排序結果:{sorted(my_str)}")
print(f"集合對象的排序結果:{sorted(my_set)}")
print(f"字典對象的排序結果:{sorted(my_dict)}")
# sorted排序後順序會變成有序的了，需要注意的是排完序後會變成列表，字典還是會丟失value

# 那反向排序呢? 答案是語法：數據容器.reverse = True，reverse代表反向的意思
print(f"列表對象的排序結果:{sorted(my_list,reverse = True)}")
print(f"元組對象的排序結果:{sorted(my_tuple,reverse = True)}")
print(f"字符串對象的排序結果:{sorted(my_str,reverse = True)}")
print(f"集合對象的排序結果:{sorted(my_set,reverse = True)}")
print(f"字典對象的排序結果:{sorted(my_dict,reverse = True)}")