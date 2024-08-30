from links import URLpage
from locators import ForgotXpath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginXpath


def test_link_login_if_click_oopen_login_page(driver):
    driver.get(URLpage.FORGOT)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ForgotXpath.link_to_login)))
    driver.find_element(By.XPATH, ForgotXpath.link_to_login).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
    assert driver.current_url == URLpage.LOGIN
