from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators
from pages.reset_pass_page import ResetPassPage


class ForgotPassPage:

    restore_button = [By.XPATH, locators.restore_pass_button_xpath]
    reset_input = [By.XPATH, locators.reset_mail_input_xpath]

    def __init__(self, driver):
        self.driver = driver

    def fill_mail(self, mail):
        self.driver.find_element(*self.reset_input).click()
        self.driver.find_element(*self.reset_input).send_keys(mail)

    def click_restore_pass(self):
        self.driver.find_element(*self.restore_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ResetPassPage.new_pass_input))

