"""

讀取文件bill
將文件寫出到bill.txt.bak文件作為備份
同時，將文件內標記為測試的數據行丟棄

open和r模式打開一個文件對象，並讀取文件
open和w模式打開另一個文件對象，用於文件寫出
for循環內容，判斷是否是測試，不是就write寫出，是測試就continue跳過
將兩個文件對象均close
"""
f_open_r = open('F:/bill.txt', 'r',encoding='utf-8')
f_open_w = open('F:/bill_loadout.txt.bak', 'w',encoding='utf-8')
for line in f_open_r:
    line = line.strip() # 將換行符處理掉
    # 錯誤示範    if content == "測試":  先將換行符處理掉，然後(",")這邊依據逗號分割
    #           分割出來的一行之中，有5個內容，0,1,3,4，第4個為測試或正式，再用[]抓到我要的內容是否等於測試
    if line.split(",")[4] == "測試":
        continue
    #     將內容寫出去
    f_open_w.write(line)
#     由於前面對test前面已經strip把換行符弄沒了，所以輸出前要再把換行加回來\n
    f_open_w.write("\n")
f_open_r.close()
f_open_w.close()