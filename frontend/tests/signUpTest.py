from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

SIGNUP_URL = "http://localhost:3000/SignUp"

def main():

    # Create object and link to server
    service = Service(executable_path="./chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get(LOGIN_URL)
    
    # Test clicking Continue without Input
    clickContinue(driver)


    time.sleep(10)
    driver.quit()
    
def clickSubmit(driver):
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Submit')]"))
    )
    
    continueButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Submit')]")
    continueButton.click()


if __name__ == '__main__':
    main()