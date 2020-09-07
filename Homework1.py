from selenium import webdriver
driver=webdriver.Firefox(executable_path=r'C:\Users\elena\Downloads\geckodriver-v0.27.0-win64\geckodriver.exe')
driver.get("https://www.datafolks.com")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def verifyLogo():
   # wait until logo on the page is visible and verify its text
   logo = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME,"tn-atom")))
   assert logo.text == "DATAFOLKS"

def waitForElementVisibility(element_xpath):
   return WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, element_xpath)

def waitForElementClickable(element_xpath):
   return WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, element_xpath)

verifyLogo()

# find main text of home page and verify it's text
main_text = driver.find_element_by_xpath('//div[@data-elem-id=1551634856822]/h1')
assert main_text.text == "Quality code\nfor your ideas"

# wait until Contact Us in Navigation bar is clickable
contact_us_navigation_bar_btn = waitForElementClickable("//a[contains(text(),'Contact Us')]") #returns Web Element
contact_us_navigation_bar_btn.click()

verifyLogo()

# wait until text on the Contact Us page will be visible and verify its text
contact_page_header = waitForElementVisibility('//div[@data-elem-id=1551634856822]/h1')
assert contact_page_header.text == "Get in touch"

#wait until email input field is visible and input mail@example.com
email_input_field = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email_input_field.send_keys("mail@example.com")

# wait until the SUBMIT button is clickable
submit_btn = waitForElementClickable('//button[@class="t-submit"]')
submit_btn.click()


# wait until thank you! we will contact you soon message pops up and close the browser
popup_text = waitForElementVisibility('//div[@id="tildaformsuccesspopuptext"]')
assert popup_text.text == "Thank you! We will contact you soon."

driver.close()
