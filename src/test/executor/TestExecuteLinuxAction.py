from src.code.executor.ExecuteLinuxAction import ExecuteLinuxAction


__author__ = 'zeeshan'
from unittest import TestCase

PASSWORD = "namchi123"
USER_NAME = "zeeshan"
IP_ADDRESS = "127.0.0.1"

class testExecuteLinuxAction(TestCase):

    def test_execute_command_on_remote_machine_valid_input(self):
        obj = ExecuteLinuxAction(ip_address=IP_ADDRESS,user_name=("%s" % USER_NAME),password=PASSWORD)
        list_of_command = ["ls","df -h"]
        obj.execute_command_on_remote_machine(list_of_command)

    def test_execute_command_on_remote_machine_invalid_input_shld_fail(self):
        try:
            obj = ExecuteLinuxAction(ip_address=IP_ADDRESS,user_name="INVALID_USER_NAME",password=PASSWORD)
            list_of_command = ["ls","df -h"]
            obj.execute_command_on_remote_machine(list_of_command)
            self.fail("Should have thrown a exception for authentication failure")
        except Exception as e:
            if not e.message.__contains__("Invalid user name or password"):
                self.fail(" The error message is invalid "+e.message)

    def test_execute_command_on_remote_machine_empyt_cmd_list(self):
        obj = ExecuteLinuxAction(ip_address=IP_ADDRESS,user_name=("%s" % USER_NAME),password=PASSWORD)
        list_of_command = []
        obj.execute_command_on_remote_machine(list_of_command)

    def test_execute_command_on_remote_machine_with_invalid_cmd(self):
        obj = ExecuteLinuxAction(ip_address=IP_ADDRESS,user_name=("%s" % USER_NAME),password=PASSWORD)
        list_of_command = ["invalid_command"]
        obj.execute_command_on_remote_machine(list_of_command)

    def test_copy_file_to_remote_server(self):
        obj = ExecuteLinuxAction(ip_address=IP_ADDRESS,user_name=("%s" % USER_NAME),password=PASSWORD)
        obj.copy_file_to_remote_server(["/home/zeeshan/out.txt"],"/tmp/")