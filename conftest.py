
from email.policy import default
import pytest 
from selenium import webdriver


CHROME_URL = "http://localhost:4444/wd/hub"

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default = "chrome")
    parser.addoption("--executor", action="store", default = "localhost")




@pytest.fixture(scope='function')
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    
    capabilities = {
    "browserName": browser,
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}
    driver = webdriver.Remote(
        desired_capabilities=capabilities,
        command_executor= f"http://{executor}:4444/wd/hub",
        
    )

    request.addfinalizer(driver.quit)
    return driver

@pytest.fixture(scope='class')
def browser_class(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    
    capabilities = {
    "browserName": browser,
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": False
    }
}
    driver = webdriver.Remote(
        desired_capabilities=capabilities,
        command_executor= f"http://{executor}:4444/wd/hub",
        
    )

    request.addfinalizer(driver.quit)
    return driver