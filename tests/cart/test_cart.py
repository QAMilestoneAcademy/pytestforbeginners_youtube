from pytest import mark

@mark.smoke
def test_cart_firsttestcase():
    assert 1+2==3

def test_cart_secondtestcase():
    assert [1,2]==[1,2,3]

def test_cart_thirdtestcase():
    assert "I am"=="I am QAMilestone"