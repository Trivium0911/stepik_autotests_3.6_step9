from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_button_present(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    btn = browser.find_element(By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > button")
    time.sleep(10)
    assert btn is not None, "Basket not found."

