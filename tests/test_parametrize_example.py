from pytest import mark

@mark.param_testcase
@mark.parametrize("product_name,product_color",[("shoe","black"),("car","red"),("mobile","golden"),("tv","silver")])
def test_product_detail(product_name,product_color):
    print(f"I am {product_name} with {product_color}")

# @mark.param_testcase
# @mark.parametrize("number",[1,0,100,-4])
# def test_first(number):
#     assert number > 0