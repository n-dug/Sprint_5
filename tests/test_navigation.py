from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import *
faker = Faker()


class TestStellarBurgers:
    def test_account_to_constructor_link(self, driver, login):
        WebDriverWait(driver, 5)
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5)
        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCTOR))
        assert driver.current_url == Constants.URL_LOGO

    def test_account_to_constructor_logo(self, driver, login):
        WebDriverWait(driver, 5)
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5)
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCTOR))
        assert driver.current_url == Constants.URL_LOGO
