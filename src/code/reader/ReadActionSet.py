from src.code.Action import Action, ActionSet

COMMAND = "cmd"

__author__ = 'zeeshan'


class ReadActionSetFromXML(object):

    def __init__(self, validator):
        self.validator = validator

    def get_actionsets(self, file_path):
        """
          Generate actionsets from the xml file
        :param file_path:
        :return:list_of_actionset
        """
        document = self.validator.validate_action_set_xml(file_path)
        actionsets_list = []

        for action_set_xml in document.findall('actionset'):

            if action_set_xml is None or len(action_set_xml) == 0:
                continue

            action_list = []
            actions = action_set_xml.findall("action")

            for action in actions:
                # TODO need to replace this if else with lookup

                action_list.append(
                    Action(action.attrib.get("%s" % COMMAND), action.text))

                # elif type == "rcmd":
                #     action_list.append(Action(action.text,ExecuteRemoteCommandAction().execute_action))
                # else:
                #     action_list.append(Action(action.text,
                #                               ExecuteRemoteCommandAction().execute_action))
                # action_list.append(action.text)

            action_set = self.__get_action_set_obj(action_list, action_set_xml)

            if action_set is not None:
                actionsets_list.append(action_set)

        return actionsets_list

    def __get_action_set_obj(self, action_list, action_set_xml):

        if action_set_xml is None:
            return None
        # print action_set_xml.
        ip = action_set_xml.attrib['ip']
        username = action_set_xml.attrib['username']
        password = action_set_xml.attrib['password']
        operating_system = action_set_xml.attrib['os']
        name = action_set_xml.attrib['name']

        action_set = ActionSet(
            ip, username, password, operating_system, name, action_list)
        return action_set
