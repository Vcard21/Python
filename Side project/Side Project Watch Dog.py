import hashlib
from pathlib import Path

file_location = Path(r"C:\Users\\Desktop\python-training")
for file in file_location.rglob("*.py"):
    file_bytes = file.read_bytes()
    hash_num = hashlib.sha256(file_bytes).hexdigest()
with open('data list.txt','rb') as f:
    content = f.readlines()
    print(content)
