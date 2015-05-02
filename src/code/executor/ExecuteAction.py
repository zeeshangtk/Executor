import glob

__author__ = 'zeeshan'

class ExecuteAction(object):

    def __init__(self,action_set,execute_native_action):
        self._action_set = action_set
        self.execute_native_action = execute_native_action


    def _execute_command(self,cmd_string):
        pass

    def _execute_remote_command(self,cmd_string):
        cmd_list = []
        cmd_list.append(cmd_string)
        self.execute_native_action.execute_command_on_remote_machine(cmd_list)

    def _copy_file(self,src_path,target_path):
        pass

    def _copy_file_to_remote_server(self,src_path,target_path):
        list_of_files = glob.glob(src_path)
        self.execute_native_action.copy_file_to_remote_server(list_of_files,target_path)

    def _copy_file_to_ftp_server(self):
        pass

    def execute_action_list(self):
        list_of_action = self._action_set.list_of_action

        for action in list_of_action:

            if action.get_command() == "cmd":
                self._execute_command(action.get_command_input())

            elif action.get_command() == "rcmd":
                self._execute_remote_command(action.get_command_input())

            elif action.get_command()=="cp":
                command_input_list = action.get_command_input().split(" ")
                self._copy_file(command_input_list[0],command_input_list[1])

            elif action.get_command() == "rcp":
                command_input_list = action.get_command_input().split(" ")
                self._copy_file_to_remote_server(command_input_list[0],command_input_list[1])