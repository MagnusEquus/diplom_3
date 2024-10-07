import data
import helpers
from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure
import locators


class TestMainFunctional:

    @allure.title('переход по клику на «Конструктор»')
    @allure.description('Со страницы логина жмем на кнопку конструктора, проверяем новый урл')
    def test_goto_constructor(self, driver):
        driver.get(locators.LOGIN_URL)
        page = LoginPage(driver)
        page.click_constructor_button()
        assert driver.current_url == locators.MAIN_URL

    @allure.title('переход по клику на «Лента заказов»')
    @allure.description('Со страницы конструктора жмем на кнопку лента заказов, проверяем новый урл')
    def test_goto_feed(self, driver):
        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        page.click_feed_button()
        assert driver.current_url == locators.FEED_URL

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    @allure.description('Кликаем на первый ингредиент в списке, проверяем что открылось окно с деталями')
    def test_ingredient_description(self, driver):
        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        page.click_ingredient_by_name(data.INGREDIENT)
        assert page.check_ingredient_description_visible()

    @allure.title('всплывающее окно закрывается кликом по крестику')
    @allure.description('Кликаем на первый ингредиент в списке, кликаем на крестик в появившимся окне, проверяем что окно с деталями закрылось')
    def test_popup_close(self, driver):
        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        page.click_ingredient_by_name(data.INGREDIENT)
        page.click_close_ingredient_popup()
        assert not page.check_ingredient_description_visible()

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    @allure.description('Перетаскиваем ингредиент в бургер, проверяем что у него увеличилось значение счетчика')
    def test_adding_ingredient_increases_counter(self, driver):
        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        value1 = page.get_ingredient_counter_value_by_name(data.INGREDIENT)
        page.add_ingredient_by_name(data.INGREDIENT)
        value2 = page.get_ingredient_counter_value_by_name(data.INGREDIENT)
        assert int(value2) > int(value1)

    @allure.title('залогиненный пользователь может оформить заказ')
    @allure.description('Логинимся, проверяем что на экране конструктора доступна кнопка оформления')
    def test_authorized_user_can_order(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        assert page.check_if_ordering_is_available()
