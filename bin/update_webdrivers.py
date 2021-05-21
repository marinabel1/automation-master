# encoding: utf-8

from pprint import pprint
import os
from re import search

import requests
import tarfile
import zipfile
from pathlib import Path
from io import BytesIO
import os


class WebDriverUpdater:
    def __init__(self):
        self.driver_folder = f"{os.path.dirname(os.path.realpath(__file__))}/../webdriver"

    def run(self, browser=None):
        # ChromeDriver(self.driver_folder).run()
        GeckoDriver(self.driver_folder).run()
        # OperaDriver(self.driver_folder).run()


class Base:
    def __init__(self, driver_folder, links):
        self.driver_folder = driver_folder
        self.links = links

    def run(self):
        if self.driver_folder is None:
            raise Exception("driver_folder is not set")

        for key in self.links:
            path = f"{self.driver_folder}/{key}"
            self.__download(self.links[key], path)

    def __get_links(self):
        raise NotImplementedError("__get_links is not implemented")

    def __download(self, url, path):
        print("URL: %s" % url)

        response = requests.get(url, allow_redirects=True, )

        if response.status_code != 200:
            raise Exception(f"Wrong response code: {response.status_code}")

        content = response.content
        size = len(content)
        print("Size: %.2f MB (%d)" % (size / 1024 / 1024, size))

        if size < 1000000:
            raise Exception(f"Wrong file size: {size}")

        suffix = Path(url).suffix

        content = BytesIO(response.content)

        if suffix == '.zip':
            with zipfile.ZipFile(content) as z:
                file = [info.filename for info in z.infolist() if search("driver(\.exe)?$", info.filename)][0]
                with open(f"{path}/{Path(file).name}", 'wb') as f:
                    f.write(z.read(file))
        elif suffix == '.gz':
            tar_file = tarfile.open(fileobj=content, mode="r|gz")
            tar_file.extractall(path)

        if os.path.isfile(path + "/chromedriver"):
            os.chmod(path + "/chromedriver", 0o744)

        if os.path.isfile(path + "/geckodriver"):
            os.chmod(path + "/geckodriver", 0o744)

        if os.path.isfile(path + "/operadriver"):
            os.chmod(path + "/operadriver", 0o744)

        print("New file extracted to: %s\n" % path)


class ChromeDriver(Base):
    def __init__(self, driver_folder):
        self.latest_version = self.__get_latest_version()
        super().__init__(f"{driver_folder}/chrome", self.__get_links())

    def __get_latest_version(self):
        response = requests.get('https://chromedriver.storage.googleapis.com/LATEST_RELEASE')

        if response.status_code != 200:
            raise Exception(f"Wrong response code: {response.status_code}")

        return response.text

    def __get_links(self):
        url = f"https://chromedriver.storage.googleapis.com/{self.latest_version}/"
        return {
            "linux": f"{url}chromedriver_linux64.zip",
            "macos": f"{url}chromedriver_mac64.zip",
            "windows": f"{url}chromedriver_win32.zip"
        }


class GeckoDriver(Base):
    def __init__(self, driver_folder):
        self.latest_release = self.__get_latest_release()
        super().__init__(f"{driver_folder}/firefox", self.__get_links())

    def __get_latest_release(self):
        response = requests.get("https://api.github.com/repos/mozilla/geckodriver/releases/latest")

        if response.status_code != 200:
            raise Exception(f"Wrong response code: {response.status_code}")

        return f"v{response.json()['name']}"

    def __get_links(self):
        url = f"https://github.com/mozilla/geckodriver/releases/latest/download/"
        return {
            "linux": f"{url}geckodriver-{self.latest_release}-linux64.tar.gz",
            "macos": f"{url}geckodriver-{self.latest_release}-macos.tar.gz",
            "windows": f"{url}geckodriver-{self.latest_release}-win64.zip"
        }


class OperaDriver(Base):
    def __init__(self, driver_folder):
        super().__init__(f"{driver_folder}/opera", self.__get_links())

    def __get_links(self):
        url = f"https://github.com/operasoftware/operachromiumdriver/releases/latest/download/"
        return {
            "linux": f"{url}operadriver_linux64.zip",
            "macos": f"{url}operadriver_mac64.zip",
            "windows": f"{url}operadriver_win64.zip"
        }


if __name__ == '__main__':
    updater = WebDriverUpdater()
    updater.run()
