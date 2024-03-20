from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

LOGIN_URL = "http://localhost:3000"

def main():

    # Create object and link to server
    service = Service(executable_path="./chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(LOGIN_URL)
    
    # Test Case: empty Input Field
    # clickContinue(driver)

    # Test Case: Owner Account
    testAdminAccount(driver)

    # continueButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Continue')]")
    # continueButton.click()

    time.sleep(10)
    driver.quit()
    
def testAdminAccount(driver):
    ''' Test Case for Admin account Successfully login '''
    fillInEmail(driver, "admin@admin.com")
    fillInPassword(driver, "admin")
    clickContinue(driver)
    
def clickContinue(driver):
    # Wait for page elements to load
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Continue')]"))
    )
    
    continueButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Continue')]")
    continueButton.click()

def fillInEmail(driver, email):
    # Wait for page elements to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
    
    # Locate email input fields and fill in test email
    emailInput = driver.find_element(By.XPATH, "//input[@type='email']")
    emailInput.clear()
    emailInput.send_keys(email)

def fillInPassword(driver, password):
    # Wait for page elements to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    
    # Locate password input fields and fill in test password
    passwordInput = driver.find_element(By.XPATH, "//input[@type='password']")
    passwordInput.clear()
    passwordInput.send_keys(password)
    
    
if __name__ == '__main__':
    main()