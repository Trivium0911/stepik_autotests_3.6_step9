from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_button_present(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    time.sleep(10)
    btn = browser.find_element(By.CSS_SELECTOR, ".product_page #add_to_basket_form .btn-add-to-basket")
    assert btn is not None, "Basket not found."
