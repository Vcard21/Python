"""
----W寫入操作----
1,打開
f = open('python.txt','w')
2,讀寫
f.write('hello world')
3,關閉
f.flush()

注意：
1,直接調用write，內容並未真正寫入文件，而是會攢積在程序的內存中，稱之為緩衝區
2,當調用flush的時候，內容會真正寫入文件
3,這樣做是避免頻繁的操作硬盤，導致效率下降(先積累內存在PYTHON程序中，然後再一次性的寫磁碟)
"""

# # 打開檔案，不存在的檔案 ,三模式r.w.a
# f = open('F:/test.txt','w',encoding='utf-8')
# # write寫入
# f.write("hello world") # 會將內容寫入到內存中
# # flush刷新
# # f.flush() # 將內容中積攢的內容寫入到硬碟的文件中
# # close關閉
# f.close() # 其實close方法內置了flush功能，所以如果功能單一的話可以直接使用close

# 打開一個已經存在的文件
f = open('F:/test.txt','w',encoding='utf-8')
# write寫入.flush刷新
f.write('黑馬程序員')
f.flush()

# 當檔案不存在時，會建立新檔案並且輸入我想輸入的內容
# 而當存在時，再次寫write的話會替換掉原本的內容

"""
總結：
1,寫入文件使用open函數的'w'模式進行寫入
2,寫入的方法有：
write()寫入內容
flush()刷新內容到硬碟中
3,注意事項：
w模式，文件不存在，會創建新文件
w模式，文件存在，會清空原有內容
close()方法，帶有flush()方法的功能
"""



"""
-----追加寫入-----

1,打開
f = open('python.txt','a') 把模式改成a即可
2,讀寫
f.write('hello world')
3,關閉
f.flush()

注意：
a模式，檔案不存在會創建檔案
a模式，檔案存在則會在最後追加寫入檔案

"""

# 打開文件，不存在的文件
# f_a = open("F:/test1.txt","a",encoding="utf-8")
# # write寫入
# f_a.write("黑馬程序")
# # flush刷新
# f_a.flush()
# # close關閉
# f_a.close()


f_a = open("F:/test1.txt","a",encoding="utf-8")
# write寫入，flush刷新
f_a.write("\npython") # 反協槓n可以換行
# close關閉
f_a.close()
# w模式再度寫入會清空內容，但是a模式再度寫入是追加
""""
總結：
1,追加寫入文件使用open函數的'a'模式進行寫入
2,追加寫入的方法有(和w模式一致)：
    write()寫入內容
    flush()刷新內容到硬盤中
3,注意事項：
    a模式,文件不存在創建新文件
    a模式,文件存在會在原有內容後面繼續寫入
    可以使用'\n'來寫出換行符
"""