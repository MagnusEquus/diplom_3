import time

import pytest

import helpers
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
import allure
import locators


class TestAccount:

    @pytest.mark.skip
    def test_redirect_to_account(self, driver):
        driver.get(locators.main_url)
        page = MainPage(driver)
        page.click_account_button()
        assert driver.current_url == locators.login_url

    @pytest.mark.skip
    def test_goto_order_history(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.main_url)
        page = MainPage(driver)
        page.click_account_button()
        page = ProfilePage(driver)
        page.click_order_history()
        assert driver.current_url == locators.order_history_url

    def test_logging_out(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.main_url)
        page = MainPage(driver)
        page.click_account_button()
        page = ProfilePage(driver)
        page.click_logout()
        assert driver.current_url == locators.login_url
