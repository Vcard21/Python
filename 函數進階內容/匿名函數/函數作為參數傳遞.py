"""
在前面的函數學習中，函數一直都是接受數據做為參數傳入
數字;字符串;字典;列表;元組等
其實，我們學習的函數本身，也可以做為參數傳入另一個函數內

def test_func(compute):
    result = compute(1,2)
    print(result)
def compute(x,y):
    return x+y

test_func(compute)

第一個def本質上只做數據內容的提供，而第二個def才提供實際的執行邏輯
這是一種「計算邏輯」的傳遞，而非數據的傳遞
就像上述代碼那樣，不僅僅是相加、相減、想除、等任何邏輯都可以自行定義並作為函數傳入。
"""
# 定義一個函數，接收令一個函數作為傳入參數
def test_func(compute):
    result = compute(1,2) # 在這邊時才可以確定這邊用的是函數，因為這是函數的調用方式
    print(type(compute))
    print(result)
# 定義一個函數，準備做為參數傳入另一個函數
def compute(x,y):
    return x+y
# 調用，並傳入參數
test_func(compute)

"""
總結：
1,函數本身是可以做為參數，傳入另一個函數中進行使用。
2,將函數傳入的作用在於：傳入計算邏輯，而非傳入數據
"""