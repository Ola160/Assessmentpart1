import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from openpyxl import load_workbook

excel_file = '/Users/olatundeolawoyin/PycharmProjects/Assessmentpart1/TestData/amazonlog1.xlsx'
wb = load_workbook(excel_file)
sheet = wb.active

username = sheet['A1'].value
password = sheet['B1'].value

driver = webdriver.Chrome()

driver.get('https://www.amazon.co.uk/')

sign_in_button = driver.find_element(By.ID, 'nav-link-accountList')
sign_in_button.click()

email_field = driver.find_element(By.ID, 'ap_email')
email_field.send_keys(username)

continue_button = driver.find_element(By.ID, 'continue')
continue_button.click()

time.sleep(2)

password_field = driver.find_element(By.ID, 'ap_password')
password_field.send_keys(password)

sign_in_submit = driver.find_element(By.ID, 'signInSubmit')
sign_in_submit.click()

time.sleep(5)

driver.quit()

