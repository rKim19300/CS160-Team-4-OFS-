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
    
    # Test clicking Continue without Input
    clickContinue(driver)

    # Wait before proceed to avoid web load slowly issue
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "chakra-input css-datkyu"))
    # )

    # # Testing steps
    # input_element = driver.find_element(By.CLASS_NAME, "chakra-input css-datkyu")
    # input_element.clear()
    # input_element.send_keys("testEmail@gmail.com" + Keys.ENTER)

    # # Wait before proceed to avoid web load slowly issue
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    # )


    # # Find and click on the matched first link found
    # link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
    # link.click()

    # # Find and return an array of all match results
    # #link = driver.find_elements(By.PARTIAL_LINK_TEXT, "Tech With Tim")

    
    
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Continue')]"))
    # )
    
    # continueButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Continue')]")
    # continueButton.click()

    time.sleep(10)
    driver.quit()
    
def clickContinue(driver):
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Continue')]"))
    )
    
    continueButton = driver.find_element(By.XPATH, "//*[contains(text(), 'Continue')]")
    continueButton.click()


if __name__ == '__main__':
    main()