import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    driver = None

    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox browser.........")
    elif browser == 'ie':
        driver = webdriver.Ie()
        print("Launching Internet Explorer browser.........")
    else:
        raise ValueError(f"Unsupported browser: {browser}. Supported browsers are 'chrome', 'firefox', and 'ie'.")
    driver.implicitly_wait(20)
    yield driver  # Provide the driver to the test
    driver.quit()  # Quit the driver after the test is finished
def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Specify the browser: chrome, firefox, ie")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


