import hashlib
from pathlib import Path
import sqlite3

file_location = Path(r"C:\Users\\Desktop\python-training")
database = sqlite3.connect('WatchDog.db')
directory = database.cursor()
directory.execute(f"CREATE TABLE IF NOT EXISTS WatchDog(id {hash_num} primary key auto_increment)")""")
for file in file_location.rglob("*.py"):
    file_bytes = file.read_bytes()
    hash_num = hashlib.sha256(file_bytes).hexdigest()
with open('data list.txt',encoding='utf-8') as f:
    content = f.readlines()
    directory.execute(list(content)[0],[100])
    database.commit()
database.close()

