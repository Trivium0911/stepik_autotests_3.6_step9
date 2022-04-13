from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_button_exist(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(10)
    assert browser.find_element(By.CSS_SELECTOR, "button[class~='btn-add-to-basket']"), "Basket not found."
