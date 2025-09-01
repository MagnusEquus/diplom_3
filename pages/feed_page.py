from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
import allure
import locators


class FeedPage(BasePage):

    order_by_count = [By.XPATH, locators.FEED_ORDER_BY_COUNT_XPATH]
    close_order_popup = [By.XPATH, locators.FEED_CLOSE_ORDER_POPUP_XPATH]
    orders_list = [By.XPATH, locators.FEED_ORDER_LIST_XPATH]
    orders_overall_counter = [By.XPATH, locators.FEED_ORDERS_OVERALL_XPATH]
    orders_today_counter = [By.XPATH, locators.FEED_ORDERS_TODAY_XPATH]
    current_order_by_count = [By.XPATH, locators.FEED_ORDER_NUMBER_XPATH]
    order_in_progress = [By.XPATH, locators.FEED_ORDERNUMBER_IN_PROGRESS_XPATH]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Открываем первый заказ из списка готовых заказов')
    def open_first_order(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.orders_list))
        order = self.get_order_by_count(1)
        order.click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.close_order_popup))

    @allure.step('Смотрим что открылось окно заказа')
    def popup_is_opened(self):
        return self.driver.find_element(*self.close_order_popup).is_displayed()

    @allure.step('Проходимся по каждому заказу в списке и сверяем номер')
    def check_if_order_is_in_list(self, order_number):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.orders_list))
        list = self.driver.find_element(*self.orders_list)
        list_size = len(list.size)
        for i in range(1, list_size + 1):
            current_order = self.get_feed_order_by_count(i)
            current_order_number = current_order.text
            if current_order_number == order_number:
                return True

    @allure.step('Возвращаем количество заказов за сегодня')
    def get_today_orders_count(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.orders_today_counter))
        return self.driver.find_element(*self.orders_today_counter).text

    @allure.step('Возвращаем количество заказов за все время')
    def get_overall_orders_count(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.orders_overall_counter))
        return self.driver.find_element(*self.orders_overall_counter).text

    @allure.step('Проверяем что заказ с таким номером есть в списке')
    def check_if_order_in_progress(self, order_number):
        order_number = str(order_number).replace('#0', '')
        order_in_progress = self.get_order_in_progress_by_number(order_number)
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of(order_in_progress))
        return '0' + str(order_number) == order_in_progress.text

    @allure.step('Получаем заказ из списка готовых заказов по его порядковому номеру')
    def get_order_by_count(self, number):
        order = super().variable_locator(self.order_by_count, 'ORDERCOUNT', number)
        return order

    @allure.step('Получаем номер заказа из элемента списка по порядковому номеру')
    def get_feed_order_by_count(self, number):
        order = super().variable_locator(self.current_order_by_count, 'ELEMENTNUMBER', number)
        return order

    @allure.step('Получаем заказ из списка готовящихся по номеру заказа')
    def get_order_in_progress_by_number(self, order_number):
        order = super().variable_locator(self.order_in_progress, 'ORDERNUMBER', order_number)
        return order
