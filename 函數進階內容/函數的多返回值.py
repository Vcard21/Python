"""
如果一個函數要有多個返回值，該如何書寫代碼
用「逗號」隔開就好
按照返回值的順序，寫對應順序的多個變量接收即可
變量之間用逗號隔開
支持不同類型的數據return
"""
def test_reture():
    return 1,"hello",True
# 類型不受限
x,y,z = test_reture()
# 需要注意的是接收的變量一定要對好順序
print(x)
print(y)
print(z)