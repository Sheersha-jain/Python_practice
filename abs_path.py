import os

def absolute_file_path():
    return os.path.abspath('abs_path.py')

print "Absolute path of file is", os.path.abspath('abs_path.py')
