import time

import pytest
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.item_page import Item_page
from pages.login_page import Login_page



# @pytest.mark.run(order=3)
def test_buy_product_1():
    driver = webdriver.Chrome()

    print('Start test 1')

    login = Login_page(driver)
    login.authorization()

    ip = Item_page(driver)
    ip.move_to_category()
    ip.click_select_product_1()
    ip.add_to_cart_prod_1()
    ip.click_close_window()

    ip.back_to()
    ip.scroll_to()
    ip.click_select_product_2()
    ip.add_to_cart_prod_2()
    ip.click_close_window()
    ip.click_cart()




    print("Finish test 1")
    time.sleep(5)
    driver.quit()
