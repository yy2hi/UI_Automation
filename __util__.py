from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

def click(element):
    ActionChains(driver).click(element).perform()

# Finds element by XPath
def find_element_by_xpath(xpath):
    return driver.find_element(By.XPATH, xpath)