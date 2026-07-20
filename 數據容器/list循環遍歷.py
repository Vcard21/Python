"""
list循環條件:
定義一個變量表示下標，從0開始
循環條件為下標值<列表的元素數量
while循環語法:
index = 0
while index < len(list):
    元素 = 列表[index]
    對元素進行處理
    index += 1

for循環語法:
for 臨時變量 in 數據容器:
    對臨時變量進行處理
"""
def list_while_func():
    """
    使用while循環遍歷列表的演示函數
    :return: None
    """
    my_list = ["傳智教育","黑馬程序員","python"]
    # 循環控制變量通過下標索引來控制,默認0
    # 每一次循環將下標索引變量+1
    # 循環條件:下標索引變量<列表的元素數量

    # 定義一個變量用來標記列表的下標
    index = 0
    while index < len(my_list):
        # 通過index變量取出對應下標的元素
        element = my_list[index]
        print(f"列表的元素:{element}")

        # 至關重要 將循環變量每次都+1,避免無線循環
        index += 1

def list_for_func2():
    """
    使用for循環遍歷列表的演示函數
    :return:None
    """
    my_list2 = [1,2,3,4,5]
    # for 臨時變量 in 數據容器:
    for element2 in my_list2:
        print(f"列表的元素有:{element2}")

list_while_func()


list_for_func2()

"""
課後總結
1,遍歷指的意思是將容器內的元素依次取出，並處理，稱之為遍歷操作
2,如何遍歷列表的元素，使用while、for循環
3,for 循環和while 循環對比:
for循環更簡單，while更靈活
for用於從容器內依次取出元素並處理，while用以任何需要循環的場景。
"""

"""
課後練習
定義一個列表，內容是:[1,2,3,4,5,6,7,8,9,10]
遍歷列表，取出列表內的偶數，並存入一個新的列表對象中
使用while循環和for循環各操作一次

提示:
通過if 來判斷偶數
通過列表append方法來增加元素
"""
def list_for_func3():
    task_list = [1,2,3,4,5,6,7,8,9,10]
    task_list_new = []
    index = 0
    while index < len(task_list):
        if task_list[index] % 2 ==0:
            # 如果要整除的結果可以使用餘數符號 %
            task_list_new.append(task_list[index])
            index += 1
        else:
            index += 1
    # 為什麼這邊while不使用else就沒辦法跑呢?因為他的if要等到index+1往上才能繼續走
    # 但你寫在裡面就變成沒讀到偶數(2)以前就不跑了，所以讀不到
    print(task_list_new)
def list_for_func4():
    task_list = [1,2,3,4,5,6,7,8,9,10]
    task_list_new = []
    # 在for裡面你甚至不需要寫index = 0，因為它會自動抓下一個
    for task in task_list:
        if task % 2 ==0:
            # index += 1，所以index這根本不用寫，因為他自己會動。
            task_list_new.append(task)
    print(task_list_new)
list_for_func3()
list_for_func4()

