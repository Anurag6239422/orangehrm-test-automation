from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LogOut:
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_button = (By.XPATH, "//ul[@class='oxd-dropdown-menu']//li[4]")

    def logout_click(self):
        self.driver.find_element(*self.dropdown_button).click()

    