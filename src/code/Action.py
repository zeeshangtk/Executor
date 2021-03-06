
__author__ = 'zeeshan'


class Action(object):

    """
        Represent the command string and the type of command.
        For eg: The type of command is cp i.e copy and action string is
        the input for that command
    """

    def __init__(self, type, _command_input):
        """
            Represents input that needs to be given to a command
        """
        self._command_input = _command_input
        """
        Represents the command
        """
        self._command = type

    def __eq__(self, other):
        if self._command_input != other.get_command_input():
            return False
        elif self._command != other.get_command():
            return False

        return True

    def get_command_input(self):
        return self._command_input

    def get_command(self):
        return self._command


class ActionSet(object):

    """
        ActionSet is  the poyo object that represents the input xml.
        This object has the list of command that has to be executed.
    """

    def __init__(self, ip, user_name, password,
                 remote_os, name, list_of_action):
        self.ip = ip
        self.user_name = user_name
        self.password = password
        self.remote_os = remote_os
        self.name = name
        # represents a list of action
        self.list_of_action = list_of_action

    def __eq__(self, other):
        if self.ip != other.ip:
            return False
        if self.user_name != other.user_name:
            return False
        if self.password != other.password:
            return False
        if self.remote_os != other.remote_os:
            return False
        if self.name != other.name:
            return False

        if cmp(self.list_of_action, other.list_of_action) != 0:
            return False

        return True
