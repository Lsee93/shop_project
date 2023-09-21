import time

import pytest
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.login_page import Login_page
import sys


# sys.path.append("C:\\Users\\Ivandaeva\\PycharmProjects\\main_project")

# @pytest.mark.run(order=3)
def test_buy_product_1():
    driver = webdriver.Chrome()

    print('Start test 1')

    login = Login_page(driver)
    login.authorization()


    print("Finish test 1")
    time.sleep(10)
    driver.quit()
