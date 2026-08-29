import hashlib
import pathlib
from pathlib import Path
import sqlite3

# Phase 1
# import Path and hashlib to connect and give sha256 value
file_location = Path(r"C:\Users\\Desktop\python-training")
database = sqlite3.connect('WatchDog.db')
# 建立檔案並連接至資料庫
directory = database.cursor()
# 建立游標
directory.execute(
    # 建立內部資料表
    """
    CREATE TABLE IF NOT EXISTS WatchDog
    (id INTEGER primary key auto_increment,
    Path,
    Old hash,
    )
"""
)

"""
Issue：How to determine whether baseline has been initialized !Solved!

原設計：透過第一筆資料是否存在判斷baseline是否建立。

問題：若監控目錄本身為空，baseline可以合理地包含0 rows，因此「0 rows」無法區分「尚未初始化」與「已初始化但baseline為空」。

TODO：研究SQLite中更適合保存／判斷baseline initialization state的方法。

Update：Using fetchone tool return VALUES to determine already build baseline or not
"""
directory.row_factory = sqlite3.Row
# core setting to control what data will return by database(sqlite3)
directory.execute("SELECT Old hash FROM WatchDog")
# select Old hash and use by baseline,so baseline use fetchone tool to check data are None or not
baseline = directory.fetchone()
# determine baseline is None or not
New_hash = []
# add a dict that current status could add into
if baseline is None:
    # add baseline
    for file in file_location.rglob("*.py"):
        # Path的功能rglob去遍歷那個路徑的某一檔案，遍歷什麼檔案用（）內指定
        file_bytes = file.read_bytes()
        # 抓到的檔案py檔案讀取後用bytes的方式呈現
        hash_num = hashlib.sha256(file_bytes).hexdigest()
        # 把用bytes方式呈現的file_bytes加上sha256雜湊值，雜湊值用64個十六位進制表示
        directory.execute('INSERT INTO WatchDog(Old hash, Path) VALUES (?,?)', (hash_num, file))
        # 建立第一批資料baseline
        database.commit()
    database.close()
else:
    # if baseline already EXISTS,then rglob all the file again to compare the hash_num has change or not
    for file in file_location.rglob("*.py"):
        # Path的功能rglob去遍歷那個路徑的某一檔案，遍歷什麼檔案用（）內指定
        file_bytes = file.read_bytes()
        # 抓到的檔案py檔案讀取後用bytes的方式呈現
        hash_num = hashlib.sha256(file_bytes).hexdigest()
        # 把用bytes方式呈現的file_bytes加上sha256雜湊值，雜湊值用64個十六位進制表示
        New_hash[file] = hash_num
    # add current status of hash to compare baseline
    directory.execute("SELECT Path,Old hash FROM WatchDog")
    # select Path and Old hash
    Old_hash = {row["Path"]: row["Old hash"] for row in directory.fetchall()}
    # after select Path and Old hash,storage database values as dict,then two dict should be comparable

    if New_hash[file] == Old_hash[Path]:
        # 如果沒變
        if New_hash[hash_num] == Old_hash["Old hash"]:
            # 再度判斷hash是否有變
            print("Unchange")
        else:
            directory.execute(
                "UPDATE WatchDog SET Old hash = ?",New_hash[Path] )
            print("Change")
    else: # 這邊就已經代表是路徑不相符的時候，所以路徑不相符時的判斷就應該是【刪除、新增】
        if  New_hash[file] is None: # 這邊應該是刪除，想想看，刪除應該用什麼判斷?應該是原本有但現在沒有
            print(f"The file{Old_hash["Path"]} has been Deleted")
        # path不等於空時，代表路徑不同，所以代表新增
        else:
            directory.execute("INSERT INTO WatchDog(Path,Old_hash) VALUES (?,?)", New_hash)
            print(f"Found new file{New_hash[file]} that wasn't exist before.(Update to Database)")
            """
            TODO:
            add Not Null for database to make sure None value are truly null
            """
    # 以下暫時不會用到
    # with open('data list.txt','rb') as f:
    #     content = f.readlines()
    #     directory.execute("INSERT INTO WatchDog (New hash) VALUES (hash_num, '{}')".format(hash_num))