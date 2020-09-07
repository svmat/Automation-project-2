from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'C:\Users\elena\Downloads\geckodriver-v0.27.0-win64\geckodriver.exe')
driver.get("https://www.datafolks.com")

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def waitForElementVisibility(element_xpath):
  return WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, element_xpath)

# wait until the "see why we're worth it" button becomes visible
see_why_we_re_worth_it_btn = waitForElementVisibility('//div[@data-elem-id=1551635176282]/a')
see_why_we_re_worth_it_btn.click()

image_elements = ['//div[@data-elem-id=1551738136013]', '//div[@data-elem-id=1551738610551]', '//div[@data-elem-id=1551738610551]', '//div[@data-elem-id=1551738391114]')
for image_xpath in image_elements:
     waitForElementVisibility(image_xpath)

# find the mobile development element in areas of expertise and verify it's text and image presence
mobile_development_text = waitForElementVisibility('//div[@data-elem-id=1551735998271]')
assert mobile_development_text.text == "Mobile Development"

# find the web development element in areas of expertise and verify it's text and image presence
web_development_text = waitForElementVisibility('//div[@data-elem-id=1551735996289]')
assert web_development_text.text == "Web Development"

# find the augmented reality element in areas of expertise and verify it's text and image presence
augmented_reality_text = waitForElementVisibility('//div[@data-elem-id=1551735997222]')
assert augmented_reality_text.text == "Augmented Reality"

# find the virtual reality element in the areas of expertise and verify it's text and image presence
virtual_reality_text = waitForElementVisibility('//div[@data-elem-id=1551735995307]')
assert virtual_reality_text.text == "Virtual Reality"

driver.close()
