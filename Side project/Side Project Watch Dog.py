import hashlib
from pathlib import Path
import sqlite3
from select import select

file_location = Path(r"C:\Users\\Desktop\python-training")
database = sqlite3.connect('WatchDog.db')
directory = database.cursor()
directory.execute(
    """
    CREATE TABLE IF NOT EXISTS WatchDog
    (id INTEGER primary key auto_increment,
    New hash TEXT,
    )
"""
)
for file in file_location.rglob("*.py"):
    file_bytes = file.read_bytes()
    hash_num = hashlib.sha256(file_bytes).hexdigest()
    directory.execute(
        "SELECT COUNT(1) FROM WatchDog WHERE New hash = ?",
        
    )
    with open('data list.txt','rb') as f:
        content = f.readlines()
        directory.execute(hash_num)
        database.commit()
database.close()

