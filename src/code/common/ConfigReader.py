import ConfigParser
import os

__author__ = 'zeeshan'

class ConfigReader(object):
    def __init__(self,config_file_path):
        self.config_file_path = config_file_path

    def read_attribute(self,section,attribute):
        configParser = ConfigParser.RawConfigParser()

        if(not os.path.exists(self.config_file_path)):
            raise Exception("The configuration file "+self.config_file_path+" does not existin. "
                        "So loading executor with default configuration")

        configParser.read(self.config_file_path)
        return configParser.get(section,attribute)
