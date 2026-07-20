"""
list[0,1,2]
第一個數值是0
也可以倒退來
list[-3,-2,-1]
負值也可以用
如果是嵌套list的話該怎麼拿裡面的元素呢?
list[[1,2,3],[a,b,c]]
如果我要2
那就是list[1][1]
c的話就是
list[2][2]
"""
my_list = ["tom","lily","rose"]
# 下標索引，從前向後，從0開始每次+1
print(my_list[0])
print(my_list[1])
print(my_list[2])
# 反向的下標索引取出，從後向前，從-1開始每次-1
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

# 嵌套列表
my_list1=[[1,2,3],[4,5,6]]
print(my_list[1][1])