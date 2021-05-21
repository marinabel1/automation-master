import os
import platform

from pprint import pprint
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.opera.options import Options as OperaOptions
from os.path import isfile
from selenium import webdriver


class WebDriver:
    BROWSER_CHROME = 'chrome'
    BROWSER_FIREFOX = 'firefox'
    BROWSER_OPERA = 'opera'

    MOBILE_MOTO_G4 = 'Moto G4'
    MOBILE_GALAXY_S3 = 'Galaxy S III'
    MOBILE_GALAXY_S5 = 'Galaxy S5'
    MOBILE_GALAXY_NOTE_2 = 'Galaxy Note II'
    MOBILE_GALAXY_NOTE_3 = 'Galaxy Note 3'
    MOBILE_PIXEL_2 = 'Pixel 2'
    MOBILE_PIXEL_2_XL = 'Pixel 2 XL'
    MOBILE_IPHONE_5_SE = 'iPhone 5/SE'
    MOBILE_IPHONE_6_7_8 = 'iPhone 6/7/8'
    MOBILE_IPHONE_6_7_8_PLUS = 'iPhone 6/7/8 Plus'
    MOBILE_IPHONE_X = 'iPhone X'
    MOBILE_IPAD = 'iPad'
    MOBILE_IPAD_MINI = 'iPad Mini'
    MOBILE_IPAD_PRO = 'iPad Pro'
    MOBILE_BLACKBERRY_Z30 = 'BlackBerry Z30'
    MOBILE_BLACKBERRY_PLAYBOOK = 'Blackberry PlayBook'
    MOBILE_NEXUS_4 = 'Nexus 4'
    MOBILE_NEXUS_5 = 'Nexus 5'
    MOBILE_NEXUS_5X = 'Nexus 5X'
    MOBILE_NEXUS_6 = 'Nexus 6'
    MOBILE_NEXUS_6P = 'Nexus 6P'
    MOBILE_NEXUS_7 = 'Nexus 7'
    MOBILE_NEXUS_10 = 'Nexus 10'
    MOBILE_LG_OPTIMUS_L70 = 'LG Optimus L70'
    MOBILE_NOKIA_N9 = 'Nokia N9'
    MOBILE_NOKIA_LUMIA_520 = 'Nokia Lumia 520'
    MOBILE_MICROSOFT_LIMIA_550 = 'Microsoft Lumia 550'
    MOBILE_MICROSOFT_LIMIA_905 = 'Microsoft Lumia 950'
    MOBILE_KINDLE_HDX = 'Kindle Fire HDX'

    def __init__(
            self,
            browser=BROWSER_CHROME,
            domain="zver480011.develz.ru",
            start_page="zver480011.develz.ru",
            login=None,
            password=None,
            mobileEmulation=None,
            isHeadless=False
    ):
        self.domain = domain
        self.start_page = start_page
        self.login = login
        self.password = password
        self.mobileEmulation = mobileEmulation
        self.isHeadless = isHeadless

        self.driver = self.__get_webdriver(browser)

    def __get_webdriver(self, browser):
        """Получить WebDriver для нужного браузера и операционной системы"""

        if browser not in [self.BROWSER_CHROME, self.BROWSER_FIREFOX, self.BROWSER_OPERA]:
            raise Exception(f"Unsupported browser: {browser}")

        driver = None

        if browser == self.BROWSER_CHROME:
            driver_path = self.__get_chromedriver_path()

            cap = DesiredCapabilities().CHROME
            cap["marionette"] = False
            cap["goog:loggingPrefs"] = {"browser": "ALL"}

            options = ChromeOptions()
            options.add_argument("--auto-open-devtools-for-tabs")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-gpu")

            if self.mobileEmulation:
                mobile_emulation = {"deviceName": self.mobileEmulation}
                options.add_experimental_option("mobileEmulation", mobile_emulation)

            if self.isHeadless:
                options.add_argument("--no-sandbox")
                options.add_argument("--headless")

            driver = webdriver.Chrome(desired_capabilities=cap, executable_path=driver_path, options=options)

        elif browser == self.BROWSER_FIREFOX:
            driver_path = self.__get_geckodriver_path()
            cap = DesiredCapabilities().FIREFOX
            cap["marionette"] = False

            options = FirefoxOptions()

            if self.isHeadless:
                options.headless = True

            driver = webdriver.Chrome(desired_capabilities=cap, executable_path=driver_path, options=options)
        elif browser == self.BROWSER_OPERA:
            driver_path = self.__get_operadriver_path()
            cap = DesiredCapabilities().OPERA
            cap["marionette"] = False

            options = OperaOptions()

            if self.isHeadless:
                options.headless = True

            driver = webdriver.Opera(desired_capabilities=cap, executable_path=driver_path, options=options)

        if driver is None:
            raise Exception(f"Unable to initialize driver for browser: {browser}")

        return driver

    def __get_chromedriver_path(self):
        """Получить путь до WebDriver для браузера Chrome"""

        driver_folder = f"{os.path.dirname(os.path.realpath(__file__))}/{self.BROWSER_CHROME}"

        platform_name = platform.system()
        if platform_name == 'Windows':
            sub_path = "windows/chromedriver.exe"
        elif platform_name == 'Linux':
            sub_path = "linux/chromedriver"
        elif platform_name == 'Darwin':
            sub_path = "macos/chromedriver"
        else:
            raise Exception(f"Unsupported OS platform: {platform_name}")

        driver_path = f"{driver_folder}/{sub_path}"
        if not isfile(driver_path):
            raise Exception(f"chromedriver binary not found: {driver_path}")

        return driver_path

    def __get_geckodriver_path(self):
        """Получить путь до WebDriver для браузера Firefox"""

        driver_folder = f"{os.path.dirname(os.path.realpath(__file__))}/{self.BROWSER_FIREFOX}"

        platform_name = platform.system()
        if platform_name == 'Windows':
            sub_path = "windows/geckodriver.exe"
        elif platform_name == 'Linux':
            sub_path = "linux/geckodriver"
        elif platform_name == 'Darwin':
            sub_path = "macos/geckodriver"
        else:
            raise Exception(f"Unsupported OS platform: {platform_name}")

        driver_path = f"{driver_folder}/{sub_path}"
        if not isfile(driver_path):
            raise Exception(f"geckodriver binary not found: {driver_path}")

        return driver_path

    def __get_operadriver_path(self):
        """Получить путь до WebDriver для браузера Opera"""

        driver_folder = f"{os.path.dirname(os.path.realpath(__file__))}/{self.BROWSER_OPERA}"

        platform_name = platform.system()
        if platform_name == 'Windows':
            sub_path = "windows/operadriver.exe"
        elif platform_name == 'Linux':
            sub_path = "linux/operadriver"
        elif platform_name == 'Darwin':
            sub_path = "macos/operadriver"
        else:
            raise Exception(f"Unsupported OS platform: {platform_name}")

        driver_path = f"{driver_folder}/{sub_path}"
        if not isfile(driver_path):
            raise Exception(f"operadriver binary not found: {driver_path}")

        return driver_path

    def get_driver(self):
        driver = self.driver
        driver.domain = self.domain
        driver.login = self.login
        driver.password = self.password
        driver.result_path = None

        driver.implicitly_wait(5)
        driver.maximize_window()

        if self.login is not None and self.password is not None:
            url = f"https://{self.login}:{self.password}@{self.start_page}"
        else:
            url = f"https://{self.start_page}"

        driver.get(url)

        return self.driver
