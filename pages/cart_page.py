from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    order_button = "//a[@id='startOrder']"

    # Getters
    def get_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.order_button)))

    # Actions
    def click_order_button(self):
        self.get_order_button().click()
        print("Click order button")

    # Methods
    def product_confirmation(self):
        self.get_current_url()
        self.click_order_button()
