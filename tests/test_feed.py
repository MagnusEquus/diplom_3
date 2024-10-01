import time
import helpers
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.order_history_page import OrderHistoryPage
import allure
import locators


class TestFeed:

    def test_order_popup_opened(self, driver):
        driver.get(locators.feed_url)
        page = FeedPage(driver)
        page.open_first_order()
        assert page.popup_is_opened()

    def test_orders_in_profile_visible_in_feed(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.main_url)
        page = MainPage(driver)
        time.sleep(1)
        page.add_first_bun()
        page.make_an_order()

        driver.get(locators.main_url)
        page.click_account_button()

        page = ProfilePage(driver)
        page.click_order_history()

        page = OrderHistoryPage(driver)
        order_number = page.get_first_order_number()

        driver.get(locators.feed_url)
        page = FeedPage(driver)
        assert page.check_if_order_is_in_list(order_number)

    def test_today_orders_counter_increases(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.feed_url)
        page = FeedPage(driver)
        old_value = page.get_today_orders_count()

        driver.get(locators.main_url)
        page = MainPage(driver)
        time.sleep(1)
        page.add_first_bun()
        page.make_an_order()

        driver.get(locators.feed_url)
        page = FeedPage(driver)
        new_value = page.get_today_orders_count()
        assert new_value > old_value

    def test_overall_orders_counter_increases(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.feed_url)
        page = FeedPage(driver)
        old_value = page.get_overall_orders_count()

        driver.get(locators.main_url)
        page = MainPage(driver)
        time.sleep(1)
        page.add_first_bun()
        page.make_an_order()

        driver.get(locators.feed_url)
        page = FeedPage(driver)
        new_value = page.get_overall_orders_count()
        assert new_value > old_value

    def test_new_orders_are_in_progress(self, driver, user):
        helpers.login_user(driver, user['email'], user['password'])
        driver.get(locators.main_url)
        page = MainPage(driver)
        time.sleep(1)
        page.add_first_bun()
        page.make_an_order()

        driver.get(locators.main_url)
        page.click_account_button()

        page = ProfilePage(driver)
        page.click_order_history()

        page = OrderHistoryPage(driver)
        order_number = page.get_first_order_number()

        driver.get(locators.feed_url)
        page = FeedPage(driver)
        assert page.check_if_order_in_progress(order_number)
