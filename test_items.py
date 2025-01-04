from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    button = len(browser.find_elements(By.CSS_SELECTOR,(".btn-primary")))
    assert button > 0, 'Кнопка отсутствует на странице'
