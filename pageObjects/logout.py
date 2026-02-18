from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogOut:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.dropdown_button = (By.XPATH, "//span[contains(@class,'oxd-userdropdown-tab')]")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def logout_click(self):
        self.wait.until(EC.visibility_of_element_located(self.dropdown_button)).click()
        self.wait.until(EC.element_to_be_clickable(self.dropdown_button)).click()

    