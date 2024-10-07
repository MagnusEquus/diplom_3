import helpers
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_history_page import OrderHistoryPage
import allure
import locators
import data


class TestFeed:

    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    @allure.description('Заходим на страницу со списком заказов, открываем первый в списке, проверяем что открылось описание')
    def test_order_popup_opened(self, driver):
        driver.get(locators.FEED_URL)
        page = FeedPage(driver)
        page.open_first_order()
        assert page.popup_is_opened()

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    @allure.description('Авторизируемся, делаем заказ, смотрим что он появился у пользователя в профиле')
    def test_orders_in_profile_visible_in_feed(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        page.add_ingredient_by_name(data.INGREDIENT)
        page.make_an_order()

        driver.get(locators.MAIN_URL)
        page.click_account_button()

        page = ProfilePage(driver)
        page.click_order_history()

        page = OrderHistoryPage(driver)
        order_number = page.get_order_number_by_count(1)

        driver.get(locators.FEED_URL)
        page = FeedPage(driver)
        assert page.check_if_order_is_in_list(order_number)

    @allure.title('при создании нового заказа счётчик Выполнено за всё сегодня увеличивается')
    @allure.description('Авторизируемся, создаем заказ, проверяем что увеличился счетчик заказов за сегодня')
    def test_today_orders_counter_increases(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.FEED_URL)
        page = FeedPage(driver)
        old_value = page.get_today_orders_count()

        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        page.add_ingredient_by_name(data.INGREDIENT)
        page.make_an_order()

        driver.get(locators.FEED_URL)
        page = FeedPage(driver)
        new_value = page.get_today_orders_count()
        assert new_value > old_value

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    @allure.description('Авторизируемся, создаем заказ, проверяем что увеличился счетчик заказов за все время')
    def test_overall_orders_counter_increases(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.FEED_URL)
        page = FeedPage(driver)
        old_value = page.get_overall_orders_count()

        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        page.add_ingredient_by_name(data.INGREDIENT)
        page.make_an_order()

        driver.get(locators.FEED_URL)
        page = FeedPage(driver)
        new_value = page.get_overall_orders_count()
        assert new_value > old_value

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    @allure.description('Оформляем заказ, проверяем что его номер появился в списке заказов в обработке')
    def test_new_orders_are_in_progress(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.MAIN_URL)
        page = MainPage(driver)
        page.add_ingredient_by_name(data.INGREDIENT)
        page.make_an_order()

        driver.get(locators.MAIN_URL)
        page.click_account_button()

        page = ProfilePage(driver)
        page.click_order_history()

        page = OrderHistoryPage(driver)
        order_number = page.get_order_number_by_count(1)

        driver.get(locators.FEED_URL)
        page = FeedPage(driver)
        assert page.check_if_order_in_progress(order_number)
