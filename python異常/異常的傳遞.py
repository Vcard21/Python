def func1():
    print("func1開始執行")
    num = 1/0
    print(f"func1結束執行")
# 定義一個異常的方法，調用方法
def func2():
    print("func2開始執行")
    func1()
    print("func2結束執行")
# 定義一個方法，調用方法

def main():
    try:
        func2()
    except Exception as e:
        print(f"出現異常了，內容為:{e}")
main()
# 只要程式帶有層級關係，在最尾部、最高級的層級時就可以直接使用try捕獲。