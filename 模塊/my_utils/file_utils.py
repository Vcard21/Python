"""
文件處理相關工具模塊
"""

def print_file_info(file_name):
    """
    功能是，將給定路徑的文件內容輸出到控制台中
    :param file_name:即將讀取的文件路徑
    :return:None
    """
    f = None
    try:
        f = open(file_name,"r",encoding="utf-8")
        content  = f.read()
        print("文件的全部內容如下:")
        print(content)
    except Exception as e:
        print(f"bug，原因是:{e}")
    finally:
        if f: # 如果便亮是None，表示False，如果有任何內容，就是Ture
            f.close()

def append_to_file(file_name,data):
    """
    功能是將指定的數據追加到指定的文件中
    :param file_name:指定的文件路徑
    :param data:指定的數據
    :return:None
    """
    f = open(file_name,"a",encoding="utf-8")
    f.write(data)
    f.write("\n")
    f.close()
if __name__ == '__main__':
    # print_file_info("F:/bill.txt")
    append_to_file("F:/test_append.txt","傳智教育")