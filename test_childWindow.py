from pageObjects.childWindow import Window
def test_Window(browserInstance):
    driver = browserInstance

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    win_dow = Window(driver)

    child_url = win_dow.move_to_new_window()

    #Test Case 6
    assert "orangehrm.com" in child_url


