import time
from LINKS import URLpage
from LINKS import RegisterXpath
from LINKS import RegisterCSS
from LINKS import LoginXpath
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_register_form_if_name_email_pass_correct_go_auth_page(driver):
    gen_id = datetime.now().strftime("%Y%m%d%H%M%S")
    name = f"name{gen_id}"
    email = f"FedorIdolenkov_{gen_id}@ya.ya"
    password = f"psswrd{gen_id}"
    driver.get(URLpage.REGISTER)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, RegisterXpath.name)))
    driver.find_element(By.XPATH, RegisterXpath.name).send_keys(name)
    driver.find_element(By.XPATH, RegisterXpath.email).send_keys(email)
    driver.find_element(By.XPATH, RegisterXpath.password).send_keys(password)
    driver.find_element(By.XPATH, RegisterXpath.button_register).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
    assert driver.current_url == URLpage.LOGIN


def test_alert_text_if_pass_less_than_6_char(driver):
    gen_id = datetime.now().strftime("%Y%m%d%H%M%S")
    name = f"name{gen_id}"
    email = f"FedorIdolenkov_{gen_id}@ya.ya"
    password = '12345'
    driver.get(URLpage.REGISTER)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, RegisterXpath.name)))
    driver.find_element(By.XPATH, RegisterXpath.name).send_keys(name)
    driver.find_element(By.XPATH, RegisterXpath.email).send_keys(email)
    driver.find_element(By.XPATH, RegisterXpath.password).send_keys(password)
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
