import pytest
import sys

def setup():
    print ("Setup test")
 
def teardown():
    print ("Teardown test")

def setup_module(module):
    print ("Setup module")
 
def teardown_module(module):
    print ("Teardown module")
 
def setup_function(function):
    print ("Setup function")
 
def teardown_function(function):
    print ("Teardown function")
 
def test_something_one():
    print("Test 1")
 
def test_something_two():
    print("Test 2")

@pytest.mark.xfail()
def test_xfail():
    assert False
    
@pytest.mark.xfail(
    sys.version.startswith("3"),
    reason="supported only in older Python versions")
def test_xfail_condition():
    assert False

@pytest.mark.xfail()
def test_xfail_fail():
    assert True
