from pytest import mark


@mark.product
class ProductTest:

    @mark.smoke
    def test_product_firsttestcase(self):
       assert 1+2==3


    def test_product_secondtestcase(self):
        assert [1,2]==[1,2,3]


    def test_product_thirdtestcase(self):
        assert "I am"=="I am QAMilestone"