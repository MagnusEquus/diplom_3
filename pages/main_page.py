from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import allure
import locators


class MainPage:

    account_link_button = [By.XPATH, locators.account_link_xpath]
    feed_link_button = [By.XPATH, locators.feed_link_button_xpath]
    first_ingredient = [By.XPATH, locators.first_ingredient_xpath]
    ingredient_popup = [By.XPATH, locators.ingredient_popup_xpath]
    ingredient_popup_close = [By.XPATH, locators.ingredient_popup_close_xpath]
    ingredient_counter_value = [By.XPATH, locators.ingredient_counter_value_xpath]
    first_bun_drop = [By.XPATH, locators.constructor_bun_first_dragndrop_xpath]
    order_button = [By.XPATH, locators.order_button_xpath]
    close_new_order_popup = [By.XPATH, locators.order_close_new_order_popup_xpath]

    def __init__(self, driver):
        self.driver = driver

    def click_account_button(self):
        self.driver.find_element(*self.account_link_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.account_link_button))

    def click_feed_button(self):
        self.driver.find_element(*self.feed_link_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.account_link_button))

    def click_first_ingredient(self):
        self.driver.find_element(*self.first_ingredient).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.ingredient_popup))

    def check_ingredient_description_visible(self):
        state = self.driver.find_element(*self.ingredient_popup).is_displayed()
        return state

    def click_close_ingredient_popup(self):
        self.driver.find_element(*self.ingredient_popup_close).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(self.ingredient_popup))

    def get_first_ingredient_counter_value(self):
        return self.driver.find_element(*self.ingredient_counter_value).text

    def add_first_bun(self):
        action = ActionChains(self.driver)
        bun = self.driver.find_element(*self.first_ingredient)
        target = self.driver.find_element(*self.first_bun_drop)
        action.drag_and_drop(bun, target).perform()

    def check_if_ordering_is_available(self):
        return self.driver.find_element(*self.order_button).is_displayed()

    def make_an_order(self):
        self.driver.find_element(*self.order_button).click()

    def close_new_order_popup(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(*self.close_new_order_popup))
        self.driver.find_element(*self.close_new_order_popup).click()

