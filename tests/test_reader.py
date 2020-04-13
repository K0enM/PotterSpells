import os
from src import spell_reader as sr


def test_file_read(tmp_path):
    file = open(os.path.join(tmp_path, "hello.txt"), "w")
    file.write("yeet")
    file.close()
    assert sr.load_spells(os.path.join(tmp_path, "hello.txt")) == 4, "Did not load correct file"
