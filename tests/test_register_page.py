import time
from LINKS import URL_REGISTER_PAGE
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_register_form_if_name_email_pass_correct_go_auth_page(driver):
    name = f"Имя{datetime.now().strftime("%Y%m%d_%H%M%S")}"
    time.sleep(10)
    driver.get(URL_REGISTER_PAGE)
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/div/div/main/div/form/button'))
    )

    driver.find_element(By.CLASS_NAME, 'text input__textfield text_type_main-default').send_keys(name)
    time.sleep(10)