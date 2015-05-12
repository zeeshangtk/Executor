import shutil
import sys
from src.code.Main import Main

__author__ = 'zeeshan'


if __name__=="__main__":
    file_paths = []

    try:
        for arg in sys.argv:
            if arg.__contains__(".xml"):
                print "The input file is "+arg+" \n"
                file_paths.append(arg)
        obj = Main(file_paths)
        obj.start_execution()

    except Exception as e:
        print e.message
