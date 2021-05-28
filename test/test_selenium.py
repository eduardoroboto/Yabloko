from selenium.webdriver import Firefox
from pytest import fixture
from test_flask import flask_test


@fixture
def browser(flask_test):
    browser = Firefox()
    yield browser
    browser.quit()

def test_preencher_o_login(browser):
    browser.get("http://127.0.0.1:5000/login")
    from time import sleep
    sleep(5)