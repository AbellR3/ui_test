from selenium.webdriver.common.by import By

from BaseClass import BasePage
def test_lucky_button(browser):
    page = BasePage(browser, "https://yandex.ru/")
    page.find_element((By.XPATH,'//*[text()="Погода"]'),15).click()

    assert browser.current_url == "https://yandex.ru/"
