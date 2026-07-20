"""
局部變量是定義在函數體內部的變量，即只在函數體內部生效
局部變量的定義是在函數體內部，臨時保存數據，調用完成之後立刻銷毀變量。
本章重點之一 golbal關鍵字
"""

# 局部變量演示
def testA():
    num = 100
    print(num)
testA()
# 出了函數體，局部變量就無法使用了。
# print(num)

# 全局變量是在函數體內外都能生效的變量，只需要定義在外部就可以一直用

num = 200
def test_a():
    print(f"test_a = {num}")
def test_b():
    print(f"test_b = {num}")
test_a()
test_b()
print(num)

# 在函數內修改全局變量
num = 200
def test_a():
    print(f"test_a = {num}")
def test_b():
    num = 500  # 局部變量
    print(f"test_b = {num}")
test_a()
test_b()
print(num)
# 使用golbal關鍵字就可以把函數內的數值改成內外一致了。
num = 200
def test_a():
    print(f"test_a = {num}")
def test_b():
    global num #設置內部局部變量為全局變量。
    num = 500  # 局部變量
    print(f"test_b = {num}")
test_a()
test_b()
print(num)