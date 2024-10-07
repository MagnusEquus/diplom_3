import pytest
import helpers
from pages.profile_page import ProfilePage
from pages.main_page import MainPage
import allure
import locators


class TestAccount:

    @allure.title('переход по клику на «Личный кабинет»')
    @allure.description('Жмем кнопку аккаунта, смотрим что кидает на страницу логина')
    def test_redirect_to_account(self, driver):
        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        page.click_account_button()
        assert driver.current_url == locators.LOGIN_URL

    @allure.title('переход в раздел «История заказов»')
    @allure.description('Логинимся, смотрим что в профиле можно перейти в историю заказов')
    def test_goto_order_history(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        page.click_account_button()
        page = ProfilePage(driver)
        page.click_order_history()
        assert driver.current_url == locators.ORDER_HISTORY_URL

    @allure.title('выход из аккаунта')
    @allure.description('В профиле жмем выход из аккаунта, смотрим что при следующем клике на иконку аккаунта кинет опять нам страницу логина')
    def test_logging_out(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        page.click_account_button()
        page = ProfilePage(driver)
        page.click_logout()
        assert driver.current_url == locators.LOGIN_URL
