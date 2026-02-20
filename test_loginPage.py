import json
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.login import LogIn

test_data_path = 'data/test_loginPageFramework.json'

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]
#Test Case 1
@pytest.mark.parametrize("test_list_item", test_list)
def test_correctLogin(browserInstance, test_list_item):
    driver = browserInstance

    log = LogIn(driver)

    if test_list_item["type"] == "valid":
        log.Correctlogin_data(test_list_item["username"], test_list_item["password"])

        dashboard = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
        )

        assert dashboard.is_displayed()

#Test Case 2
@pytest.mark.parametrize("test_list_item", test_list)
def test_incorrectLogin(browserInstance, test_list_item):
    driver = browserInstance
    
    log = LogIn(driver)
    if test_list_item["type"] == "Invalid":
        log.Incorrectlogin_data(test_list_item["username"], test_list_item["password"])

        message = driver.find_element(By.CLASS_NAME, "oxd-alert-content-text").text

        assert "Invalid credentials" in message

