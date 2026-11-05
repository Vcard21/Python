import hashlib
from pathlib import Path
import sqlite3
# Phase 1
# import Path and hashlib to connect and give sha256 value
file_location = Path(r"C:\Python\Python\Side project")
database_path = Path("WatchDog.db").resolve()
# 使用resolve轉換成絕對路徑
database = sqlite3.connect(database_path)
# 建立檔案並連接至資料庫
directory = database.cursor()
# 建立游標
# 建立內部資料表
directory.execute(
    """
    CREATE TABLE IF NOT EXISTS WatchDog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Path_location TEXT NOT NULL,
    Oldhash TEXT NOT NULL
    )
"""
)
directory.execute(
    """
    CREATE TABLE IF NOT EXISTS Baseline_exists (
    id INTEGER PRIMARY KEY CHECK(id = 1),
    Baseline_state INTEGER NOT NULL CHECK(Baseline_state IN (0, 1))
    )
"""
)
directory.execute(
    "INSERT OR IGNORE INTO Baseline_exists (id, Baseline_state) VALUES (?, ?)",
    (1, 0)
)
"""
!GPT說明!
這句可以直接理解成：

嘗試 INSERT：
id = 1
Baseline_state = 0

如果成功
→ 第一次啟動，建立初始狀態

如果 id = 1 已經存在
→ 因為 PRIMARY KEY 衝突
→ IGNORE
→ 完全不修改原本資料
"""
# CHECK(id = 1)
# → id 只允許等於 1
# CHECK(Baseline_state IN (0, 1))
# → 狀態只會有0或1

""" SQLITE3 筆記
id
→ 欄位名稱

INTEGER
→ 整數

PRIMARY KEY
→ 這一列的唯一識別碼

AUTOINCREMENT
→ 新增 row 時，SQLite 自動幫 id 往上加
"""


"""
Issue：How to determine whether baseline has been initialized 

原設計：透過第一筆資料是否存在判斷baseline是否建立。

問題：若監控目錄本身為空，baseline可以合理地包含0 rows，因此「0 rows」無法區分「尚未初始化」與「已初始化但baseline為空」。

TODO：研究SQLite中更適合保存／判斷baseline initialization state的方法。

Update：Using fetchone tool return VALUES to determine already build baseline or not

Update2：fetchone 無法判斷空資料中新增的檔案是否是本來就有還是惡意放出，需用其他方式

Solution：
使用獨立的 Baseline_exists table 保存初始化狀態。

Baseline_state = 0
→ 尚未初始化

Baseline_state = 1
→ 已初始化，即使 WatchDog table 為 0 rows 也成立
"""
directory.row_factory = sqlite3.Row
# core setting to control what data will return by database(sqlite3)
directory.execute("SELECT  Baseline_state FROM Baseline_exists")
# select Old hash and use by baseline,so baseline use fetchone tool to check data are None or not
baseline = directory.fetchone()
# determine baseline is None or not
New_hash = {}
# add a dict that current status could add into

