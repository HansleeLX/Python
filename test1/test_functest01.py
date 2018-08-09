import sys
import os
o_path = os.path.abspath(os.path.dirname(os.getcwd()))
sys.path.append(o_path)
from testpython import functest

def functest_test01():
    functest.functest()
    return
