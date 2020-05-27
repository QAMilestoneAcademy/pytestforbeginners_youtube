from pytest import fixture
from pytest import mark
import json
import time
from selenium import webdriver
my_jsonpath="C:/Pytest_project/GetStarted_1/data/test_data.json"

def load_jsondata(path):
    with open(path) as my_data:
        data=json.load(my_data)
        return data

@fixture(params=load_jsondata(my_jsonpath))
def my_testdata(request):
    test_data=request.param
    return test_data

@fixture(scope="session")
def chrome_browser():
    driver=webdriver.Chrome(executable_path='C:/Selenium/Chromedriver/chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.close()