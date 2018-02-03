import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path

    def write(self, text):
        with open(self.path, 'w') as f:
            f.write(text)

    def __str__(self):
       return self.path

    def __add__(self, obj):
        new_path = os.path.join(tempfile.gettempdir(), 'NewFile')
        with open(new_path, 'w') as f:
            with open(self.path, 'r') as self_file:
                f.write(self_file.read())
            with open(obj.path, 'r') as obj_file:
                f.write(obj_file.read())
        return self.path + obj.path



sp = os.path.join(tempfile.gettempdir(), )
pathfile1 = 'log.txt'
pathfile2 = 'log1.txt'
obj_1 = File(pathfile1)
obj_2 = File(pathfile2)
print(obj_1)
obj_1.write('lilili')
obj_test = obj_1 + obj_2
print(obj_test)