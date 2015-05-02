from src.code.executor import ExecuteAction
from src.code.executor.ExecutorApi import ExecutorApi
from src.code.reader.ReadActionSet import ReadActionSetFromXML
from src.code.util.Validator import Validator


class Main(object):


    def start_execution(self):
        FILE_PATH = "/home/zeeshan/Development/python/Executor/src/test/reader/ActionSetInputToCommandExecutor.xml"
        validator = Validator()
        read_action_set_frm_xml =ReadActionSetFromXML(validator)

        obj = ExecutorApi(read_action_set_frm_xml)
        obj.execute_action_set(FILE_PATH)

if __name__=="__main__":
    obj = Main()
    obj.start_execution()
        
