import time
from LINKS import URLpage
from LINKS import RegisterXpath
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
    time.sleep(5)
    driver.get(URLpage.REGISTER)
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, RegisterXpath.name)))
    driver.find_element(By.XPATH, RegisterXpath.name).send_keys(name)
    driver.find_element(By.XPATH, RegisterXpath.email).send_keys(email)
    driver.find_element(By.XPATH, RegisterXpath.password).send_keys(password)

    time.sleep(5)
    driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button').click()
    time.sleep(5)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located(
            (By.XPATH, LoginXpath.button_login))
    )
    assert driver.current_url == URLpage.LOGIN