if baseline["Baseline_state"] == 0:
    # add baseline
    for file in file_location.rglob("*"):
        if file.resolve() == database_path: # 為什麼還要再寫一次在原本的呢?因為尚未建立新DB時，也有可能把自己寫進baseline，第二次才排除變成刪除
            continue
        if not file.is_file():
            continue
        # 這邊再寫一次是為了防止rglob讀取所有檔案時，把資料夾也當成普通檔案，而else中的這次是為了防止非檔案的物件也被讀取
        # Path的功能rglob去遍歷那個路徑的某一檔案，遍歷什麼檔案用（）內指定
        print(f"file has been found{file}")
        file_bytes = file.read_bytes()
        # 抓到的檔案py檔案讀取後用bytes的方式呈現
        hash_num = hashlib.sha256(file_bytes).hexdigest()
        # 把用bytes方式呈現的file_bytes加上sha256雜湊值，雜湊值用64個十六位進制表示
        directory.execute("INSERT INTO WatchDog(Oldhash, Path_location) VALUES (?,?)", (hash_num, str(file)))
        # 建立第一批資料baseline
        print("beseline are now created")

    directory.execute(
        "UPDATE Baseline_exists SET Baseline_state = ? WHERE id = ?",
        (1, 1)
    )
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

        """
        為什麼要轉成絕對路徑？
        1.避免因執行地點不同而報錯
        2.解決多模組呼叫的衝突
        3.消除符號連結（Symlink）與相對符號
        4.提高安全性
        以上為AI解答
        """
        if file.resolve() == database_path:
            continue
        file_bytes = file.read_bytes()
        #     # 抓到的檔案py檔案讀取後用bytes的方式呈現
        hash_num = hashlib.sha256(file_bytes).hexdigest()
        #     # 把用bytes方式呈現的file_bytes加上sha256雜湊值，雜湊值用64個十六位進制表示
        New_hash[str(file)] = hash_num # 這邊要改是因為之前New_hash是path物件，為了要跟Old_hash作對比，轉成同樣的str，才能做對比
        # add current status of hash to compare baseline
        #
        # if str(file) in Old_hash:
        #     # 如果沒變
        #     if New_hash[file] == Old_hash[str(file)]:
        #         # 再度判斷hash是否有變
        #         print("Unchange")
        #     else:
        #         directory.execute(
        #                      "UPDATE WatchDog SET Oldhash = ? WHERE Path_location = ?", (New_hash[file],str(file))
        #                  )
        #         print("Change")
        # else:
        #     # else:
        #     """
        #     錯誤，原來的if else就是再講file是否有在舊hash中，那else就只會有file不存在舊hash的可能性。
        #     所以我不應該繼續加deleted的判斷，只會有新增的判斷。
        #     deleted是原本有但現在沒有的判斷，從一開始有這件事就不應該存在於第一個else的判斷上。
        #     """
        #     directory.execute("INSERT INTO WatchDog(Path_location,Oldhash) VALUES (?,?)",(str(file),New_hash[file]))
        #     print(f"Found new file{New_hash[file]} that wasn't exist before.(Add to Database)")
        #     """
        #     todo:
        #     add Not Null for database to make sure None value are truly null
        #     -Solved
        #     """
    """
    錯誤示範：

    # 用resolve功能判定絕對路徑，如果這個路徑跟database存著的Watch dog db相同
    # 那就中斷這一次的資料輸入，進入下一個循環
    # 用location儲存file的檔案路徑，使用Path.resolve這個功能去把路徑轉成絕對路徑
    location = str(Path.resolve(file))
    if file_location == location:
        continue
    #Path的功能rglob去遍歷那個路徑的某一檔案，遍歷什麼檔案用（）內指定
            """
    directory.execute("SELECT Path_location,Oldhash FROM WatchDog")
    # select Path and Old hash
    # after select Path and Old hash,storage database values as dict,then two dict should be comparable
    Old_hash = {row["Path_location"]: row["Oldhash"] for row in directory.fetchall()}

    # 兩者都一樣的話
    common_keys = New_hash.keys() & Old_hash.keys()
    for path in common_keys:
        compare1 = New_hash[path]
        compare2 = Old_hash[path]

        if compare1 == compare2:
            continue
        else:
            print(f"{path} has changed")
            directory.execute(
                "UPDATE WatchDog SET Oldhash = ? WHERE Path_location = ?", (New_hash[path], path)
            )

    # 兩者有一個不一樣的話
    added_keys = New_hash.keys() - Old_hash.keys()
    for path in added_keys:
        directory.execute("INSERT INTO WatchDog(Path_location,Oldhash) VALUES (?,?)", (path, New_hash[path]))
        print(f"Found new file{path} that wasn't exist before.(Add to Database)")

    # 刪除
    deleted_keys = Old_hash.keys() - New_hash.keys()
    if not deleted_keys:
        print("No file got Deleted")
    else:
        for path in deleted_keys:
            print(f"file {path} has been Deleted")
            directory.execute(
                "DELETE FROM WatchDog WHERE Path_location = ?",
                (path,)
            )
            # 這邊要是deleted的判斷，既然路徑存不存在舊hash的判斷已經在上面，那只能另開刪除的判斷
            # 這邊就已經代表是路徑不相符的時候，所以路徑不相符時的判斷就應該是【刪除、新增】
            # if  str(file) not in New_hash: # 這邊應該是刪除，想想看，刪除應該用什麼判斷?應該是原本有但現在沒有
            #     print(f"The file has been Deleted")
    database.commit()
    database.close()
    # 以下暫時不會用到
    # with open('data list.txt','rb') as f:
    #     content = f.readlines()
    #     directory.execute("INSERT INTO WatchDog (New hash) VALUES (hash_num, '{}')".format(hash_num))