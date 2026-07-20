""""""
from itertools import takewhile

# 新增元素(字典[key] = value)
my_dict = {"周杰倫":99,"林俊傑":88,"張學友":77}
my_dict["張信哲"] = 55
print(my_dict)

# 更新元素(字典[key] = value)
my_dict = {"周杰倫":99,"林俊傑":88,"張學友":77}
my_dict["周杰倫"] = 33
print(my_dict)
# 新增跟更新是一樣的，差別就在如果原本沒有那就是新增，如果有那就是更新


# 刪除元素(字典.pop(key))
my_dict = {"周杰倫":99,"林俊傑":88,"張學友":77}
score = my_dict.pop("周杰倫")
print(f"刪除後的結果是 ={my_dict}，分數是{score}")

# 清空元素(字典.clear())
my_dict.clear()
print(my_dict)

# 獲取全部的key(字典.keys())
my_dict = {"周杰倫":99,"林俊傑":88,"張學友":77}
keys =  my_dict.keys()
print(keys)
# 方式1 遍歷字典
for key in keys:
    print(f"字典的keys是{key}")
    print(f"字典的value是:{my_dict[key]}")
# 方式2 直接對字典進行for循環，每一次循環都是直接得到key
for key in my_dict:
    print(f"2字典的keys是{key}")
    print(f"2字典的value是:{my_dict[key]}")

# 統計字典內的元素數量 len()
num = len(my_dict)
print(f"字典統計內容數量為:{num}")

"""
總結：
字典[key] 獲取指定key對應的值
字典[key] = value 添加或更新值
字典.pop(key) 取出key對應的value並在字典內刪除此key的鍵值對
字典.clear() 清空字典
字典.keys() 獲取字典的全部key,可用於for循環遍歷字典
len(字典) 計算字典內的元素數量

特點：
1,可以容納多個數據
2,可以容納不同類型的數據
3,每一份數據是key value鍵值對
4,可以通過key獲取到value ,key不可重複(重複會覆蓋)
5,不支持下標索引
6,可以修改
7,支持for循環,不支持while循環(因為不支持下標索引)

操作注意：
新增和更新元素的語法一致，如果key不存在即新增，key存在為更新(key不可重複)
"""

"""
練習：

"""
task_dict = {
    "王力宏":{
        "部門:":"科技部","工資":3000,"級別":1
    },
    "周杰倫":{
        "部門":"市場部","工資":5000,"級別":2
    },
    "林俊傑":{
        "部門":"市場部","工資":7000,"級別":3
    },
    "張學友":{
        "部門":"科技部","工資":4000,"級別":2
    },
    "劉德華":{
        "部門":"市場部","工資":6000,"級別":2
    }
}
for name in task_dict:
    if task_dict[name]["級別"] == 1:
        # 獲取員工的信息字典
        employee_info = task_dict[name]
# 修改員工的信息
        employee_info["級別"] = 2
        employee_info["工資"] +=  1000
# 將員工的信息更新至task_dict
        task_dict[name] = employee_info
print(f"對員工進行升職加薪後的結果是{task_dict}")