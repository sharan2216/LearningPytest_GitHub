import pytest


@pytest.mark.skip
def testLogin():
    print("Login successful")


@pytest.mark.regression
def testLogoff():
    print("Logoff successful")


@pytest.mark.sanity
def testCalculation():
    assert 2 + 2 == 4


@pytest.mark.xfail("will test it later")
def testCalculation1():
    assert 2 + 2 == 4
