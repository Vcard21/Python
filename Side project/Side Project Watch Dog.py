import hashlib
from pathlib import Path
import sqlite3

# Phase 1
# import Path and hashlib to connect and give sha256 value
file_location = Path(r"C:\Users\\Desktop\python-training")
database = sqlite3.connect('WatchDog.db')
# 建立檔案
directory = database.cursor()
# 建立游標
directory.execute(
    # 建立內部資料表
    """
    CREATE TABLE IF NOT EXISTS WatchDog
    (id INTEGER primary key auto_increment,
    New hash,
    Path,
    Old hash,
    )
"""
)
"""
Issue：How to determine whether baseline has been initialized

原設計：透過第一筆資料是否存在判斷baseline是否建立。

問題：若監控目錄本身為空，baseline可以合理地包含0 rows，因此「0 rows」無法區分「尚未初始化」與「已初始化但baseline為空」。

TODO：研究SQLite中更適合保存／判斷baseline initialization state的方法。
"""
baseline = True
for file in file_location.rglob("*.py"):
    # Path的功能rglob去遍歷那個路徑的某一檔案，遍歷什麼檔案用（）內指定
    file_bytes = file.read_bytes()
    # 抓到的檔案py檔案讀取後用bytes的方式呈現
    hash_num = hashlib.sha256(file_bytes).hexdigest()
    # 把用bytes方式呈現的file_bytes加上sha256雜湊值，雜湊值用64個十六位進制表示
    directory.execute('INSERT INTO WatchDog(Old hash, Path) VALUES (?,?)', (hash_num, file_location))
    # 建立第一批資料baseline
    baseline = False



    # 以下暫時不會用到
    with open('data list.txt','rb') as f:
        content = f.readlines()
        directory.execute("INSERT INTO WatchDog (New hash) VALUES (hash_num, '{}')".format(hash_num))
        database.commit()
database.close()

