"""
函數的定義中
def關鍵字，可以定義帶有名稱的函數
lambda關鍵字，可以定義匿名函數(無名稱)
有名稱的函數，可以基於名稱重複使用
無名稱的匿名函數，只可臨時使用一次

語法：
lambda 傳入參數:函數體(一行代碼)
1,lambda是關鍵字，表示定義匿名函數
2,穿入參數表示匿名函數的形式參數，如x,y表示接收2個形式參數
3,函數體，就是函數的執行邏輯，!要注意，只能寫一行，無法寫多行代碼!
"""
def test_func(compute):
    result = compute(1,2) # 在這邊時才可以確定這邊用的是函數，因為這是函數的調用方式
    print(type(compute))
    print(result)
def compute(x,y):
    return x+y
test_func(compute)
# 上面是原本將函數進行參數使用的示範
# 如果使用lambda關鍵字的話會變成如下

def test_func(compute):
    result = compute(1,2) # 在這邊時才可以確定這邊用的是函數，因為這是函數的調用方式
    print(type(compute))
    print(result)
# def compute(x,y):
#     return x+y
test_func(lambda x,y:x+y) # 語法：lambda 傳入參數(x,y):函數邏輯(x+y)
# x跟y就跟示範的傳參一樣
# lambda不用寫return語句，lambda語法默認return
# lambda無法使用多行代碼

"""
總結：
1,匿名函數使用lambda關鍵字進行定義
2,定義語法：
lambda 傳入參數:函數邏輯(一行代碼)
3,注意事項：
    1,匿名函數用於臨時建構一個函數，只用一次的場景
    2,匿名函數的定義中，函數體只能寫一行代碼，如果函數體要寫多行代碼，那就不可用lambda匿名函數，應使用def定義
      帶名函數
4,應用場景：
    在大數據分析等使用頻率非常高
"""