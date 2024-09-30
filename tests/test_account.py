import pytest
import helpers
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
import allure
import locators
import data


class TestAccount:

    @pytest.mark.skip
    def test_redirect_to_account(self, driver):
        driver.get(locators.main_url)
        page = MainPage(driver)
        page.click_account_button()
        assert driver.current_url == locators.login_url

    def test_goto_order_history(self, driver, user):
        helpers.login_user(user['email'], user['password'])
        page = MainPage(driver)
        page.click_account_button()
        page = ProfilePage
        page.click_order_history()
        assert driver.current_url == locators.order_history_url
