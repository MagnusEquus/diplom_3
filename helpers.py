import requests
from pages.login_page import LoginPage
from pages.main_page import MainPage
import allure
import locators
import data
import time


@allure.step('Создаем юзера с задаными данными')
def register_user(email, password, name):
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    requests.post(data.url_register, data=payload)


@allure.step('Удаляем юзера по почте и паролю')
def delete_user(email, password):
    token = get_user_token(email, password)
    requests.delete(data.url_user, headers={'Authorization': token})


@allure.step('Получаем токен юзера по почте и паролю')
def get_user_token(email, password):
    payload = {
        "email": email,
        "password": password
    }

    response = requests.post(data.url_login, data=payload)
    if response.status_code != 401:
        token = response.json()["accessToken"]
        return token


def login_user(driver, email, password):
    driver.get(locators.main_url)
    page = MainPage(driver)
    page.click_account_button()
    page = LoginPage(driver)
    page.login_into_account(email, password)
    time.sleep(0.3)
