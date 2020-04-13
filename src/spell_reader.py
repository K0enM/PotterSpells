import json
import os


def load_spells(file_path):
    path = os.path.join(os.curdir, file_path)
    file = open(path, "r")
    data = file.read()
    return len(data)

