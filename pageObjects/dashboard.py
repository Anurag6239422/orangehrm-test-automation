from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DasboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard_header = (By.XPATH, "//h6[text()='Dashboard']")
        self.wait = WebDriverWait(self.driver, 10)
        self.user_profile = (By.CLASS_NAME, "oxd-userdropdown-name")

    def is_dashboard_header_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.dashboard_header)).is_displayed()
    
    def is_user_profile_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.user_profile)).is_displayed()