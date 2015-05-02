from unittest import TestCase

from src.code.Action import Action, ActionSet
from src.code.reader.ReadActionSet import ReadActionSetFromXML
from src.code.util.Validator import Validator

SRC_TEST_READER_ = "./"

__author__ = 'zeeshan'


class TestReadActionSetFromXML(TestCase):

    def test_get_actionsets_file_not_present_fail(self):
        try:
            obj = ReadActionSetFromXML(Validator())
            # obj.get_actionsets("ActionSetPass.xml")
            obj.get_actionsets("/opt/nofile.xml")
            self.fail("Should have thrown a no file found exception")
        except Exception as e:
            self.assertEqual(
                e.message, "The file /opt/nofile.xml does not exists")

    def test_get_actionsets_pass(self):

        obj = ReadActionSetFromXML(Validator())
        list_of_actionsets = obj.get_actionsets("%sActionSetPass.xml" %SRC_TEST_READER_)

        dummy_action_0 = [Action("rcp", '/opt/ /opt/'),
                          Action("rcmd", "ls"),
                          Action("rcp", '/opt/jar /opt/jar')]

        dummy_action_1 = [Action("rcp", '/tmp/ /tmp/'),
                          Action("rcmd", 'date',),
                          Action("rcp", '/opt/bin /opt/bin')]

        dummy_actionsets_0 = ActionSet(
            "127.0.0.1", "root1", "123", "Linux", "nameOne", dummy_action_0)
        dummy_actionsets_1 = ActionSet(
            "127.0.0.2", "root2", "1234", "Windows", "nameTwo", dummy_action_1)

        self.assertEqual(list_of_actionsets[0], dummy_actionsets_0)
        self.assertEqual(list_of_actionsets[1], dummy_actionsets_1)

    def test_get_actionsets_invalidfile_fail(self):
        try:
            obj = ReadActionSetFromXML(Validator())
            obj.get_actionsets("%sInvalidActionSet.xml" % SRC_TEST_READER_)
            self.fail("Invalid file exception should be thrown")
        except Exception as e:
            if not e.message.__contains__("is invalid mismatched"):
                self.fail("was expecting invalid xml message")
            print "the erorr message for invalid file is "+e.message

    def test_get_actionsets_null_entry_fail(self):
        try:
            obj = ReadActionSetFromXML(Validator())
            list_of_actionsets = obj.get_actionsets(
                "%sActionSetWithNullParamter.xml" % SRC_TEST_READER_)
        except Exception as e:
            print "the erorr message for null is"+e.message

