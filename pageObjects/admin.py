from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Admin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.admin_visble = (By.XPATH, "//span[text()='Admin']")
        self.admin_user_name =(By.XPATH, "(//input[@fdprocessedid='aeasjf'])[1]")

    def is_admin_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.admin_visble)).is_displayed()
    
    def open_admin_page(self):
        self.wait.until(EC.visibility_of_element_located(self.admin_visible)).click()
    