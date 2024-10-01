from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators


class FeedPage:

    first_order = [By.XPATH, locators.feed_first_order_xpath]
    close_order_popup = [By.XPATH, locators.feed_close_order_popup_xpath]
    orders_list = [By.XPATH, locators.feed_order_list_xpath]
    orders_overall_counter = [By.XPATH, locators.feed_orders_overall_xpath]
    orders_today_counter = [By.XPATH, locators.feed_orders_today_xpath]

    def __init__(self, driver):
        self.driver = driver

    def open_first_order(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.first_order))
        self.driver.find_element(*self.first_order).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.close_order_popup))

    def popup_is_opened(self):
        return self.driver.find_element(*self.close_order_popup).is_displayed()

    def check_if_order_is_in_list(self, order_number):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.orders_list))
        list = self.driver.find_element(*self.orders_list)
        list_size = len(list.size)
        for i in range(1, list_size + 1):
            current_order_locator = [By.XPATH, locators.feed_order_number_xpath.replace('ELEMENTNUMBER', str(i))]
            current_order_number = self.driver.find_element(*current_order_locator).text
            if current_order_number == order_number:
                return True

    def get_today_orders_count(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.orders_today_counter))
        return self.driver.find_element(*self.orders_today_counter).text

    def get_overall_orders_count(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.orders_overall_counter))
        return self.driver.find_element(*self.orders_overall_counter).text

    def check_if_order_in_progress(self, order_number):
        order_number = str(order_number).replace('#0', '')
        order_locator = locators.feed_ordernumber_in_progress_xpath.replace('ORDERNUMBER', order_number)
        order_in_progress = [By.XPATH, order_locator]
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(order_in_progress))
        return '0' + str(order_number) == self.driver.find_element(*order_in_progress).text
