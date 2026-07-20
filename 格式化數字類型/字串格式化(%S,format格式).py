"""
1.字符串拼接太多太麻煩
2.字符串無法和數字或其他類型完成拼接
ex:
name = "黑馬程序員"
message = "學it就來 %s % name
print(message)
其中的　%Szz
%代表:我要佔位
S代表:將變量變成字符串放入佔位的地方
所以綜合起來的意思就是:我先佔個位置，等等有個遍量過來，我把變成字符串放到佔位的位置

數字類型也可以
"""
name = "黑馬程序員"
message = "學IT: %s" %name
print(message)

# 通過佔位的形式，完成數字和字符串的拼接
class_num = 57
avg_salary = 16781
message = "Python大數據學科,北京%s期,畢業平均工資: %s" %(class_num, avg_salary)
print(message)

# %s=將內容換成字符串放入，%d=將內容轉換成整數放數，%f=將內容轉換成浮點數放入
bl_num = 12
vessel = 16
