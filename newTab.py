from selenium import webdriver
import time
import math

try:
    link ="http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector('button.trollface')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))


    x_element = browser.find_element_by_css_selector('#input_value.nowrap')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_css_selector('#answer[required]')
    answer.send_keys(y)

    button = browser.find_element_by_css_selector('button.btn-primary')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()