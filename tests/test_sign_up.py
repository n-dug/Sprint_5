from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import *
from locators import *
faker = Faker()


class TestSignUp:
    def test_sign_up_from_main(self, driver):
        email = faker.email()
        name = faker.name()
        password = faker.password()
        driver.find_element(*Locators.MAIN_PAGE_SIGN_IN_BUTTON).click()
        # регистрация
        driver.find_element(*Locators.SIGN_UP_REF).click()
        driver.find_element(*Locators.SIGN_UP_BUTTON).click()
        driver.find_element(*Locators.SIGN_UP_NAME).send_keys(name)
        driver.find_element(*Locators.SIGN_UP_EMAIL).send_keys(email)
        driver.find_element(*Locators.SIGN_UP_PASSWORD).send_keys(password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SIGN_UP_BUTTON))
        driver.find_element(*Locators.SIGN_UP_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_matches(Constants.URL_LOG))
        # авторизация
        driver.find_element(*Locators.SIGN_IN_EMAIL).send_keys(email)
        driver.find_element(*Locators.SIGN_IN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_PROFILE))
        assert driver.current_url == Constants.URL_PROFILE

    def test_sign_up_from_account(self, driver):
        email = faker.email()
        name = faker.name()
        password = faker.password()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # регистрация
        driver.find_element(*Locators.SIGN_UP_REF).click()
        driver.find_element(*Locators.SIGN_UP_BUTTON).click()
        driver.find_element(*Locators.SIGN_UP_NAME).send_keys(name)
        driver.find_element(*Locators.SIGN_UP_EMAIL).send_keys(email)
        driver.find_element(*Locators.SIGN_UP_PASSWORD).send_keys(password)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SIGN_UP_BUTTON))
        driver.find_element(*Locators.SIGN_UP_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_matches(Constants.URL_LOG))
        # авторизация
        driver.find_element(*Locators.SIGN_IN_EMAIL).send_keys(email)
        driver.find_element(*Locators.SIGN_IN_PASSWORD).send_keys(password)
        driver.find_element(*Locators.SIGN_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_PROFILE))
        assert driver.current_url == Constants.URL_PROFILE

    def test_sign_up_wrong_password(self, driver):
        email = faker.email()
        name = faker.name()
        driver.find_element(*Locators.MAIN_PAGE_SIGN_IN_BUTTON).click()
        driver.find_element(*Locators.SIGN_UP_REF).click()
        driver.find_element(*Locators.SIGN_UP_BUTTON).click()
        driver.find_element(*Locators.SIGN_UP_NAME).send_keys(name)
        driver.find_element(*Locators.SIGN_UP_EMAIL).send_keys(email)
        # ввод пароля < 6 символов
        driver.find_element(*Locators.SIGN_UP_PASSWORD).send_keys(Constants.WRONG_PASSWORD)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable(Locators.SIGN_UP_BUTTON))
        driver.find_element(*Locators.SIGN_UP_BUTTON).click()
        mess = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD)).text
        assert mess == 'Некорректный пароль'
