from pytest import fixture
from pytest import mark


# @fixture(params=["apples","guava","orange"])
# def fruit(request):
#     return request.param
#
# @mark.fixture_sampl1
# def test_fruit(fruit):
#     print(f"I am {fruit}")

@mark.fixture_sampl1
def test_product_detail(my_testdata):
    my_product_name=my_testdata["product_name"]
    my_product_color=my_testdata["product_color"]
    print(f"I am {my_product_name} with {my_product_color} ")
