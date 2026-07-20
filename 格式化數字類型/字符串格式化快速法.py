# 通過語法:f"內容{}"的格式來快速格式化
# 特點是不限數據類型，也不做精度控制
name = "船製播客"
set_up_year = 2006
stock_price = 19.99
# f:format
print(f"我是{name}，我成立於:{set_up_year}年，我今天的股價是:{stock_price}")

# 適合對精度沒有要求的時候進行快速的格式化