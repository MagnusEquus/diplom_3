from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
import allure
import locators


class MainPage(BasePage):

    ingredient_by_name = [By.XPATH, locators.INGREDIENT_BY_NAME_XPATH]
    ingredient_popup = [By.XPATH, locators.INGREDIENT_POPUP_XPATH]
    ingredient_popup_close = [By.XPATH, locators.INGREDIENT_POPUP_CLOSE_XPATH]
    ingredient_by_name_counter_value = [By.XPATH, locators.INGREDIENT_BY_NAME_COUNTER_XPATH]
    first_bun_drop = [By.XPATH, locators.CONSTRUCTOR_BUN_FIRST_DRAGNDROP_XPATH]
    order_button = [By.XPATH, locators.ORDER_BUTTON_XPATH]
    close_new_order_popup_button = [By.XPATH, locators.ORDER_CLOSE_NEW_ORDER_POPUP_XPATH]

    def __init__(self, driver):
        super().__init__(driver)

    def click_account_button(self):
        self.redirect(self.account_link_button, self.account_link_button)

    def click_feed_button(self):
        self.redirect(self.feed_link_button, self.account_link_button)

    def click_ingredient_by_name(self, name):
        super().variable_locator(self.ingredient_by_name, 'NAME', name).click()
        # self.driver.find_element(*self.ingredient_by_name).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(self.ingredient_popup))

    def check_ingredient_description_visible(self):
        state = self.driver.find_element(*self.ingredient_popup).is_displayed()
        return state

    def click_close_ingredient_popup(self):
        self.driver.find_element(*self.ingredient_popup_close).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(self.ingredient_popup))

    def get_ingredient_counter_value_by_name(self, name):
        return super().variable_locator(self.ingredient_by_name_counter_value, 'NAME', name).text

    def add_ingredient_by_name(self, name):
        action = ActionChains(self.driver)
        bun = super().variable_locator(self.ingredient_by_name, 'NAME', name)
        target = self.driver.find_element(*self.first_bun_drop)
        action.drag_and_drop(bun, target).perform()

    def check_if_ordering_is_available(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.order_button))
        return self.driver.find_element(*self.order_button).is_displayed()

    def make_an_order(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.order_button))
        self.driver.find_element(*self.order_button).click()

    def close_new_order_popup(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.close_new_order_popup_button))
        self.driver.find_element(*self.close_new_order_popup_button).click()

