# if else是同級

print("歡迎來到黑馬兒童遊樂園，兒童免費，成人收費。")
age = int(input("請輸入你的年齡"))
# 記得input的輸入類型永遠都是str，要修改再自己修改條件式
if age >= 18:
    print("你已成年，遊玩需要補票10元")
else:
# 記得else要加個冒號：
    print("你未成年，可以免費遊玩")
print("祝你遊玩愉快。")

# 通過input語句獲得鍵盤輸入的身高，判斷身高是否超過120cm，並通過print給出信息
print("歡迎來到黑馬動物園")
high_cm = int(input("請輸入你的身高(cm):"))
if high_cm > 120 :
    print("您的身高超出120cm，遊玩需要購票10元")
else:
    print("您的身高未超過120cm，可以免費遊玩")
print("祝您遊玩愉快")