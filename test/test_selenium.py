from selenium.webdriver import Firefox
from pytest import fixture, mark
import time
from app import create_app
from test_flask import flask_test
from flask import url_for

## todo script with requests to jumt start this test
## commands 1
# clerk={'position':1,'name':'eduardo','subjects':'devolucao\nreclamacao\ nfinanceiro','password':'12345'}
# post('http://127.0.0.1:5000/clerk/adicionar',json=clerk).json()

@fixture(scope='module')
def browser( ):
    browser = Firefox()
    yield browser
    browser.quit()


def test_login_vazio(browser):
    browser.get("http://127.0.0.1:5000/login")
    submit_button = browser.find_elements_by_xpath('/html/body/form/p[4]/input')[0]
    submit_button.click()
    error_msg = browser.find_elements_by_xpath("/html/body/h3")[0]
    assert error_msg.text == "Error no Login"

def test_login_errado(browser):
    browser.get("http://127.0.0.1:5000/login")
    name = browser.find_elements_by_xpath('/html/body/form/p[2]/input')[0]
    name.send_keys('fvfsf')
    password = browser.find_elements_by_xpath('/html/body/form/p[3]/input')[0]
    password.send_keys('sdfdfsd')
    submit_button = browser.find_elements_by_xpath('/html/body/form/p[4]/input')[0]
    submit_button.click()
    error_msg = browser.find_elements_by_xpath("/html/body/h3")[0]
    assert error_msg.text == "Error no Login"

def test_login_certo(browser):
    browser.get("http://127.0.0.1:5000/login")
    name = browser.find_elements_by_xpath('/html/body/form/p[2]/input')[0]
    name.send_keys('eduardo')
    password = browser.find_elements_by_xpath('/html/body/form/p[3]/input')[0]
    password.send_keys('12345')
    submit_button = browser.find_elements_by_xpath('/html/body/form/p[4]/input')[0]
    submit_button.click()
    name_win = browser.find_elements_by_xpath("/html/body/h1")[0]
    assert name_win.text == "eduardo"
    time.sleep(1)

def test_escolher_tickets_aparece(browser):
    browser.get("http://127.0.0.1:5000/tickets/machine")
