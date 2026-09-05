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
# 建立內部資料表
directory.execute(
    """
    CREATE TABLE IF NOT EXISTS WatchDog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Path TEXT NOT NULL,
    Oldhash TEXT NOT NULL
    )
"""
)

"""
Issue：How to determine whether baseline has been initialized 

原設計：透過第一筆資料是否存在判斷baseline是否建立。

問題：若監控目錄本身為空，baseline可以合理地包含0 rows，因此「0 rows」無法區分「尚未初始化」與「已初始化但baseline為空」。

TODO：研究SQLite中更適合保存／判斷baseline initialization state的方法。

Update：Using fetchone tool return VALUES to determine already build baseline or not

-Solved
"""
directory.row_factory = sqlite3.Row
# core setting to control what data will return by database(sqlite3)
directory.execute("SELECT Oldhash FROM WatchDog")
# select Old hash and use by baseline,so baseline use fetchone tool to check data are None or not
baseline = directory.fetchone()
# determine baseline is None or not
New_hash = []
# add a dict that current status could add into
directory.execute("SELECT * FROM WatchDog")
dormant = directory.fetchall()
print(dormant)
if baseline is None:
    # add baseline
    for file in file_location.rglob("*.py"):
        # Path的功能rglob去遍歷那個路徑的某一檔案，遍歷什麼檔案用（）內指定
        file_bytes = file.read_bytes()
        # 抓到的檔案py檔案讀取後用bytes的方式呈現
        hash_num = hashlib.sha256(file_bytes).hexdigest()
        # 把用bytes方式呈現的file_bytes加上sha256雜湊值，雜湊值用64個十六位進制表示
        directory.execute("INSERT INTO WatchDog(Oldhash, Path) VALUES (?,?)", (hash_num, file))
        # 建立第一批資料baseline
        print("beseline are now created")
        database.commit()
    database.close()
else:
    # if baseline already EXISTS,then rglob all the file again to compare the hash_num has change or not
    for file in file_location.rglob("*"):
        if not file.is_file():
            continue
        """
            TODO:
                rglob all file but not include Path itself
            Solvation1:
                using Path.is_file() tool to sparate path and file
            -Solved

            New problem:
                database are a file too,when every changed by program itself,program will tell us the file has changed
            Solvation2:
                using tool Path.resolve()
                這個工具可以把Path轉成解析後的絕對路徑
                konwn by AI
        """
        # 用resolve功能判定絕對路徑，如果這個路徑跟database存著的Watch dog db黨相同
        # 那就中斷這一次的資料輸入，進入下一個循環
        if database == file.path.resolve('python'):
            continue
        #      Path的功能rglob去遍歷那個路徑的某一檔案，遍歷什麼檔案用（）內指定
        file_bytes = file.read_bytes()
        #     # 抓到的檔案py檔案讀取後用bytes的方式呈現
        hash_num = hashlib.sha256(file_bytes).hexdigest()
        #     # 把用bytes方式呈現的file_bytes加上sha256雜湊值，雜湊值用64個十六位進制表示
        New_hash[file] = hash_num
        # # add current status of hash to compare baseline
        directory.execute("SELECT Path,Oldhash FROM WatchDog")
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
                    "UPDATE WatchDog SET Oldhash = ?",New_hash[Path] )
                print("Change")
        else: # 這邊就已經代表是路徑不相符的時候，所以路徑不相符時的判斷就應該是【刪除、新增】
            if  New_hash[file] is None: # 這邊應該是刪除，想想看，刪除應該用什麼判斷?應該是原本有但現在沒有
                print(f"The file{Old_hash["Path"]} has been Deleted")
            # path不等於空時，代表路徑不同，所以代表新增
            else:
                directory.execute("INSERT INTO WatchDog(Path,Oldhash) VALUES (?,?)", New_hash)
                print(f"Found new file{New_hash[file]} that wasn't exist before.(Add to Database)")
                """
                TODO:
                add Not Null for database to make sure None value are truly null

                -Solved
                """
                database.commit()
    database.close()
# 以下暫時不會用到
# with open('data list.txt','rb') as f:
#     content = f.readlines()
#     directory.execute("INSERT INTO WatchDog (New hash) VALUES (hash_num, '{}')".format(hash_num))