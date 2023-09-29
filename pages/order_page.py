from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Order_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # LOCATORS

    region = "//input[@id='quickDeliveryRegion']"
    city = "//input[@id='quickDeliveryCity']"
    address = "//input[@id='quickDeliveryAddressStreet']"
    zip_code = "//input[@id='quickDeliveryZipCode']"
    comment = "//textarea[@id='quickDeliveryComment']"
    select_payment = "//div[@class='orderStagePaymentList']"
    chosen_payment = "//option[@id='quickPaymentId193279_195902']"
    order_button = "//button[@title='Оформить заказ']"

    # GETTERS
    def get_region(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.region)))
    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))
    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))
    def get_zip_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zip_code)))
    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.comment)))
    def get_select_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_payment)))
    def get_chosen_payment(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.chosen_payment)))
    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    # Actions
    def input_region(self, region_name):
        self.get_region().send_keys(region_name)
        print("Ввели область")

    def input_city(self, city_name):
        self.get_city().send_keys(city_name)
        print("Ввели город")

    def input_address(self, address_name):
        self.get_address().send_keys(address_name)
        print("Ввели адрес")

    def input_zip_code(self, code):
        self.get_zip_code().send_keys(code)
        print("Ввели индекс")

    def input_comment(self, comm):
        self.get_comment().send_keys(comm)
        print("Ввели комментарий")

    def click_select_payment(self):
        self.get_select_payment().click()
        print("Нажали на способ оплаты")

    def click_chosen_payment(self):
        self.get_chosen_payment().click()
        print("Выбрали способ оплаты")

    def click_order_button(self):
        self.get_order_button().click()
        print("Нажали на кнопку оформить заказ")

    # Methods
    def input_information(self):
        self.get_current_url()
        self.input_region("Московская область")
        self.input_city("Москва")
        self.input_address("ул. Московская, д.999/9")
        self.input_zip_code("12345")
        self.input_comment("Тестовый комментарий")
        self.click_select_payment()
        self.click_chosen_payment()
        self.click_order_button()
