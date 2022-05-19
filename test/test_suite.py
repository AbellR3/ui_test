import pytest
from selenium.webdriver.common.by import By

from BaseClass import BasePage
from PageObj.Google import GooglePage



@pytest.mark.usefixtures('browser_class')
class TestSuite:
    def test_lucky_button(self,browser_class):
        page = BasePage(browser_class, "https://yandex.ru/")
        page.find_element((By.XPATH,'//*[text()="Погода"]'),15).click()

        assert browser_class.current_url == "https://yandex.ru/"

    def test_lucky_button(self,browser_class):
        page = GooglePage(browser_class)
        page.click_lucky_button()
        assert browser_class.current_url == "https://www.google.com/doodles"