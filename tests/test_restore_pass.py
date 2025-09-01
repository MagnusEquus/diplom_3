from pages.login_page import LoginPage
from pages.forgot_pass_page import ForgotPassPage
from pages.reset_pass_page import ResetPassPage
import allure
import locators
import data


class TestForgotPass:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    @allure.description('На странице логина жмем восстановление пароля, проверяем новый урл')
    def test_redirect_to_forgot_pass_page(self, driver):
        driver.get(locators.LOGIN_URL)
        page = LoginPage(driver)
        page.goto_forgot_pass_page()
        assert driver.current_url == locators.FORGOT_PASSWORD_URL

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    @allure.description('На странице восстановления пароля вводим почту, жмем кнопку. Смотрим что перешло на следующую страницу')
    def test_reset_pass(self, driver):
        driver.get(locators.FORGOT_PASSWORD_URL)
        page = ForgotPassPage(driver)
        page.fill_mail(data.email)
        page.click_restore_pass()
        assert driver.current_url == locators.RESET_PASSWORD_URL

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    @allure.description('Переходим на страницу восстановления пароля, вводим его, смотрим что после переключения отображения поле становится активным')
    def test_input_active(self, driver):
        driver.get(locators.RESET_PASSWORD_URL)
        page = ForgotPassPage(driver)
        page.fill_mail(data.email)
        page.click_restore_pass()
        page = ResetPassPage(driver)
        page.click_show_pass()
        assert page.check_if_password_input_is_active()
