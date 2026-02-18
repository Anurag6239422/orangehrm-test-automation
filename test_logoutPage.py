from pageObjects.logout import LogOut
from pageObjects.login import LogIn

def test_log_out(browserInstance):
    driver = browserInstance

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    log_In = LogIn(driver)
    log_In.Correctlogin_data()

    log_out = LogOut(driver)
    log_out.logout_click()

    #Test Case 6
    assert log_In.login_button_display()


