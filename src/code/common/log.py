__author__ = 'zeeshan'

import  logging
LOG_FILE_NAME="Executor.log"
logging.basicConfig(filename=LOG_FILE_NAME, level=logging.INFO,format='%(asctime)s %(message)s')

def info(msg,*arg,**kwargs):
    logging.info(msg=msg,*arg,**kwargs)

def warning(msg,*arg,**kwargs):
    logging.warning(msg=msg,*arg,**kwargs)

def error(msg,*arg,**kwargs):
    logging.error(msg=msg,*arg,**kwargs)