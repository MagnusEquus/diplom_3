from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
import allure
import locators


class OrderHistoryPage(BasePage):

    order_number_by_order_count = [By.XPATH, locators.ORDER_ORDER_NUMBER_BY_ORDER_COUNT_XPATH]

    def __init__(self, driver):
        super().__init__(driver)

    def get_order_number_by_count(self, count):
        order = self.get_order_by_count(count)
        # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(order))
        return order.text

    def get_order_by_count(self, count):
        return super().variable_locator(self.order_number_by_order_count, 'ORDERCOUNT', count)
