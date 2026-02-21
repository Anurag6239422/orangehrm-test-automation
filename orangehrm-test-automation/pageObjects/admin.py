from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Admin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.admin_visble = (By.XPATH, "//span[text()='Admin']")
        self.admin_user_name = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
        self.admin_search_button = (By.CLASS_NAME, "orangehrm-left-space")
        self.record_value = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")

    def is_admin_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.admin_visble)).is_displayed()
    
    def open_admin_page(self):
        self.wait.until(EC.visibility_of_element_located(self.admin_visible)).click()

    def is_admin_username(self):
        self.driver.find_element(*self.admin_user_name).send_keys("Admin")
        self.driver.find_element(*self.admin_search_button).click()

    def check_record(self):
        return self.wait.until(EC.visibility_of_element_located(self.record_value)).is_displayed()

    