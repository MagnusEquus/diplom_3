from pages.login_page import LoginPage
from pages.forgot_pass_page import ForgotPassPage
from pages.reset_pass_page import ResetPassPage
import allure
import locators
import data


class TestForgotPass:

    def test_redirect_to_forgot_pass_page(self, driver):
        driver.get(locators.login_url)
        page = LoginPage(driver)
        page.goto_forgot_pass_page()
        assert driver.current_url == locators.forgot_password_url

    def test_reset_pass(self, driver):
        driver.get(locators.forgot_password_url)
        page = ForgotPassPage(driver)
        page.fill_mail(data.email)
        page.click_restore_pass()

    def test_input_active(self, driver):
        driver.get(locators.reset_password_url)
        page = ForgotPassPage(driver)
        page.fill_mail(data.email)
        page.click_restore_pass()
        page = ResetPassPage(driver)
        # time.sleep(3)
        page.click_show_pass()
        assert page.check_if_password_input_is_active()
