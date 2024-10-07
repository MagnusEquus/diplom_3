from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
import locators


class OrderHistoryPage(BasePage):

    order_number_by_order_count = [By.XPATH, locators.ORDER_ORDER_NUMBER_BY_ORDER_COUNT_XPATH]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Получаем номер заказа из списка по его порядковому номеру')
    def get_order_number_by_count(self, count):
        order = self.get_order_by_count(count)
        return order.text

    @allure.step('Получаем заказ из списка по его порядковому номеру')
    def get_order_by_count(self, count):
        return super().variable_locator(self.order_number_by_order_count, 'ORDERCOUNT', count)
