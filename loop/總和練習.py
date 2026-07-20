"""
條件：
帳戶餘額1w元，給20名員工發工資
員工編號從1到20，依次領取工資，每人領1000元
領工資時，財務判斷員工的績效分(1-10)(隨機生成)，如果低於5，不發工資，換下一位
如果工資發完了，直接結束發工資
隨機數可以用
import random
num = random.randint(數字幾到幾)
"""
import random
lucky_workers = []
salary = []
money = 10000
month_next = 0
total_paid = 0
paid = 0
for i in range(1,21):
    num = random.randint(1, 10)
    if money <= 0:
        print("帳上沒錢了，下個月再來吧")
        break
    if num == 10:
        if money < 2000:
            paid = money
            month_next = 2000 - money
            total_paid += money
            lucky_workers.append(i)
            print(f"員工{i}績效10，但帳上沒這麼多了，先付{money}，下個月再來吧")
            print("沒錢了下個月再來")
            money = 0
            break
        else:
            money -= 2000
            paid = 2000
            total_paid += 2000
            lucky_workers.append(i)
            print(f"向員工{i}號,發兩倍工資共2000元,帳戶餘額還有{money}元")
    elif num > 5:
        money -= 1000
        paid = 1000
        total_paid += 1000
        print(f"向員工{i}號,發工資1000元,帳戶餘額還有{money}元")
        lucky_workers.append(i)
    else:
        print(f"員工{i},績效未達標,不發工資,下一位")
        continue
    count = [i,paid]
    salary.append(count)
print(f"今日總共發出了{total_paid}薪水")
print(f"今天領到錢的員工編號有:{lucky_workers}")
print(f"員工編號及領到的錢{salary}")
# len() 可以計算清單長度
# 指令,功能,例子
# .append(),往最後面加一個人,lucky.append(10)
# len(),算算清單裡有幾個人,len(lucky)
# lucky[0],叫出「第一個」領錢的人,注意：電腦是從 0 開始數的喔！
# .sort(),幫清單裡的數字從小到大排好,lucky.sort()
#     import random
#     num = random.randint(1, 10)
#     錯誤點!!!先定義隨機數而不是在循環中才定義，這樣隨機數就會被固定住