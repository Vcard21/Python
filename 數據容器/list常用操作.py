"""
列表除了可以:
1.定義
2.使用下標索引獲得直
然而此外列表也提供以下功能:
1.插入元素
2.刪除元素
3.清空列表
4.修改元素
5.統計元素個數
等等功能，這些我們稱之為:列表的方法
"""
# 而函數如果定義為class(類)的成員，那麼函數會稱之為方法
# class Student:
#     def add(self,x,y):
#         return x + y
# 方法和函數功能一樣，有傳入參數，有返回值，只是方法的使用格式不同
# 函數的使用為:num = add(1,2)
# 方法的使用為:student = Student()
#            num = student.add(1,2)



# 定義基礎列表
mylist = ["itcast","itheima","python"]
# 1.1查找某元素在列表內的下標索引(語法：list.index)
index =  mylist.index("itheima")
print(f"itheima在列表中的下標索引是{index}")
# 1.2如果被查找的元素不存在，會報錯
# index =  mylist.index("hello")
# print(f"itheima在列表中的下標索引是{index}")


# 2修改下標索引的值(語法：列表[下標]=值)
mylist[0] = "中文傳智教育"
print(f"列表被修改元素值後，結果是{mylist[0]}")


# 3元素的插入(語法：列表.insert(下標,元素))，如果我要在0.1中間插入，那是不是新的元素就會變成1呢，所以下標要填1
mylist.insert(1,"best")
print(f"元素插入後結果是{mylist[1]}")


# 4追加元素，將指定元素追加至列表的尾部(語法：列表.append(元素))
mylist.append("黑馬程序員")
print(f"列表在追加元素後結果是:{mylist}")


# 5追加元素2，如果想加入一批元素的話(語法：列表.extend(其他數據容器))，這個語法會將其他數據內容取出，依次加入
mylist2= [1,2,3]
mylist.extend(mylist2)
print(f"列表在追加了一個新的列表後結果是{mylist}")


# 6元素的刪除，兩種方式(語法1：del列表[下標] ,語法2：列表.pop(下標)
mylist = ["itcast","itheima","python"]
del mylist[2]
print(f"列表刪除元素後結果是{mylist}")
# pop方法還可以用定義去接收他被刪除的元素，pop本質上來說是把選擇的值給取出來然後返回出去
mylist = ["itcast","itheima","python"]
element = mylist.pop(2)
print(f"pop的結果是{mylist}，取出的元素是{element}")


# 7刪除從前到後，第一個找到的元素，代表即使有同樣數值也只會被刪除第一個(語法：列表.remove(元素)
mylist = ["itcast","itheima","python","python"]
mylist.remove("python")
print(f"通過remove python後的結果是{mylist}") # 結果是itcasr , itheima , python


# 8清空整個列表(語法：列表.clear())
mylist.clear()
print(f"列表被清空了，結果是{mylist}")


# 9統計某一元素的數量(語法：列表.count())
mylist = ["itcast","itheima","python","python"]
count = mylist.count("python")
print(f"python的值總共有{count}")


# 10統計總共有多少個元素(語法：len(列表))
mylist = ["itcast","itheima","python","python"]
count = len(mylist)
print(f"列表的元素數量總共{count}")


"""
小練習
有一個列表，內容是：[21,25,21,23,22,20]，紀錄的是一批學生的年齡
請通過列表的功能(方法)對其進行
1.定義這個列表，並用變量接收他
2.追加一個數字31到列表尾部
3.追加一個新列表[29,33,30]，到列表尾部
4.取出第一個元素(應為21)
5.取出最後一個元素(應是30)
6.查找元素31，在列表中的位置
"""
tasklist = [21,25,21,23,22,20]
tasklist.append(31)
print(tasklist)
tasklist2 = [29,33,30]
tasklist.extend(tasklist2)
print(tasklist)
first_num = tasklist.pop(0)
print(first_num)
# last_num = tasklist.pop(8)
# 使用最後一個可以使用負數還記得嗎?最後一個是-1
# 所以這邊是：
last_num = tasklist.pop(-1)
print(last_num)
index =tasklist.index(31)
print(index)

