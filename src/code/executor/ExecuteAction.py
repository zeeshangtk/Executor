import glob
import traceback

import os
from src.code.common import log
from src.code.util import Constants

__author__ = 'zeeshan'





class ExecuteAction(object):

    def __init__(self, action_set, execute_native_action,cfg):
        self._action_set = action_set
        self.execute_native_action = execute_native_action
        self.cfg = cfg

    def _execute_command(self, cmd_string):
        object = os.popen(cmd_string,"r")
        log.info("The output after executing the command "+cmd_string+" is "+ object.read())

    def _execute_remote_command(self, cmd_string):
        cmd_list = []
        cmd_list.append(cmd_string)
        self.execute_native_action.execute_command_on_remote_machine(cmd_list)

    def _copy_file(self, src_path, target_path):
        pass

    def _copy_file_to_remote_server(self, src_path, target_path):
        list_of_files = glob.glob(src_path)
        log.info("The list of files in src_path " +
                 src_path + " is " + str(list_of_files))
        if(list_of_files == None or not list_of_files):
            print "\n\nThe list of files are empty. Hence not proceeding with replication\n"
            return

        failed_file_dict = self.execute_native_action.copy_file_to_remote_server(
            list_of_files, target_path)

        for src_file, destination in failed_file_dict.iteritems():
            print "Unable to copy file source "+src_file+" destination file "+destination
            log.info("Unable to copy file source "+src_file+" destination file "+destination)

    def _copy_file_to_ftp_server(self):
        pass

    def execute_action_list(self):
        list_of_action = self._action_set.list_of_action

        for action in list_of_action:
            try:
                if action.get_command() == "cmd":
                    self._execute_command(action.get_command_input())

                elif action.get_command() == "rcmd":
                    self._execute_remote_command(action.get_command_input())

                elif action.get_command() == "cp":
                    command_input_list = action.get_command_input().split(Constants.COMMAND_SPLIT_REGEX)
                    self._copy_file(command_input_list[0], command_input_list[1])

                elif action.get_command() == "rcp":
                    command_input_list = action.get_command_input().split(Constants.COMMAND_SPLIT_REGEX)
                    self._copy_file_to_remote_server(
                        command_input_list[0], command_input_list[1])
            except Exception,e:
                print e.message
                if self.cfg.fail_fast == True:
                    raise e

