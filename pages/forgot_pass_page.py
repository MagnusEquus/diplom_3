from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
import allure
import locators
from pages.reset_pass_page import ResetPassPage


class ForgotPassPage(BasePage):

    restore_button = [By.XPATH, locators.RESTORE_PASS_BUTTON_XPATH]
    reset_input = [By.XPATH, locators.RESET_MAIL_INPUT_XPATH]

    def __init__(self, driver):
        super().__init__(driver)

    def fill_mail(self, mail):
        self.driver.find_element(*self.reset_input).click()
        self.driver.find_element(*self.reset_input).send_keys(mail)

    def click_restore_pass(self):
        self.redirect(self.restore_button, ResetPassPage.new_pass_input)

