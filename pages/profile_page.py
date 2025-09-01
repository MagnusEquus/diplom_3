from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage
import allure
import locators


class ProfilePage(BasePage):

    order_history_button = [By.XPATH, locators.ORDER_HISTORY_BUTTON_XPATH]
    logout_button = [By.XPATH, locators.LOGOUT_BUTTON_XPATH]

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переходим на страницу с историей заказов')
    def click_order_history(self):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(self.order_history_button))
        self.driver.find_element(*self.order_history_button).click()

    @allure.step('Нажимаем на выход из аккаунта')
    def click_logout(self):
        from pages.login_page import LoginPage
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.logout_button))
        self.driver.find_element(*self.logout_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(LoginPage.login_button))
