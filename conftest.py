import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from constants import Constants
from locators import Locators


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*Locators.MAIN_AUTH_BUTTON).click()
    driver.find_element(*Locators.EMAIL_AUTH).send_keys(*Constants.EMAIL)
    driver.find_element(*Locators.PASSWORD_AUTH).send_keys(*Constants.RIGHT_PASSWORD)
    driver.find_element(*Locators.AUTH_BUTTON).click()
    return login
