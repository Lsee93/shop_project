from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Order_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    region = "//input[@id='quickDeliveryRegion']"
    city = "//input[@id='quickDeliveryCity']"
    address = "//input[@id='quickDeliveryAddressStreet']"
    zip_code = "//input[@id='quickDeliveryZipCode']"
    comment = "//input[@id='quickDeliveryComment']"
    select_payment = "//select[@class='paymentSelect input validInput']"
    chosen_payment = "//option[@id='quickPaymentId193279_195902']"
    order_button = "//button[@title='Оформить заказ']"

    # Getters

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
        print("Input region")

    def input_city(self, city_name):
        self.get_city().send_keys(city_name)
        print("Input city name")

    def input_address(self, address_name):
        self.get_address().send_keys(address_name)
        print("Input address")

    def input_zip_code(self, code):
        self.get_zip_code().send_keys(code)
        print("Input code")

    def input_comment(self, comm):
        self.get_comment().send_keys(comm)
        print("Input comment")

    def click_select_payment(self):
        self.get_select_payment().click()
        print("Click select payment")

    def click_chosen_payment(self):
        self.get_chosen_payment().click()
        print("Click chosen payment")

    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")

    # Methods
    def input_information(self):
        self.get_current_url()
        self.input_first_name("Ivan")
        self.input_last_name("Ivanov")
        self.input_postal_code("1234")
        self.click_continue_button()
