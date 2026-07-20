"""
定義兩個變量，用以獲取從鍵盤輸入的內容，並給出提示信息:
變量1，變量名:user_name，紀錄用戶名稱
變量2，變量名:user_type，記錄用戶類型
並通過格式化字符串的形式，通過print語句輸出歡迎信息，如下:
您好:黑馬程序員，您是尊貴的:sssssvip用戶，歡迎您的光臨。
"""
user_name = input("請輸入名字")
user_type = input("請輸入公司職稱")
print("您好: %s %s，歡迎使用本登錄系統" % (user_name,user_type))
