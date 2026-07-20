# # 有很多場景，不僅僅是多個並列條件，還會有滿足前置條件才會二此判斷的多層判斷需求。
# """if 條件1 :
#      if 條件 :
#      """
# # 縮進表示層次關係
# if int(input("你的身高是多少:"))>120:
#     print("身高超出限制，不可以免費")
#     print("但是如果vip條件大於3，就可以免費")
#     if int(input("你的vip級別是多少")) > 3 :
#         print("vip級別達標，可以免費")
#     else:
#         print("sorry，你需要買票10元")
# else:
#     print("您好，小朋友歡迎遊玩")
# print("黑馬動物園")
#
# # if elif else可以自由組合，滿足縮進的要求即可
age = int(input("請輸入你的年齡"))
year = int(input("請輸入入職幾年"))
level = int(input("請輸入你的級別"))
if age >= 18:
    print("你是成年人")
    if age <30:
        print("你的年齡達標了")
        if year > 2:
            print("恭喜你，年齡和入職時間都達標，可以領禮物")
        elif level >1:
            print("恭喜你，年齡和級別達標，可以領禮物")
        else:
            print("不好意思，儘管年齡達標，但是入職時間和級別都不達標")
    else:
        print("不好意思，年齡太大了")
else:
    print("不好意思小朋友不可以領")