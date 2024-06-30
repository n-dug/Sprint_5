from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import *
from locators import *

faker = Faker()


def test_account_to_constructor_link(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.MAIN_PAGE_SIGN_IN_BUTTON))
    driver.find_element(*Locators.MAIN_PAGE_SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_EMAIL))
    driver.find_element(*Locators.SIGN_IN_EMAIL).send_keys(*Constants.EMAIL)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_PASSWORD))
    driver.find_element(*Locators.SIGN_IN_PASSWORD).send_keys(*Constants.RIGHT_PASSWORD)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_BUTTON))
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.CONSTRUCTOR).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCTOR))
    assert driver.current_url == Constants.URL_S


def test_account_to_constructor_logo(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.MAIN_PAGE_SIGN_IN_BUTTON))
    driver.find_element(*Locators.MAIN_PAGE_SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_EMAIL))
    driver.find_element(*Locators.SIGN_IN_EMAIL).send_keys(*Constants.EMAIL)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_PASSWORD))
    driver.find_element(*Locators.SIGN_IN_PASSWORD).send_keys(*Constants.RIGHT_PASSWORD)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_BUTTON))
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    driver.find_element(*Locators.LOGO).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.CONSTRUCTOR))
    assert driver.current_url == Constants.URL_S
