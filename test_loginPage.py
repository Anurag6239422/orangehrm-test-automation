import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.login import LogIn

#Test Case 1

def test_correctLogin(browserInstance):
    driver = browserInstance
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    log = LogIn(driver)
    log.Correctlogin_data()

    dashboard = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    assert dashboard.is_displayed()

#Test Case 2

def test_incorrectLogin(browserInstance):
    driver = browserInstance
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    
    log = LogIn(driver)
    log.Incorrectlogin_data()

    message = driver.find_element(By.CLASS_NAME, "oxd-alert-content-text").text

    assert "Invalid credentials" in message

