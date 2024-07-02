import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from constants import Constants


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome()
    driver.get(Constants.URL)
    yield driver
    driver.quit()
