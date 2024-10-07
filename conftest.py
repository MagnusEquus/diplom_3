import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import helpers
import data


@allure.step('Создаем драйвер для кроссбраузерного тестирования')
@pytest.fixture(params=[
    'chrome',
    'firefox'
])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.step('Создаем юзера, выдаем его креды и токен. После - удаляем')
@pytest.fixture
def user():
    helpers.delete_user(data.email, data.password)
    helpers.register_user(data.email, data.password, data.name)
    creds = {
        "email": data.email,
        "password": data.password,
        "name": data.name,
        "token": helpers.get_user_token(data.email, data.password)
    }
    yield creds
    helpers.delete_user(data.email, data.password)
