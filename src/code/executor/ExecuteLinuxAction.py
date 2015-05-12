import os
from src.code.common import log

__author__ = 'zeeshan'

import paramiko
from paramiko.ssh_exception import AuthenticationException

module_name = "ExecuteLinuxAction- "
class ExecuteLinuxAction(object):

    SSH_PORT = 22

    def __init__(self,ip_address,user_name,password):
        self._ip_address = ip_address
        self._user_name= user_name
        self._password = password

    def execute_command_on_remote_machine(self,list_of_command):
        """
        Executes a list of commands in the remote machine by using ssh internally
        :param list_of_command:
        :return:
        """
        cilent_connection = self._get_connection()

        if list_of_command == None or not list_of_command:
            return
        self._execute_command_remotely_single_session(cilent_connection,list_of_command)

    def copy_file_to_remote_server(self,src_file_list,dest_folder):
        """
        Copies a list of files from the list to the destination folder
        :param src_file_list:
        :param dest_folder:
        :return:
        """
        sftp_client = self._getSFTPConnection()

        for src_file in src_file_list:
            # sftp_client.chdir(dest_folder)
            ###Note:This is a bug from the library itself that does
            ##not allow the dest to be folder.I have to manually pass all the file
            ##name.
            try:

                file_name =  os.path.split(src_file)[1]
                log.info("The file "+file_name+" to be copied  to destination path "+dest_folder+os.sep+file_name)
                sftp_client.put(src_file,dest_folder+os.sep+file_name)
                print "The file "+file_name+" has  been copied  to destination path "+dest_folder+os.sep+file_name

            except Exception as e:
                print e.message
                log.error(e.message)
                raise e


    def _execute_command_remotely_single_session(self, client, list_of_command):
        """
            Executes the list of linux command in a single remote session
        """
        sub_module = module_name+self._execute_command_remotely_single_session.func_name
        stdin = None
        stdout = None
        try:
            channel = client.invoke_shell()
            stdin = channel.makefile('wb')
            stdout = channel.makefile('rb')

            command_string = ""
            command_string = self._get_command_string(list_of_command)
            stdin.write(command_string)

            log.info(sub_module+"The output of the "+command_string
                         +" is "+str(stdout.readlines()))

        except Exception as e:
            log.error(sub_module+"ERROR while executing command"+e.message)
            print e.message
            raise e
        finally:
            stdout.close()
            stdin.close()
            client.close()

    def _get_connection(self):
        sub_module = module_name+self._get_connection.func_name
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self._ip_address, port=ExecuteLinuxAction.SSH_PORT, username=self._user_name, password=self._password, pkey=None)
            log.info(sub_module+"Connected successfully to the remote machine with ip"+self._ip_address)
        except AuthenticationException as e:
            log.error(sub_module+"Unable to connect with ip"+self._ip_address+" with error"+e.message)
            raise Exception("Invalid user name or password for ip"+self._ip_address+" with username "+self._user_name)
        except Exception as e:
            log.error(sub_module+"Unable to connect with ip"+self._ip_address+" with error"+e.message)
            raise  e
        return client


    def _getSFTPConnection(self):
        """
            Opens an SFTP connection if not already open
        :return: a sftp clinet object
        """
        subModule = module_name + self._getSFTPConnection.func_name+"-"

        transport = paramiko.Transport((self._ip_address, ExecuteLinuxAction.SSH_PORT))
        transport.connect(username=self._user_name, password=self._password)
        sftp_client = paramiko.SFTPClient.from_transport(transport)
        log.info(subModule+"Successfuly connected to "+self._ip_address)
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

        print "the command is " + command_string
        return command_string