"""
所謂返回值，就是程序中函數完成事情後，最後給調用者的結果
def 函數(參數):
    函數體
    return 返回值
變量 = 函數(參數)
"""
def add(a,b):
    result = a + b
    # 通過返回值將相加的結果返回給調用者
    return result
    # return 也代表函數的結束，事情都要在return前結束。
r = add(5,6)
# 函數的返回值可以通過變量去接收。
print(r)