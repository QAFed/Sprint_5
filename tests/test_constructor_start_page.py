from LINKS import URLpage
from selenium.webdriver.common.by import By
from LINKS import StartXpath
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from LINKS import LoginXpath


def test_button_login_if_click_open_login_page(driver):
    driver.get(URLpage.START)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_login)))
    driver.find_element(By.XPATH, StartXpath.button_login).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
    assert driver.current_url == URLpage.LOGIN


def test_button_personal_account_if_click_open_login_page(driver):
    driver.get(URLpage.START)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_personal_account)))
    driver.find_element(By.XPATH, StartXpath.button_personal_account).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
    assert driver.current_url == URLpage.LOGIN
