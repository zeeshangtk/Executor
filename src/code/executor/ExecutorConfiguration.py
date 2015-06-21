import traceback
from src.code.common import log
from src.code.common.ConfigReader import ConfigReader
import  ast
__author__ = 'zeeshan'

class ExecutorConfiguration(object):
    # /home/zeeshan/PycharmProjects/Executor/Executor/Executor.cfg
    # /home/zeeshan/PycharmProjects/Executor/Executor/src/code/executor/ExecutorConfiguration.py
    configuration_file_path = "Executor.cfg"
    section = "Executor"
    # TODO need to replace with a single intialization
    def __init__(self):
        self.fail_fast = True
        self.validate_files_after_copy = True
        self.__load_configuration()

    def __load_configuration(self):
        try:
            config_reader = ConfigReader(config_file_path=self.configuration_file_path)
            fail_fast_tmp = config_reader.read_attribute(section=self.section,attribute="fail_fast")
            self.fail_fast = ast.literal_eval(fail_fast_tmp)
            self.validate_files_after_copy = ast.literal_eval(config_reader.read_attribute(section=self.section,attribute="validate_files"))
        except Exception , e:
            # print str(traceback.format_exc())
            log.error("Could not load configuration from "+self.configuration_file_path+" "+e.message)
        log.info("The configuration are fail_fast = "+str(self.fail_fast)+" validate_files:"+str(self.validate_files_after_copy))


