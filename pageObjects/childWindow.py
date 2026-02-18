from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Window:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.orangehrm_link = (By.XPATH, "//a[@href='http://www.orangehrm.com']")

    def move_to_new_window(self):
        self.parent_window = self.driver.current_window_handle
        self.driver.find_element(*self.orangehrm_link).click()

        self.wait.until(EC.number_of_windows_to_be(2))

        for window in self.driver.window_handles:
            if window != self.parent_window:
                self.driver.switch_to.window(window)
                self.child_url = self.driver.current_url
                self.driver.close()
                break

        self.driver.switch_to.window(self.parent_window)


        return self.child_url