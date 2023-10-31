from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    textbox_username_xpath = "//label[@for='ap_email']/following-sibling::input[1]"
    continue_button_id = "(//span[@id='continue'])[1]"
    textbox_password_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[1]/input"
    button_login_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[2]/div/form/div/div[2]/span"

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by, value, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located((by, value)))

    def setUsername(self, username):
        username_input = self.wait_for_element(By.XPATH, self.textbox_username_xpath)
        username_input.clear()
        username_input.send_keys(username)

    def continueButton(self):
        continue_button = self.wait_for_element(By.ID, self.continue_button_id)
        continue_button.click()

    def setPassword(self, password):
        password_input = self.wait_for_element(By.XPATH, self.textbox_password_xpath)
        password_input.clear()
        password_input.send_keys(password)

    def clickLogin(self):
        login_button = self.wait_for_element(By.XPATH, self.button_login_xpath)
        login_button.click()
