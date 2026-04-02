from pageObjects.childWindow import Window

def test_Window(browserInstance):
    driver = browserInstance

    win_dow = Window(driver)

    child_url = win_dow.move_to_new_window()

    #Test Case 6
    assert "orangehrm.com" in child_url


