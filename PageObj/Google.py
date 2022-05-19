from BaseClass import BasePage
from selenium.webdriver.common.by import By
import allure


class GoogleLocator:
    lucky_button = (By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[2]')


class GooglePage(BasePage):
    def click_lucky_button(self):
        button = self.find_element(GoogleLocator.lucky_button)
        with allure.step(f'Нажимаю на кнопку {GoogleLocator.lucky_button}'):
            try:
                button.click()
            except Exception as e:
                raise AssertionError(f'Exeption {e}')