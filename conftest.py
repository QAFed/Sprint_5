
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from links import URLpage
from locators import RegisterXpath
from locators import StartXpath
from locators import LoginXpath
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import LoginPassName


@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=service)
    yield web_driver
    web_driver.quit()


def reg_new_user(driver):
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
    return new_user


@pytest.fixture
def driver_with_login_user(driver):
    new_user = reg_new_user(driver)
    driver.get(URLpage.LOGIN)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
    driver.find_element(By.XPATH, LoginXpath.email).send_keys(new_user.email)
    driver.find_element(By.XPATH, LoginXpath.password).send_keys(new_user.password)
    driver.find_element(By.XPATH, LoginXpath.button_login).click()
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_order)))
    yield driver
    driver.quit()

