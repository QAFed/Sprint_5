import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    web_driver = webdriver.Chrome(service=service)
    yield web_driver
    web_driver.quit()


