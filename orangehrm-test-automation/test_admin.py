from pageObjects.login import LogIn
from pageObjects.admin import Admin
import time
import json
import pytest

test_data_path = 'data/test_loginPageFramework.json'

with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("data_list_item",test_list)
def test_admin_validation(browserInstance,data_list_item):
    driver = browserInstance

    log = LogIn(driver)
    if data_list_item["type"] == "valid":
        log.Correctlogin_data(data_list_item["username"], data_list_item["password"])

        ad_min = Admin(driver)

        #Test Case 4
        assert ad_min.is_admin_visible()

        #Test Case 5
        assert ad_min.check_record()
