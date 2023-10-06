import re

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.item_page import Item_page
from selenium import webdriver


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS
    order_button = "//a[@id='startOrder']"
    price_product_1 = "//tbody//following-sibling::tr[1]//following-sibling::span[@class='price']"
    price_product_2 = "//tbody//following-sibling::tr[2]//following-sibling::span[@class='price']"
    price_product_1_total = "//tbody//following-sibling::tr[1]//following-sibling::span[@class='ajaxtotal price']"
    price_product_2_total = "//tbody//following-sibling::tr[2]//following-sibling::span[@class='ajaxtotal price']"
    total_sum = "//span[@class='TotalSum']"

    # GETTERS
    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))
    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1)))
    def get_price_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_2)))
    def get_price_product_1_total(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1_total)))
    def get_price_product_2_total(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_2_total)))
    def get_total_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_sum)))

    # ACTIONS
    def click_order_button(self):
        self.get_order_button().click()
        print("Нажали перейти к оформлению")

    def assert_sum(self):
        a = float(re.sub("[^0-9.]", "", self.get_price_product_1().text) + re.sub("[^0-9.]", "", self.get_price_product_2().text))
        assert a == float(re.sub("[^0-9.]", "", self.get_total_sum().text))
        print("Сумма товаров совпадает с итогом")


    # METHODS
    def assert_product_1_between_main_and_cart(self):
        driver = webdriver.Chrome()
        ip = Item_page(driver)
        self.assert_value_between_elements(ip.get_price_txt(),re.sub("[^0-9.]", "", self.get_price_product_1().text))
        print("Цена товара 1 на главной странице совпадает с ценой в корзине")

    def assert_product_2_between_main_and_cart(self):
        driver = webdriver.Chrome()
        ip = Item_page(driver)
        self.assert_value_between_elements(ip.get_price_txt(), re.sub("[^0-9.]", "", self.get_price_product_2().text))
        print("Цена товара 2 на главной странице совпадает с ценой в корзине")

    def assert_method_in_cart(self):
        self.assert_word(self.get_price_product_1(), re.sub("[^0-9.]", "", self.get_price_product_1_total().text))
        self.assert_word(self.get_price_product_2(), re.sub("[^0-9.]", "", self.get_price_product_2_total().text))
        self.assert_sum()

    # METHODS
    def assert_product_1(self):
        self.assert_product_1_between_main_and_cart()

    def assert_product_2(self):
        self.assert_product_2_between_main_and_cart()

    def start_order(self):
        self.click_order_button()


