"""

定義如下的函數：
1.查詢餘額函數
2.存款函數
3.取款函數
4.主菜單函數

req：
1.程序啟動後要求輸入客戶姓名
2.查詢餘額、存款、取款後都會返回主菜單
3.存款、取款後都顯示一下當前餘額
4.只有客戶選擇退出或者說輸入錯誤時才會退出，否則將會一直運行
"""
money = 5000000
name = None
# 定義一個全局變量：money ,用來記錄銀行卡餘額(默認5000000)
# 定義一個全局變量：name ,用來記錄客戶姓名(啟動程序時輸入)，可以先用none卡位
name = input("請輸入你的姓名")
# 要求客戶輸入姓名


# 定義查詢函數
def query(show_header):
    if show_header: # 為什麼需要if呢?因為要調用這個函數，但不想要印出查詢餘額才用False把他規避掉，
        print("_____查詢餘額_____")
    print(f"{name}，您好,你的餘額剩餘,{money}元")
# 定義存款函數
def saveing(num):
    global money
    money += num
    print(f"{name}，您好,您存款{num}元成功")

    # 調用query函數查詢餘額
    query(False)

def get_money(num):
    global money
    money -= num
    print("_____取款_____")
    print(f"{name},您好,您取款{num}元成功")
# 定義取款函數

def main():
    print("_____主菜單_____")
    print(f"{name},您好,歡迎來到黑馬銀行atm，請選擇操作")
    print("查詢餘額輸入\t{1}")
    print("選擇存款輸入\t{2}")
    print("選擇取款輸入\t{3}")
    print("選擇退出輸入\t{4}")
    return input("請輸入您的選擇")

    # 如果需要對齊的話就再多打一個反協槓t
# 設置無線循環，確保程序不退出
while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True) # 要顯示第一項print，所以用Ture
        continue # 要如何不斷進入主菜單?使用continue直接進行下一個循環
    elif keyboard_input == "2":
        num = int(input("您想要存多少錢?請輸入"))
        saveing(num) # 輸入金額
        print(f"餘額為{money}")
        continue
    elif keyboard_input == "3":
        num = int(input("您想要取多少錢?請輸入"))
        get_money(num) # 輸入金額
        print(f"餘額為{money}")
        continue
    else:
        print("程序退出")
        break

