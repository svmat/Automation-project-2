from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:\Users\elena\Downloads\geckodriver-v0.27.0-win64\geckodriver.exe')
driver.get("https://www.datafolks.com")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# wait until the "CONTACT US" button in the middle of the page is clickable
contact_us_middle_of_the_page_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@data-elem-id=1551726675405]/a')))
contact_us_middle_of_the_page_btn.click()

#wait until Contact Us form is visible and verify presence of name and its text
name_input_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,  "//div[contains (text(), 'Name')]")))
assert name_input_field.text == "Name"

# wait until Contact Us input form is visible and input name Elena Lanchi
name_input_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "Name")))
name_input_field.send_keys("Elena Lanchi")

#wait until Contact us form is visible and verify presence of email and its text
email_input_field = WebDriverWait(driver,  20).until(EC.presence_of_element_located((By.XPATH,  "//div[contains (text(), 'E-mail')]")))
assert email_input_field.text == "E-mail"

# wait until Contact Us email input is visible and input email elena@mail.com
email_input_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "Email")))
email_input_field.send_keys("elena@mail.com")

#wait until Contact Us form is visible and verify presense of phone and its text
phone_number_input_field =WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains (text(), 'Phone')]")))
assert phone_number_input_field.text == "Phone"

# wait until Contact us form phone input is visible and input 1234589
phone_number_input_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "Phone")))
phone_number_input_field.send_keys("1234589")

#wait until Contact Us form is visible and verify Country input name and its text
country_name_input_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[contains (text(), 'Country')]")))
assert country_name_input_field.text == "Country"

# wait until Contact us form Country input is visible and input USA
country_name_input_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "Country")))
country_name_input_field.send_keys("USA")

# wait until Send button is clickable and click on it
send_btn = WebDriverWait(driver, 120).until(EC.element_to_be_clickable((By.CLASS_NAME, "t-submit")))
send_btn.click()

#wait until the close button is clickable and click on it
close_btn = WebDriverWait(driver,  120).until(EC.element_to_be_clickable((By.XPATH, '//div[@class= "t-popup__close-wrapper"]')))
close_btn.click()