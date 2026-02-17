from pageObjects.login import LogIn
from pageObjects.admin import Admin

def test_admin_validation(browserInstance):
    driver = browserInstance

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    log = LogIn(driver)
    log.Correctlogin_data()

    ad_min = Admin(driver)

    #Test Case 4
    assert ad_min.is_admin_visible()

    #Test Case 5
    assert ad_min.check_record()
