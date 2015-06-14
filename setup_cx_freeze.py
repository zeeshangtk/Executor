__author__ = 'zeeshan'

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
sys.path.append("/home/zeeshan/PycharmProjects/Executor/Executor/env/lib/python2.7/site-packages/pycrypto-2.6.1-py2.7.egg-info")
include_files=["./env/lib/python2.7/site-packages/pycrypto-2.6.1-py2.7.egg-info"]
zip_includes=["./env/lib/python2.7/"]




build_exe_options = {"packages": ["paramiko","wsgiref","argparse","ecdsa"],"zip_includes":zip_includes}
# GUI applications require a different base on Windows (the default is for a
# console application).

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Executor",
        version = "0.2",
        description = "Will execute command/ copy files to remote machine ",
        options = {"build_exe": build_exe_options},
        executables = [Executable("StartExecutor.py", base=base,targetName = "Executor",compress= True,copyDependentFiles = True)])