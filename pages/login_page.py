from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators
from pages.forgot_pass_page import ForgotPassPage
from pages.main_page import MainPage


class LoginPage:

    restore_pass_button = [By.XPATH, locators.restore_pass_xpath]
    email_input = [By.XPATH, locators.input_login_email_xpath]
    password_input = [By.XPATH, locators.input_login_pass_xpath]
    login_button = [By.XPATH, locators.login_button_xpath]
    constructor_link_button = [By.XPATH, locators.constructor_button_xpath]

    def __init__(self, driver):
        self.driver = driver

    def goto_forgot_pass_page(self):
        self.driver.find_element(*self.restore_pass_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ForgotPassPage.restore_button))

    def login_into_account(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.account_link_button))

    def click_constructor_button(self):
        self.driver.find_element(*self.constructor_link_button).click()
