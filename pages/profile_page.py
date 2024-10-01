from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators


class ProfilePage:

    order_history_button = [By.XPATH, locators.order_history_button_xpath]
    logout_button = [By.XPATH, locators.logout_button_xpath]

    def __init__(self, driver):
        self.driver = driver

    def click_order_history(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.order_history_button))
        self.driver.find_element(*self.order_history_button).click()

    def click_logout(self):
        from pages.login_page import LoginPage
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.logout_button))
        self.driver.find_element(*self.logout_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(LoginPage.login_button))
