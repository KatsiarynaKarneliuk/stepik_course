import time
import pytest
from selenium import webdriver

def test_should_check_add_basket_presence(browser,pause_time):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(30)
    add_basket = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    assert add_basket, "Кнопка не найдена"

    if pause_time:
        print(f'Включена автопауза на {pause_time} секунд')
        time.sleep(int(pause_time))
