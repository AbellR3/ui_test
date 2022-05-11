
import pytest 
from selenium import webdriver
from pytest import Parser

CHROME_URL = "http://localhost:4444/wd/hub"

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default = "chrome")




@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption("--browser")
    capabilities = {
        "browserName":browser,
        
    }
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor= CHROME_URL,
        options=chrome_options
    )

    request.addfinalizer(driver.quit)
    return driver
