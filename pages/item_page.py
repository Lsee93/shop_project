import time

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
    choose_size_product = "//select[@class='selectBox']"
    select_size_product = "//option[@value='3113124']"
    close_window = "//a[@class='fancybox-item fancybox-close']"
    cart = "//span[@class='header-toolsIcon _cart']"
    filter_price = "//input[@id='goods-filter-max-price']"
    button_show = "//button[@title='Показать']"
    show_all_colors = "//span[@class='filter-moreText pseudo-link']"
    color_checkbox_1 = "//label[@for='filterAttrVal9166786']"
    color_checkbox_2 = "//label[@for='filterAttrVal15222981']"
    size = "//label[@for='filterPropVal3113124']"

    # GETTERS
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

    def get_choose_size_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_size_product)))

    def get_select_size_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size_product)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))
    def get_close_window(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.close_window)))
    def get_filter_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price)))

    def get_button_show(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_show)))
    def get_show_all_colors(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.show_all_colors)))
    def get_color_checkbox_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_checkbox_1)))
    def get_color_checkbox_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.color_checkbox_2)))
    def get_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size)))


    # ACTIONS
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

    def click_size(self):
        self.get_size().click()
        print("Выбрали размер")

    def click_show_all_colors(self):
        self.get_show_all_colors().click()
        print("Раскрыли все цвета в фильтре")

    def click_color_checkbox_1(self):
        self.get_color_checkbox_1().click()
        print("Выбрали первый цвет")

    def click_color_checkbox_2(self):
        self.get_color_checkbox_2().click()
        print("Выбрали второй цвет")

    def input_price(self, price):
        self.get_filter_price().clear()
        self.get_filter_price().send_keys(price)
        print("Ввели максимальную сумму")
        time.sleep(10)

    def click_button_show(self):
        self.get_button_show().click()
        print("Нажали кнопку применить")

    def click_choose_size_product(self):
        self.get_choose_size_product().click()
        print("Нажали на поле с размером")

    def click_select_size_product(self):
        self.get_select_size_product().click()
        print("Выбрали размер")

    # METHODS
    def choose_category(self):
        self.get_current_url()
        self.move_to_item()
        self.move_to_catalog()
        self.move_to_category()

    def filter_item(self):
        self.click_size()
        self.click_show_all_colors()
        self.click_color_checkbox_1()
        self.click_show_all_colors()
        self.click_color_checkbox_2()
        self.input_price("1840")
        self.click_button_show()

    def select_products_1(self):
        self.click_select_product_1()
        self.click_choose_size_product()
        self.click_select_size_product()
        self.add_to_cart_prod_1()
        self.click_close_window()

    def select_products_2(self):
        self.click_select_product_2()
        self.click_choose_size_product()
        self.click_select_size_product()
        self.add_to_cart_prod_2()
        self.click_close_window()
