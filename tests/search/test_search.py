from pytest import mark
flag=0

def test_search_firsttestcase():
    assert 1+2==3

@mark.smoke
def test_search_secondtestcase():
    assert [1,2]==[1,2,3]
    global flag
    flag=1


def test_search_thirdtestcase():
    assert "I am"=="I will run only if previous testcase is passed"