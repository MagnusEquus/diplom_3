from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators


class OrderHistoryPage:

    first_order_number = [By.XPATH, locators.order_history_first_order_number_xpath]

    def __init__(self, driver):
        self.driver = driver

    def get_first_order_number(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.first_order_number))
        return self.driver.find_element(*self.first_order_number).text
