"""
字典的定義：
通過【字】找到對應的涵義
Key:Value
字典的定義同樣使用{}
不過存儲的元素是一個個的鍵值對，如以下：
{key:value}
"""
# 定義字典
my_dict1 = {"王力宏":99,"林俊傑":88,"周杰倫":100}

# 定義空字典
my_dict2 = {}
my_dict3 = dict()
print(type(my_dict1),my_dict1)
print(type(my_dict2),my_dict2)
print(type(my_dict3),my_dict3)

# 定義重複key的字典
my_dict4 = {"王力宏":99,"林俊傑":88,"周杰倫":100,"王力宏":99,}
print(f"重複key的字典內容是:{my_dict4}")
# 即使能輸出，新的也會覆蓋老的，不支持重複！！！！！！

# 字典的Value獲取(語法：dict[])
my_dict1 = {"王力宏":99,"林俊傑":88,"周杰倫":100}
score = my_dict1["王力宏"]
print(f"王力宏的考試分數是{score}")

# 字典的嵌套:
# 字典的key和value可以是任意數據類型(key不可為字典，嵌套時使用在value)
stu_score_dict = {
    "王力宏":{
        "語文":77,
        "數學":66,
        "英文":33,
    },
    "周杰倫":{
        "語文":88,
        "數學":86,
        "英文":55,
    },
    "林俊傑":{
        "語文":99,
        "數學":96,
        "英文":66,
    }
}
print(f"學生的考試信系是:{stu_score_dict}")

# 從嵌套字典中獲取數據(語法:dict[][].....[])
# 看一下周杰倫的語文訊息
score_cn = stu_score_dict["周杰倫"]["語文"]
print(f"周杰倫的語文分數是{score_cn}")
score_en = stu_score_dict["林俊傑"]["英文"]
print(f"林俊傑的英文分數是{score_en}")

"""
總結：
1,字典可以提供基於KEY檢索VALUE的場景實現
就像查字典

2,字典的定義語法
{key:value}又稱鍵值對
空字典兩種定義方法
my_dict = {}
my_dict = dict()

3,鍵值對的key和value可以是任意類型(key不可為字典)
字典內key不允許重複,重複添加等同於覆蓋原有數據
字典不可用下標索引,而是通過Key檢索value
"""