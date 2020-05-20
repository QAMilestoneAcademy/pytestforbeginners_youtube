from pytest import fixture
from pytest import mark
import time
from selenium import webdriver

@fixture(scope="session")
def chrome_browser():
    driver=webdriver.Chrome(executable_path='C:/Selenium/Chromedriver/chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.close()