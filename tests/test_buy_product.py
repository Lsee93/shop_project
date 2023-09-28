import time

import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver

from pages.cart_page import Cart_page
from pages.item_page import Item_page
from pages.login_page import Login_page
from pages.order_page import Order_page


# @pytest.mark.run(order=3)
def test_buy_product_1():
    driver = webdriver.Chrome()

    print('Start test 1')

    login = Login_page(driver)
    login.authorization()

    ip = Item_page(driver)
    ip.choose_category()
    ip.filter_item()
    ip.select_products_1()
    ip.back_to()
    ip.select_products_2()

    ip.click_cart()

    cp = Cart_page(driver)
    cp.start_order()
    op = Order_page(driver)
    op.input_information()

    print("Finish test 1")
    time.sleep(5)
    driver.quit()
