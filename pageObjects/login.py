from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogIn:
    def __init__(self, driver):
        self.driver = driver
        self.user_name = (By.XPATH, "//input[@name='username']")
        self.password = (By.XPATH, "//input[@type='password']")
        self.logIn_Button = (By.CLASS_NAME, "oxd-button--medium")
        
    def Correctlogin_data(self):
        wait = WebDriverWait(self.driver, 15)

        wait.until(EC.visibility_of_element_located(self.user_name)).send_keys("Admin")
        wait.until(EC.visibility_of_element_located(self.password)).send_keys("admin123")
        wait.until(EC.element_to_be_clickable(self.logIn_Button)).click()
    
    def Incorrectlogin_data(self):
        self.driver.find_element(*self.user_name).send_keys("Admin")
        self.driver.find_element(*self.password).send_keys("admin124")
        self.driver.find_element(*self.logIn_Button).click()