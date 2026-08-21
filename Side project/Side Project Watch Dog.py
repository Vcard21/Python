import hashlib
from pathlib import Path
import sqlite3

file_location = Path(r"C:\Users\\Desktop\python-training")
database = sqlite3.connect('WatchDog.db')
directory = database.cursor()
directory.execute(
    """
    CREATE TABLE IF NOT EXISTS WatchDog
    (id INTEGER primary key auto_increment,
    New hash,
    Old hash,
    )
"""
)
for file in file_location.rglob("*.py"):
    file_bytes = file.read_bytes()
    hash_num = hashlib.sha256(file_bytes).hexdigest()
    with open('data list.txt','rb') as f:
        content = f.readlines()
        directory.execute("INSERT INTO WatchDog (New hash) VALUES (hash_num, '{}')".format(hash_num))
        database.commit()
database.close()

