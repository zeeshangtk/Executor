import sys
import os
from src.code.executor.ExecutorApi import ExecutorApi
from src.code.reader.ReadActionSet import ReadActionSetFromXML
from src.code.util.Validator import Validator


class Main(object):

    def __init__(self,file_paths):
        self.file_paths = file_paths

    def start_execution(self):

        validator = Validator()
        # print "reading from file_paths "+str(self.file_paths)
        read_action_set_frm_xml =ReadActionSetFromXML(validator)
        obj = ExecutorApi(read_action_set_frm_xml)
        for file_path in self.file_paths:
            obj.execute_action_set(file_path)


if __name__=="__main__":
    file_paths = []
    print sys.path
    sys.path.append(os.path.split(sys.argv[0])[0])
    for arg in sys.argv:
        if arg.__contains__(".xml"):
            print "The argument is "+arg
            file_paths.append(arg)
    try:
        obj = Main(file_paths)
        obj.start_execution()
    except Exception as e:
        print e.message
        
