from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.dashboard import DasboardPage
from pageObjects.login import LogIn

def test_dashboard_validation(browserInstance):
    driver = browserInstance

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    log = LogIn(driver)
    log.Correctlogin_data()

    dash_board = DasboardPage(driver)
    
    #Test Case 3
    assert dash_board.is_dashboard_header_visible()
    assert dash_board.is_user_profile_visible()
 

