from unittest import TestCase
from src.code.executor.SSHImplementation import SSHImplementation

__author__ = 'zeeshan'

PASSWORD = "namchi123"
USER_NAME = "zeeshan"
IP_ADDRESS = "127.0.0.1"

class TestSSHImplementation(TestCase):
    def test_execute_command_on_remote_machine(self):
        self.fail()

    def test_copy_file_to_remote_server(self):
        self.fail()

    def test_validate_if_the_file_was_replicated_with_changed_file(self):
        ssh_obj = SSHImplementation(username=USER_NAME,ip_address=IP_ADDRESS,password=PASSWORD)
        ssh_obj.validate_if_the_file_was_replicated("Executor.log","/tmp/Executor.log")

    def test_validate_if_the_file_was_replicated_with_different_file(self):
        ssh_obj = SSHImplementation(username=USER_NAME,ip_address=IP_ADDRESS,password=PASSWORD)

        ssh_obj.validate_if_the_file_was_replicated("/home/zeeshan/Development/jars/jmock-2.6.0/hamcrest-unit-test-1.3-sources.jar","/tmp/hamcrest-unit-test-1.3-sources.jar")