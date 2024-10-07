from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
import allure
import locators
from pages.forgot_pass_page import ForgotPassPage
from pages.main_page import MainPage


class LoginPage(BasePage):

    restore_pass_button = [By.XPATH, locators.RESTORE_PASS_XPATH]
    email_input = [By.XPATH, locators.INPUT_LOGIN_EMAIL_XPATH]
    password_input = [By.XPATH, locators.INPUT_LOGIN_PASS_XPATH]
    login_button = [By.XPATH, locators.LOGIN_BUTTON_XPATH]
    constructor_link_button = [By.XPATH, locators.CONSTRUCTOR_BUTTON_XPATH]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переходим на страницу восстановления пароля')
    def goto_forgot_pass_page(self):
        self.redirect(self.restore_pass_button, ForgotPassPage.restore_button)

    @allure.step('Заполняем поля и входим в аккаунт')
    def login_into_account(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPage.first_bun_drop))

    @allure.step('Переходим на страницу с конструктором')
    def click_constructor_button(self):
        self.redirect(self.constructor_link_button, self.feed_link_button)
