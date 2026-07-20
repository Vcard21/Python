"""
就是在函數裡面調用了另一個函數
"""

def func_b():
    print("2")
def func_a():
    print("1")
    # 嵌套調用func_b
    func_b()
    print("3")
func_a()
# 要執行完調用函數之後才會繼續執行外層