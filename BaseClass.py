import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def step(msg_about:str, msg_error:str):
    def this_func(func):
        def wrapper(*args, **kwargs):

            msg = f'{msg_about} {str(args), str(kwargs)}'
            with allure.step(msg):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    raise AssertionError(e, msg_error)
        return wrapper
    return this_func

class BasePage:
    def __init__(self, driver, url: str = 'https://google.com') -> None:
        self.driver = driver
        self.url = url
        self.go_to_site()

    @step('Ищю элемент', 'Не дождался элемента')
    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver,
         timeout=time
         ).until(EC.presence_of_element_located(locator))

    def go_to_site(self):
        return self.driver.get(self.url)
