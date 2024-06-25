import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get(Constants.URL)
    yield browser

    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.EMAIL).send_keys(Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD).send_keys(Constants.PASSWORD)
    driver.find_element(*Locators.AUTH_BUTTON).click()
    return driver