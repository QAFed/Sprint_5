from LINKS import URLpage
from LINKS import StartXpath
from LINKS import PersonXpath
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

def test_open_personal_account_page_if_user_is_login(driver_with_login_user):
    driver_with_login_user.get(URLpage.START)
    WebDriverWait(driver_with_login_user, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_personal_account)))
    driver_with_login_user.find_element(By.XPATH, StartXpath.button_personal_account).click()
    WebDriverWait(driver_with_login_user, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, PersonXpath.login)))
    assert driver_with_login_user.current_url == URLpage.PERSON

def test_link_constructor_click_open_start_page(driver_with_login_user):
    driver_with_login_user.get(URLpage.START)
    WebDriverWait(driver_with_login_user, 10).until(
           expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_personal_account)))
    driver_with_login_user.find_element(By.XPATH, StartXpath.button_personal_account).click()
    WebDriverWait(driver_with_login_user, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, PersonXpath.link_to_constructor)))
    driver_with_login_user.find_element(By.XPATH, PersonXpath.link_to_constructor).click()
    WebDriverWait(driver_with_login_user, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_order)))
    assert driver_with_login_user.current_url == URLpage.START

def test_link_logo_click_open_start_page(driver_with_login_user):
    driver_with_login_user.get(URLpage.START)
    WebDriverWait(driver_with_login_user, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_personal_account)))
    driver_with_login_user.find_element(By.XPATH, StartXpath.button_personal_account).click()
    WebDriverWait(driver_with_login_user, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, PersonXpath.logo_stellar)))
    driver_with_login_user.find_element(By.XPATH, PersonXpath.link_to_constructor).click()
    WebDriverWait(driver_with_login_user, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_order)))
    assert driver_with_login_user.current_url == URLpage.START




