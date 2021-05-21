# Тесты

## Установка зависимостей

Для управления зависимостями используем [pipenv](https://pypi.org/project/pipenv/). Для установки pipenv:
 
    pip install pipenv

Для установки зависимостей:
    
    pipenv install

## Selenium WebDriver

В тесте возможно конфигурация веб-драйвера:

    web_driver = WebDriver(
        WebDriver.BROWSER_CHROME,   # Браузер (из констант WebDriver.BROWSER_*)
        "andrey.develz.ru",         # Основной домен тестового контура
        "borrow.andrey.develz.ru",  # Стартовая страница теста
        "secret_login",             # BasicAuth логин (необязательный параметр)
        "super_secret_password",    # BasicAuth пароль (необязательный параметр)
        WebDriver.MOBILE_GALAXY_S5  # Эмулируемое мобильное утройство (необязательный параметр, из констант WebDriver.MOBILE_*)
    ).get_driver()

### Обновление WebDriver

Для обновления вебдрайверов используется скрипт: `bin/update_webdrivers.py`.

Скрипт выкачивает последние релизы вебдрайверов в директорию `webdriver`.

## Тесты
 
### Анкета заёмщика (borrow.zaymigo.com)

Тесты анкеты заёмщика описаны в директориях `borrow/newbie/tests` и `borrow/repeater/tests`.

Полный позитивный тест анкеты первичника:

    borrow/newbie/tests/runFullPositiveTest.py

## Полезные мелочи

### Получение элемента в консоли браузера

    document.evaluate("//*[@name='familyName']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;

