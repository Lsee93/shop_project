import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current URL " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Наименование совпадает")

    def assert_word_between_elements(self, element_1, element_2):
        value_element_1 = element_1.text
        value_element_2 = element_2.text
        assert value_element_1 == value_element_2
        print("Введенные данные совпадают")

    """Method Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = "screenshot" + now_date + '.png'
        self.driver.save_screenshot("C:\\Users\\Ivandaeva\\PycharmProjects\\InternetShop_project\\screen\\" + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Корректный url")


