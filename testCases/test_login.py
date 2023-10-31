import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.driver_finder import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen


class Test_01_Login:
    baseURL = "https://www.amazon.co.uk/"
    logger = LogGen.loggen()

    @pytest.fixture()
    def setup(self):
        driver = webdriver.Chrome()
        print("Launching Chrome browser.........")
        driver.get(self.baseURL)
        driver.maximize_window()
        yield driver
        driver.quit()

    def test_homePageTitle(self, setup):
        self.logger.info("********** Test_01_Login *********")
        self.logger.info("********** checking Home Page Title *********")
        self.driver = setup
        act_title = self.wait_for_title("amazon store. Login", 20)
        if act_title == "amazon store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home page title passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error(f"********** Home page title is failed. Actual title: {act_title} *********")
            assert False

    def test_login(self, setup):
        self.logger.info("********** verifying Login test *********")
        self.driver = setup
        self.lp = LoginPage(self.driver)

        # Wait for the username input field to be present
        self.wait_for_element(By.XPATH, self.lp.textbox_username_xpath, 30)

        self.lp.setUsername("olawohoney@yahoo.com")  # Replace with your actual username
        self.lp.continueButton()

        # Wait for the password input field to be present
        self.wait_for_element(By.XPATH, self.lp.textbox_password_xpath, 30)

        self.lp.setPassword("Aramide247!")  # Replace with your actual password
        self.lp.clickLogin()
        self.logger.info("********** Login test passed *********")

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))

    def wait_for_title(self, title, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.title_is(title))
