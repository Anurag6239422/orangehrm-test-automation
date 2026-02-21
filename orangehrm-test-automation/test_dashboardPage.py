from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.dashboard import DasboardPage
from pageObjects.login import LogIn
import json
import pytest

test_data_path = 'data/test_loginPageFramework.json'

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_dashboard_validation(browserInstance, test_list_item):
    driver = browserInstance

    log = LogIn(driver)

    if test_list_item["type"] == "valid":
        log.Correctlogin_data(test_list_item["username"], test_list_item["password"])

        dash_board = DasboardPage(driver)
    
        #Test Case 3
        assert dash_board.is_dashboard_header_visible()
        assert dash_board.is_user_profile_visible()
 

