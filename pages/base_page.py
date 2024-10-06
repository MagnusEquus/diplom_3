from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators


class BasePage:

    account_link_button = [By.XPATH, locators.ACCOUNT_LINK_XPATH]
    feed_link_button = [By.XPATH, locators.FEED_LINK_BUTTON_XPATH]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('переходим на новую страницу по кнопке и ждем загрузки')
    def redirect(self, button, wait_element):
        self.driver.find_element(*button).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(wait_element))

    def variable_locator(self, locator, variable_name, value):
        locator[1] = locator[1].replace(variable_name, str(value))
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
