import sys

from src.code.executor.ExecutorApi import ExecutorApi
from src.code.reader.ReadActionSet import ReadActionSetFromXML
from src.code.util.Validator import Validator


class Main(object):

    def __init__(self,file_paths):
        self.file_paths = file_paths

    def start_execution(self):

        validator = Validator()
        read_action_set_frm_xml =ReadActionSetFromXML(validator)
        obj = ExecutorApi(read_action_set_frm_xml)
        for file_path in self.file_paths:
            obj.execute_action_set(file_path)


if __name__=="__main__":
    file_paths = []

    for arg in sys.argv:
        if arg.__contains__(".xml"):
            print "The argument is "+arg
            file_paths.append(arg)
    try:
        obj = Main(file_paths)
        obj.start_execution()
    except Exception as e:
        print e.message
        
