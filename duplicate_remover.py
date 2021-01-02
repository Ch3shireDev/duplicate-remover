import glob
import sys
import hashlib
import os
import logging
from pathlib import Path
from humanize import naturalsize

def get_sha(path):
    BUF_SIZE = 65536
    sha1 = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)

    return sha1.hexdigest()

def delete_file(path):
    try:
        os.remove(file)
    except:
        pass

def get_size(path):
    return Path(path).stat().st_size

def info(text):
    logging.info(text)
    print(text)

print("Program usunie wszystkie duplikaty plikow z biezacego folderu i wszystkich mozliwych podfolderow. Nastepnie skasuje puste podfoldery.")

answer = None

while answer != "t":
    print("Czy wywolac program? t/n")
    answer = input()
    if answer != 't':
        exit()

skroty = set()
logging.basicConfig(filename="logs.txt", level=logging.INFO)

info("Kasowanie duplikatow...")

total_size = 0

for file in glob.glob('./**', recursive=True):
    try:
        sha = get_sha(file)
        if sha in skroty:
            total_size += get_size(file)
            delete_file(file)
            info(f"Usunieto plik {file}")
        else:
            skroty.add(sha)

    except IOError as e:
        continue
    except:
        exit()

info("Kasowanie pustych folderow...")

is_empty = True
while is_empty:
    is_empty = False
    for _dir, a,b in os.walk('.'):
        if a == [] and b == []:
            os.rmdir(_dir)
            is_empty = True


size = naturalsize(total_size)

info(f"Skasowano {size} duplikatów.")