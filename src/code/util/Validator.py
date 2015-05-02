from xml.etree import ElementTree
import os

__author__ = 'zeeshan'


class Validator(object):

    def check_if_file_exists(self, file_path):
        if not os.path.exists(file_path):
            raise Exception("The file " + os.path.abspath(file_path) + " does not exists")

    def validate_action_set_xml(self, file_path):
        self.check_if_file_exists(file_path)
        print "the file path" + str(file_path)
        try:
            return ElementTree.parse(file_path)
        except Exception as e:
            raise Exception(
                "the file file " + file_path + " is invalid " + str(e.message))
