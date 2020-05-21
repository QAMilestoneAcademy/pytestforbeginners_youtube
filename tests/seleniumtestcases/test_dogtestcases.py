from pytest import fixture
from pytest import mark
import time
from selenium import webdriver

#https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=DOG

# @fixture(scope="module")
# def chrome_browser():
#     driver=webdriver.Chrome(executable_path='C:/Selenium/Chromedriver/chromedriver.exe')
#     driver.maximize_window()
#     yield driver
#     driver.close()
@mark.selenium_example
def test_viewproductlist_dog(chrome_browser):
    driver=chrome_browser
    driver.get("https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=DOGS")
    time.sleep(5)
    print(driver.title)

@mark.selenium_example
def test_viewproduct_dog(chrome_browser):
    driver = chrome_browser
    driver.find_element_by_link_text('K9-BD-01').click()
    time.sleep(10)
