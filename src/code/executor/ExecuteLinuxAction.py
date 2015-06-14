import os
from src.code.common import log


__author__ = 'zeeshan'

module_name = "ExecuteLinuxAction- "

class ExecuteLinuxAction(object):

    def __init__(self,ssh):
        self.ssh = ssh

    def execute_command_on_remote_machine(self, list_of_command):
        """ExecuteLinuxAction
        Executes a list of commands in the remote
        machine by using ssh internally
        :param list_of_command:
        :return:
        """
        self.ssh.execute_command_on_remote_machine(list_of_command)

    def copy_file_to_remote_server(self, src_file_list, dest_folder):
        """
        Copies a list of files from the list to the destination folder
        :param src_file_list:
        :param dest_folder:
        :return:
        """
        src_and_destination_dict = {}

        for src_file in src_file_list:
            file_name = os.path.split(src_file)[1]
            dest_file = dest_folder + os.sep + file_name
            src_and_destination_dict[src_file]=dest_file

        log.info("The map that is candiate for replication is "+str(src_and_destination_dict))
        return self.ssh.copy_file_to_remote_server(src_and_destination_dict)

