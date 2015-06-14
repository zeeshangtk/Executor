
from src.code.common import log
import paramiko
from paramiko import AuthenticationException
import md5
import os
import time

module_name = "SSHImplementation-"


class SSHImplementation(object):

    SSH_PORT = 22

    def __init__(self, username, ip_address, password):
        self._user_name = username
        self._ip_address = ip_address
        self._password = password

    def execute_command_on_remote_machine(self, list_of_command):
        """
        Executes a list of commands in the remote
        machine by using ssh internally
        :param list_of_command:
        :return:
        """
        cilent_connection = self._get_connection()

        if list_of_command is None or not list_of_command:
            return

        self._execute_command_remotely_single_session(
            cilent_connection, list_of_command)

    def _create_remote_directory(self, destination, sftp_client, src_file):
        try:
            if (os.path.isdir(src_file)):
                sftp_client.mkdir(destination)
        except IOError, e:
            log.info("Cannot create directory on remote machine")

    def copy_file_to_remote_server(self, src_and_dest_dict):
        sftp_client = self._getSFTPConnection()
        failed_file_dict = {}
        for src_file, destination in src_and_dest_dict.iteritems():
            # sftp_client.chdir(dest_folder)
            # Note:This is a bug from the library itself that does
            # not allow the destination to be folder.
            # I have to manually pass all the file
            # name.
            self._create_remote_directory(destination, sftp_client, src_file)
            try:
                print "copying file "+src_file+" dest "+destination
                sftp_client.put(src_file, destination,None,True)
            except Exception, e:
                print "Unable to copy file " + src_file + " " + e.message
                log.error("Unable to copy file " + src_file + " " + e.message)
                raise e


        for src_file, destination in src_and_dest_dict.iteritems():
            if(not self.validate_if_the_file_was_replicated(src_file,destination)):
                failed_file_dict[src_file]=destination
        return failed_file_dict


    def validate_if_the_file_was_replicated(self,local_file,remote_file):
        is_file_replicated = False
        sub_module = module_name + self.validate_if_the_file_was_replicated.func_name
        sftp = self._getSFTPConnection()
        try:
            if sftp.stat(remote_file):
                local_file_data = open(local_file, "rb").read()
                remote_file_data = sftp.open(remote_file).read()
                md1 = md5.new(local_file_data).digest()
                md2 = md5.new(remote_file_data).digest()
                if md1 == md2:
                    is_file_replicated = True

        except Exception as e:
            log.error(sub_module + "Error "+e.message+" while "
                      "validating if file was copied or not for source "+local_file+" destination "+remote_file)

        return  is_file_replicated



    def _execute_command_remotely_single_session(self, client, list_of_command):
        """
            Executes the list of linux command in a single remote session
        """
        sub_module = module_name + \
            self._execute_command_remotely_single_session.func_name
        stdin = None
        stdout = None
        try:
            channel = client.invoke_shell()
            stdin = channel.makefile('wb')
            stdout = channel.makefile('rb')

            command_string = ""
            command_string = self._get_command_string(list_of_command)
            stdin.write(command_string)
            print "The output of command is "+str(stdout.readlines())
            exit_code = channel.recv_exit_status()
            # print "the exit_code is "+str(exit_code)

            if(exit_code!=0):
                raise Exception("Failed to execute the commands "+command_string+" . Exiting now")

            log.info(sub_module + "The output of the " + command_string
                     + " is " + str(stdout.readlines()))

        except Exception as e:
            log.error(sub_module + "ERROR while executing command" + e.message)
            print e.message
            raise e
        finally:
            stdout.close()
            stdin.close()
            client.close()

    def _get_connection(self):
        sub_module = module_name + self._get_connection.func_name
        log.info("connecting to " + self._ip_address +
                 " with username " + self._user_name)
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self._ip_address, port=SSHImplementation.SSH_PORT,
                           username=self._user_name, password=self._password, pkey=None)
            log.info(sub_module +
                     "Connected successfully to the remote machine with ip"
                     + self._ip_address)
        except AuthenticationException as e:
            log.error(sub_module + "Unable to connect with ip" +
                      self._ip_address + " with error" + e.message)
            raise Exception("Invalid user name or password for ip" +
                            self._ip_address + " with username " + self._user_name)
        except Exception as e:
            log.error(sub_module + "Unable to connect with ip" +
                      self._ip_address + " with error" + e.message)
            raise e
        return client

    def _getSFTPConnection(self):
        """
            Opens an SFTP connection if not already open
        :return: a sftp clinet object
        """
        subModule = module_name + self._getSFTPConnection.func_name + "-"

        log.info(subModule + "  connecting to " + self._ip_address +
                 " with username " + self._user_name)
        transport = paramiko.Transport(
            (self._ip_address, SSHImplementation.SSH_PORT))
        transport.connect(username=self._user_name, password=self._password)
        sftp_client = paramiko.SFTPClient.from_transport(transport)
        log.info(subModule + "Successfuly connected to " + self._ip_address)
        return sftp_client

    def _get_command_string(self, list_of_command):
        """
        Appends a list of command to a string and add exit to it
        :param list_of_command:
        :return:
        """
        command_string = ""

        for command in list_of_command:
            command_string += command + "\n"
        command_string += "exit \n"

        return command_string
