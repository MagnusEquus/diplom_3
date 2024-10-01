import time
import helpers
from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure
import locators


class TestMainFunctional:
 
    def test_goto_constructor(self, driver):
        driver.get(locators.login_url)
        page = LoginPage(driver)
        page.click_constructor_button()
        assert driver.current_url == locators.main_url

    def test_goto_feed(self, driver):
        driver.get(locators.main_url)
        page = MainPage(driver)
        page.click_feed_button()
        assert driver.current_url == locators.feed_url

    def test_ingredient_description(self, driver):
        driver.get(locators.main_url)
        page = MainPage(driver)
        page.click_first_ingredient()
        assert page.check_ingredient_description_visible()

    def test_popup_close(self, driver):
        driver.get(locators.main_url)
        page = MainPage(driver)
        page.click_first_ingredient()
        page.click_close_ingredient_popup()
        assert not page.check_ingredient_description_visible()

    def test_adding_ingredient_increases_counter(self, driver):
        driver.get(locators.main_url)
        page = MainPage(driver)
        value1 = page.get_first_ingredient_counter_value()
        page.add_first_bun()
        value2 = page.get_first_ingredient_counter_value()
        assert int(value2) > int(value1)

    def test_authorized_user_can_order(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.main_url)
        page = MainPage(driver)
        time.sleep(2)
        assert page.check_if_ordering_is_available()
