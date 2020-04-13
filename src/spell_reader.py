import json
import os

def load_spells():
    path = os.path.join(os.curdir, "..\\data\\spells.json")
    file = open(path, "r")
    data = file.read()
    return len(data)

print(f"{load_spells()}")