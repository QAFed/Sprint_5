from LINKS import URLpage
from LINKS import RegisterXpath
from LINKS import RegisterCSS
from LINKS import LoginXpath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import LoginPassName


def test_register_form_if_name_email_pass_correct_go_auth_page(driver):
    new_user = LoginPassName()
    driver.get(URLpage.REGISTER)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, RegisterXpath.name)))
    driver.find_element(By.XPATH, RegisterXpath.name).send_keys(new_user.name)
    driver.find_element(By.XPATH, RegisterXpath.email).send_keys(new_user.email)
    driver.find_element(By.XPATH, RegisterXpath.password).send_keys(new_user.password)
    driver.find_element(By.XPATH, RegisterXpath.button_register).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
    assert driver.current_url == URLpage.LOGIN


def test_alert_text_if_pass_less_than_6_char(driver):
    new_user = LoginPassName()
    bad_pass = '12345'
    driver.get(URLpage.REGISTER)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, RegisterXpath.name)))
    driver.find_element(By.XPATH, RegisterXpath.name).send_keys(new_user.name)
    driver.find_element(By.XPATH, RegisterXpath.email).send_keys(new_user.email)
    driver.find_element(By.XPATH, RegisterXpath.password).send_keys(bad_pass)
    driver.find_element(By.XPATH, RegisterXpath.button_register).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, RegisterCSS.pass_field_alert)))
    alert_text = driver.find_element(By.CSS_SELECTOR, RegisterCSS.pass_field_alert).text
    assert alert_text == 'Некорректный пароль'


def test_link_login_if_click_open_login_page(driver):
    driver.get(URLpage.REGISTER)
    driver.find_element(By.XPATH, RegisterXpath.link_to_login).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
    assert driver.current_url == URLpage.LOGIN
