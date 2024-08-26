import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from LINKS import URLpage
from LINKS import RegisterXpath
from LINKS import RegisterCSS
from LINKS import LoginXpath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import LoginPassName


class LoginPassName():
    def __init__(self):
        self.gen_id = datetime.now().strftime("%Y%m%d%H%M%S")
        self.name = f"name{self.gen_id}"
        self.email = f"FedorIdolenkov_{self.gen_id}@ya.ya"
        self.password = f"psswrd{self.gen_id}"

@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=service)
    yield web_driver
    web_driver.quit()


def reg_new_user():
    new_user = LoginPassName()
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(URLpage.REGISTER)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, RegisterXpath.name)))
    driver.find_element(By.XPATH, RegisterXpath.name).send_keys(new_user.name)
    driver.find_element(By.XPATH, RegisterXpath.email).send_keys(new_user.email)
    driver.find_element(By.XPATH, RegisterXpath.password).send_keys(new_user.password)
    driver.find_element(By.XPATH, RegisterXpath.button_register).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
    if driver.current_url == URLpage.LOGIN:
        return new_user
    else:
        raise Exception


def driver_with_login_user(new_user):
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(URLpage.LOGIN)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
    driver.find_element(By.XPATH, LoginXpath.email).send_keys(new_user.email)
    driver.find_element(By.XPATH, LoginXpath.password).send_keys(new_user.password)
    driver.find_element(By.XPATH, LoginXpath.button_login).click()
    if driver.current_url == URLpage.START:
        yield driver
        driver.quit()
    else:
        raise Exception

