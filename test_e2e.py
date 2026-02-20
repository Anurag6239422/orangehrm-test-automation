import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.dashboard import DasboardPage
from pageObjects.login import LogIn
from pageObjects.admin import Admin
from pageObjects.childWindow import Window
from pageObjects.logout import LogOut

def test_end2end(browserInstance):
    driver = browserInstance

    #Test Case 1

    log = LogIn(driver)
    log.Correctlogin_data("Admin", "admin123")

    dashboard = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )

    assert dashboard.is_displayed()

    #Test Case 2

    dash_board = DasboardPage(driver)
    
    assert dash_board.is_dashboard_header_visible()
    assert dash_board.is_user_profile_visible()

    #Test Case 4

    ad_min = Admin(driver)
    assert ad_min.is_admin_visible()
    assert ad_min.check_record()
    
    #Test Case 5
    log_out = LogOut(driver)
    log_out.logout_click()
    
    time.sleep(10)

    assert log.login_button_display()
    
    #Test Case 6
    win_dow = Window(driver)
    child_url = win_dow.move_to_new_window()

    assert "orangehrm.com" in child_url

    #Test Case 7
    log.Incorrectlogin_data("Admin", "admin124")

    message = driver.find_element(By.CLASS_NAME, "oxd-alert-content-text").text

    assert "Invalid credentials" in message
    