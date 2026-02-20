import time
from pageObjects.logout import LogOut
from pageObjects.login import LogIn
import time
import json
import pytest

test_data_path = 'data/test_loginPageFramework.json'

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_log_out(browserInstance, test_list_item):
    driver = browserInstance

    log_In = LogIn(driver)

    if test_list_item["type"] == "valid":
        log_In.Correctlogin_data(test_list_item["username"], test_list_item["password"])

        log_out = LogOut(driver)
        log_out.logout_click()

        time.sleep(10)

        #Test Case 6
        assert log_In.login_button_display()


