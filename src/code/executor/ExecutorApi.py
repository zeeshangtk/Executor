from src.code.executor.ExecuteAction import ExecuteAction
from src.code.executor.ExecuteLinuxAction import ExecuteLinuxAction
from src.code.executor.SSHImplementation import SSHImplementation
__author__ = 'zeeshan'

class ExecutorApi(object):

    def __init__(self,read_action_set):
        self.read_action_set = read_action_set

    def execute_action_set(self,file_path):
        """
        Takes a action set file path and execute the action in it
        :param file_path:
        :return:
        """
        actionsets_list = self.read_action_set.get_actionsets(file_path)
        for action_set in actionsets_list:
            if(action_set.remote_os=="Linux"):
                obj = ExecuteAction(action_set,ExecuteLinuxAction(SSHImplementation(action_set.user_name,action_set.ip,action_set.password)))
                obj.execute_action_list()


