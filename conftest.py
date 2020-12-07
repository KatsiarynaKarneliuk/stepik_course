import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#для тестов в разных браузерах
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    #в командной строке pytest -s -v --browser_name=chrome test_parser.py
    #pytest - s - v - -browser_name = firefox test_parser.py

    parser.addoption('--language', action='store', default="None", # для запуска тестов с разными языками, переданными с фронта
                     help="Choose language: ru, en ...(etc.)")
    # запуск из cmd: pytest --language=es test_items.py

    parser.addoption('--pause', action='store', default=0, help="Включение паузы после загрузки")

@pytest.fixture(scope="function")#выносим в него фикстуру browser (или другую, наиболее употребляемую мной, располагаем в верхнего уровня директории с тестами)
def browser(request):
    browser_name = request.config.getoption("browser_name")#команда для запроса значения параметра
    user_language = request.config.getoption("language")
    if (browser_name == "chrome"):
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def pause_time(request):
    pause_mode = request.config.getoption("pause")
    return pause_mode

