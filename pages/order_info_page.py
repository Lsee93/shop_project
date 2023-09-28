from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.order_page import Order_page
import re


class Order_info_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # LOCATORS
    order_number_title = "//h1[@class='title']"
    order_number = "//table[@class='table-box table-striped']//following-sibling::tr[1]//following-sibling::td[@class='cell2']"
    all_sum = "//span[@class='num']"
    confirmed_person = "//table[@class='table-box table-striped']//following-sibling::tr[3]//following-sibling::td[@class='cell2']"
    confirmed_phone_number = "//table[@class='table-box table-striped']//following-sibling::tr[4]//following-sibling::td[@class='cell2']"
    confirmed_email = "//table[@class='table-box table-striped']//following-sibling::tr[5]//following-sibling::td[@class='cell2']"
    confirmed_zip_code = "//table[@class='table-box table-striped']//following-sibling::tr[6]//following-sibling::td[@class='cell2']"
    confirmed_region = "//table[@class='table-box table-striped']//following-sibling::tr[7]//following-sibling::td[@class='cell2']"
    confirmed_city = "//table[@class='table-box table-striped']//following-sibling::tr[8]//following-sibling::td[@class='cell2']"
    confirmed_address = "//table[@class='table-box table-striped']//following-sibling::tr[9]//following-sibling::td[@class='cell2']"
    confirmed_comm = "//table[@class='table-box table-striped']//following-sibling::tr[10]//following-sibling::td[@class='cell2']"
    final_price = "//table[@class='table-box hbf']//following-sibling::tfoot//following-sibling::tr//following-sibling::td[2]//span[@class='num']"
    back_to_main_page = "//div[@class='buttons']"

    # GETTERS

    def get_order_number_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_number_title)))
    def get_order_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_number)))
    def get_all_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.all_sum)))
    def get_confirmed_person(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmed_person)))
    def get_confirmed_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmed_phone_number)))
    def get_confirmed_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmed_email)))
    def get_confirmed_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmed_zip_code)))
    def get_confirmed_region(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmed_region)))
    def get_confirmed_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmed_city)))
    def get_confirmed_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmed_address)))
    def get_confirmed_comm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirmed_comm)))
    def get_back_to_main_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.back_to_main_page)))
    def get_final_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.final_price)))

    # ACTIONS
    def txt_order_number_title(self):
        self.get_order_number_title().text()
        print("Получили номер заказа в заголовке")
    def txt_order_number(self):
        self.get_order_number().text()
        print("Получили номер заказа")

    def txt_all_sum(self):
        self.get_all_sum().text()
        print("Получили сумму")

    def txt_confirmed_person(self):
        self.get_confirmed_person().text()
        print("Получили ФИО")

    def txt_confirmed_phone_number(self):
        self.get_confirmed_phone_number().text()
        print("Получили номер телефона")

    def txt_confirmed_email(self):
        self.get_confirmed_email().text()
        print("Получили почту")

    def txt_confirmed_zip_code(self):
        self.get_confirmed_zip_code().text()
        print("Получили индекс")

    def txt_confirmed_region(self):
        self.get_confirmed_region().text()
        print("Получили область")
    def txt_confirmed_city(self):
        self.get_confirmed_city().text()
        print("Получили город")
    def txt_confirmed_address(self):
        self.get_confirmed_address().text()
        print("Получили адрес")

    def txt_confirmed_comm(self):
        self.get_confirmed_comm().text()
        print("Получили комментарий")

    def txt_final_price(self):
        self.get_final_price().text()
        print("Получили финальную цену")

    def click_back_to_main_page(self):
        self.get_back_to_main_page().click()
        print("Нажали на кнопку Перейти на главную")

    # METHODS
    def input_information(self):
        self.get_current_url()
        self.assert_word(self.get_order_number(), "Московская область")
        self.assert_word(self.get_confirmed_region(), "Московская область")
        self.assert_word(self.get_confirmed_city(), "Москва")
        self.assert_word(self.get_confirmed_address(), "ул. Московская, д.999/9")
        self.assert_word(self.get_confirmed_zip_code(), "12345")
        self.assert_word(self.get_confirmed_comm(), "Тестовый комментарий")
        self.assert_word(self.get_order_number(), re.sub("[^0-9.]", "", self.txt_order_number_title))




