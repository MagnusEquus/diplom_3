from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
import locators


class ResetPassPage(BasePage):

    new_pass_input = [By.XPATH, locators.INPUT_NEW_PASS_XPATH]
    show_pass_button = [By.XPATH, locators.NEW_PASS_SHOW_XPATH]
    new_pass_input_parent = [By.XPATH, locators.NEW_PATH_INPUT_PARENT_XPATH]

    def __init__(self, driver):
        super().__init__(driver)

    def click_show_pass(self):
        self.driver.find_element(*self.show_pass_button).click()

    def check_if_password_input_is_active(self):
        input_status = self.driver.find_element(*self.new_pass_input_parent).get_attribute("class")
        return 'input_status_active' in input_status
