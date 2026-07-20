"""
list 是可以被修改的對吧
那元組tuple就是不能被修改的唯讀屬性
使用目的就是希望使用這個數據內容，但是不希望這個東西被修改
元組的定義：定義元組使用小括號，且使用逗號隔開數據，數據可以是不同的數據類型
ex:
(元素,元素,......,元素)
變量 = (元素,元素,......,元素)
!  空元組的寫法  !
變量 = ()
變量 = tuple()
"""

# 定義元組
t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print(f"t1的類型是{type(t1)}")
print(f"t1的類型是{type(t2)}")

# 定義單個元素的元組
# t4 = ("hello") 這樣寫不是元組!!!
# 因為單個元素的話需要在後面再加一個逗號ide才能辨別，所以應該如下
t4 = ("hello",)
print(f"t4的類型是:{type(t4)}")

# 元組的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的類型是{type(t5)}")

# 下標索引去取出內容
# 跟list一樣而不是小括號
num = t5[1][2]
print(f"從嵌套元組中取出來的是{num}")

# 元組index() 查找下標序號
t6 = ("傳智教育","黑馬程序員","python")
index = t6.index("黑馬程序員")
print(f"index查找後的下標序號結果是{index}")

# 元組count() 計算單一內容數量
t7 = ("傳智教育","黑馬程序員","黑馬程序員","python")
num = t7.count("黑馬程序員")
print(f"統計黑馬程序員的數量有{num}")

# 元組len() 計算所有資料
t8 = ("傳智教育","黑馬程序員","黑馬程序員","python")
num = len(t8)
print(f"統計總內容數量有{num}")

# 元組的遍歷while
index = 0
while index < len(t8):
    print(f"元組的元素有{t8[index]}")
    index += 1

# 元組的遍歷for
index1 = 0
for element in range(len(t8)):
    print(f"2元組的元素有{t8[index1]}")

"""
元組的注意事項(例外)
元組不可被修改，但是元組嵌套中如果有list呢?
那裡面的list就可以被修改
釋例如下：
"""
# t8[0] = "itcast"
t9 = (1,2,["itheima","itcast"])
print(f"t9的內容是:{t9}")
t9[2][0] = "黑馬程序員"
t9[2][1] = "傳智教育"
print(f"t9修改的內容是{t9}")

"""
練習案例
定義一個元組，內容是("周杰倫",11,["football","music"])，紀錄的是一個學生的資訊，(姓名,年齡,愛好)
請通過元組的功能(方法),對其進行
1,查詢其年齡所在的下標位置
2,查詢學生的姓名
3,刪除學生愛好中的football
4,增加愛好:coding到愛好list內
"""
# 查詢下標位置index
t_task = ("周杰倫",11,["football","music"])
age =t_task.index(11)
print(f"年齡的下標索引是{t_task[age]}")

# 姓名查詢
# 錯誤示範，這邊應該要用[]
# name = t_task(0)
name = t_task[0]
print(f"姓名是{name}")

# 刪除愛好中的football
del t_task[2][0]
print(f"刪除football後的結果是{t_task}")

# 增加coding至list
t_task[2].append("coding")
print(f"增加coding後的結果是{t_task}")