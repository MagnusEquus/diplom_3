from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators
from pages.login_page import LoginPage


class MainPage:

    account_link_button = [By.XPATH, locators.account_link_xpath]

    def __init__(self, driver):
        self.driver = driver

    def click_account_button(self):
        self.driver.find_element(*self.account_link_button).click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(LoginPage.restore_pass_button))
