"""
數據容器可以是任意類型的數據，如:字串、數字、布爾值等
數據容器根據特點的不同，如：
是否支持重複元素
是否可以修改
是否有序等等
分為五類，分別是:
列表(list)、元祖(tuple)、字符串(str)、集合(set)、字典(dict)
雖然以上各有特點，但都滿足可以容納多個元素的特性。
"""

# 定義一個列表list
my_list = ["itheima","itcast","python"]
print(my_list)
print(type(my_list))

my_list1 = ["itheima",666,True]
print(my_list1)
print(type(my_list1))

# 定義一個嵌套的list
my_list2 = [[1,2,3],[4,5,6]]
print(my_list2)
print(type(my_list2))

#