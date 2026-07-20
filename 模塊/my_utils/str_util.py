"""
字符串相關工具模塊
"""


def str_reverse(s):
    """
    功能是將字符串完成反轉
    :param s: 將被反轉的字符串
    :return: 反轉後的字符串
    """
    return s[::-1]
# 迴轉s，第一個冒號代表開始切片的地方，中間表示結束切片的地方，最右邊表示步長
# 開頭不寫代表從頭，結尾不寫代表到尾，-1代表從後反著取

def substr(s,x,y):
    """
    功能是按照給定的下標完成給字符串的切片
    :param s: 即將被切片的字符串
    :param x: 切片的開始下標
    :param y: 切片的結束下標
    :return:切片完成後的字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("黑馬程序員"))
    print(substr("黑馬程序員",1,3))
