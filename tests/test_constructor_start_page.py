
import pytest

from links import URLpage
from selenium.webdriver.common.by import By
from locators import StartXpath
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginXpath


class TestConstructorPage:
    def test_button_login_if_click_open_login_page(self, driver):
        driver.get(URLpage.START)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_login)))
        driver.find_element(By.XPATH, StartXpath.button_login).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
        assert driver.current_url == URLpage.LOGIN

    def test_button_personal_account_if_click_open_login_page(self, driver):
        driver.get(URLpage.START)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_personal_account)))
        driver.find_element(By.XPATH, StartXpath.button_personal_account).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, LoginXpath.button_login)))
        assert driver.current_url == URLpage.LOGIN

    @pytest.mark.parametrize('xpath', [
        StartXpath.button_sousi_activated,
        StartXpath.button_nachinki_activated
        ])
    def test_button_nachinki_i_sousi_scroll_to_header(self, driver, xpath):
        driver.get(URLpage.START)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_personal_account)))
        driver.find_element(By.XPATH, xpath).click()
        assert driver.find_element(By.XPATH, xpath)

    def test_button_bulki_scroll_to_header(self, driver):
        driver.get(URLpage.START)
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, StartXpath.button_personal_account)))
        assert driver.find_element(By.XPATH, StartXpath.button_bulki_activated)
