"""
字符串是字符的容器,一個字符串可以存放任意數量的字符。
如:"itheima"
實際上就是
["i","t","h","e","i","m","a"]
如同list跟tuple一樣使用1 or -1(下標索引)來提取內容
"""
my_str = "itheima and itcast"
value = my_str[2]
value2 = my_str[-16]
print(f"從字符串mystr中取下標為2的元素及-16的元素為{value},{value2}")
# my_str[2] = "H"
# 同tuple一樣，字符串str是不可修改的容器


# str index
index =my_str.index("and")
print(f"查找下標的結果是{index}")

# 字符串的替換(語法：字符串.replace(字符串1,字符串2)
# 將字符串內的全部:字符串1，替換為字符串2
# !注意!，嚴格來說不是修改字符串本身，而是得到一個新字符串
new_my_str =my_str.replace("it","程序")
print(f"從{my_str}進行替換後得到{new_my_str}")

# 字符串的分割(語法：字符串.split(分隔符字符串))
# 功能是按照定的分隔符字符串，將字符串劃分為多個字符串，並存入列表對象中
# 注意!，字符串本身不變，而是得到了一個列表list
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"將字符串分割後的結果是{my_str_list}，類型是{type(my_str_list)}")

# 字符串的規整操作，去前後空格(語法：字符串.strip())
# 字符串.strip(字符串)，代表strip有默認參數
my_str = "  itheima and itcast  "
new_my_str = my_str.strip() # 不傳入參數就是去除首尾空格
print(f"字符串{my_str}被strip後的結果是{new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(f"去除12前是{my_str}，去除後的結果是{new_my_str}")
# 結果會把12跟21都去除，為什麼?因為就像前述被拆分一樣，他是分成一個一個，所以會去除掉1跟2
# 特別注意，只有strip會分開，其他的使用時還是連在一起


# 統計某個內容出現的次數，(語法：字符串.count)
my_str = "12itheima and itcast21"
count = my_str.count("it")
print(f"it出現的次數{count}")

# 統計字符串的總長度(語法：len())
num = len(my_str)
print(f"字符串{my_str}的長度是{num}")

"""
總結:
字符串下標
index
replace(1字符串,2字符串)字符串的替換
split(字符串)字符串的分割
strip()去前後空格
strip(字符串)去掉指定參數
count(字符串)計算單一長度
len(字符串)計算總體長度

特性:
只可以存儲字符串
長度任意
支持下標索引
允許重複字符串存在
不可以修改
支持for,while
"""

"""
練習:
"itheima itcast boxuegu"
1.統計總共多少it
2.將空格替換為:"|"
3.按照"|"進行字符串分隔，得到列表
"""
task1 = "itheima itcast boxuegu"
count = task1.count("it")
print(count)
task_part2 = task1.replace(" ","|")
print(task_part2)
# task_part3 = task1.split("|")，錯誤示範，因為他是說要再用新的"|"str再做下一個，而不是直接用原本的
task_part3 = task_part2.split("|")
print(task_part3)
