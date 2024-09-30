from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators
from pages.login_page import LoginPage


class ProfilePage:

    order_history_button = [By.XPATH, locators.order_history_button_xpath]

    def __init__(self, driver):
        self.driver = driver

    def click_order_history(self):
        self.driver.find_element(*self.order_history_button).click()
