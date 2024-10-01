from selenium.webdriver.common.by import By
import allure
import locators


class ResetPassPage:

    new_pass_input = [By.XPATH, locators.input_new_pass_xpath]
    show_pass_button = [By.XPATH, locators.new_pass_show_xpath]
    new_pass_input_parent = [By.XPATH, locators.new_pass_input_parent_xpath]

    def __init__(self, driver):
        self.driver = driver

    def click_show_pass(self):
        self.driver.find_element(*self.show_pass_button).click()

    def check_if_password_input_is_active(self):
        input_status = self.driver.find_element(*self.new_pass_input_parent).get_attribute("class")
        return 'input_status_active' in input_status
