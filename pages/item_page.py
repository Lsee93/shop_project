from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Item_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    item_button = "//span[@class='header-catalogBtn unselectable']"

    select_catalog = "//a[@title='Трикотаж']"
    select_category = "//a[@title='Платья']"

    select_product_1 = "//a[@title='Платье 24652 [красный]']"
    select_product_2 = "//a[@title='Платье 59208 [молочный]']"
    add_to_cart_product_1 = "//button[@title='Положить «Платье 24652 [красный]» в корзину']"
    add_to_cart_product_2 = "//button[@title='Положить «Платье 59208 [молочный]» в корзину']"
    close_window = "//a[@class='fancybox-item fancybox-close']"
    cart = "//span[@class='header-toolsIcon _cart']"


    # Getters

    def get_item_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.item_button)))

    def get_select_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_catalog)))

    def get_select_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_category)))

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_cart_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_1)))

    def get_cart_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_product_2)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_close_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_window)))


    # Actions

    def move_to_item(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_item_button())
        actions.perform()
        print("Навели курсор на список товаров")

    def move_to_catalog(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.get_select_catalog())
        actions.perform()
        print("Навели курсор на категорию в каталоге")

    def move_to_category(self):
        actions = ActionChains(self.driver)
        actions.click(self.get_select_category())
        actions.perform()
        print("Нажали на определенную категорию")

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Выбрали продукт 1")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Выбрали продукт 2")

    def back_to(self):
        self.driver.back()
        print("Вернулись назад")

    def scroll_to(self):
        self.driver.execute_script("window.scrollTo(0, 1500)")
        print("Проскролили")

    def add_to_cart_prod_1(self):
        self.get_cart_product_1().click()
        print("Добавили в корзину продукт 1")

    def add_to_cart_prod_2(self):
        self.get_cart_product_2().click()
        print("Добавили в корзину продукт 2")

    def click_cart(self):
        self.get_cart().click()
        print("Открыли корзину")

    def click_close_window(self):
        self.get_close_window().click()
        print("Закрыли модальное окно")

    # Methods
    def select_products_1(self):
        self.get_current_url()
        self.move_to_item()
        self.move_to_catalog()
        self.move_to_category()
        self.click_select_product_1()

    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()
