from src.code.executor.ExecuteLinuxAction import ExecuteLinuxAction
from src.code.executor.SSHImplementation import SSHImplementation


__author__ = 'zeeshan'
from unittest import TestCase

PASSWORD = "namchi123"
USER_NAME = "zeeshan"
IP_ADDRESS = "127.0.0.1"

class testExecuteLinuxAction(TestCase):

    ssh_obj = SSHImplementation(USER_NAME,IP_ADDRESS,PASSWORD)
    def test_execute_command_on_remote_machine_valid_input(self):
        obj = ExecuteLinuxAction(ssh=self.ssh_obj)
        list_of_command = ["ls","df -h"]
        obj.execute_command_on_remote_machine(list_of_command)

    def test_execute_command_on_remote_machine_valid_command(self):
        try:
            obj = ExecuteLinuxAction(ssh=self.ssh_obj)
            list_of_command = ["ls","df-asdf"]
            obj.execute_command_on_remote_machine(list_of_command)
        except Exception as e:
            if not e.message.__contains__("Failed to execute the commands "):
                self.fail("The error message is invalid")

    def test_execute_command_on_remote_machine_invalid_input_shld_fail(self):
        try:
            ssh_obj = SSHImplementation("INVALID",IP_ADDRESS,PASSWORD)
            obj = ExecuteLinuxAction(ssh=ssh_obj)
            list_of_command = ["ls","df -h"]
            obj.execute_command_on_remote_machine(list_of_command)
            self.fail("Should have thrown a exception for authentication failure")
        except Exception as e:
            if not e.message.__contains__("Invalid user name or password"):
                self.fail(" The error message is invalid "+e.message)

    def test_execute_command_on_remote_machine_empyt_cmd_list(self):
        obj = ExecuteLinuxAction(ssh=self.ssh_obj)
        list_of_command = []
        obj.execute_command_on_remote_machine(list_of_command)

    def test_execute_command_on_remote_machine_with_invalid_cmd(self):
        obj = ExecuteLinuxAction(ssh=self.ssh_obj)
        list_of_command = ["invalid_command"]
        obj.execute_command_on_remote_machine(list_of_command)

    def test_copy_file_to_remote_server(self):
        obj = ExecuteLinuxAction(ssh=self.ssh_obj)
        print obj.copy_file_to_remote_server(["/home/zeeshan/PycharmProjects/Executor/Executor/Setup.org"],"/tmp/ali/")