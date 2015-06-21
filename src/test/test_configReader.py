from unittest import TestCase
from src.code.common.ConfigReader import ConfigReader

__author__ = 'zeeshan'


class TestConfigReader(TestCase):
    file_path = "Executor.cfg"

    def test_read_attribute(self):
        obj = ConfigReader(self.file_path)
        self.assertEqual("false",obj.read_attribute("Executor","fail_fast"))