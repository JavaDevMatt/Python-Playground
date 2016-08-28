import sys
sys.path.append('../inner')

from inner import *

def test_for_foo_printer():
    assert foo_returner() == "foo"