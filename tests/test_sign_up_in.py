from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import *
faker = Faker()


class TestStellarBurgers:
    def test_sign_up_and_in_from_main(self, driver):
        email = faker.email()
        name = faker.name()
        # пользователь кликает кнопку «Войти в аккаунт» на главной
        driver.find_element(*Locators.MAIN_AUTH_BUTTON).click()
        # регистрация
        driver.find_element(*Locators.REG_REF).click()
        driver.find_element(*Locators.NAME_REG).send_keys(name)
        driver.find_element(*Locators.EMAIL_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REG).send_keys(Constants.RIGHT_PASSWORD)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REG_BUTTON))
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_matches(Constants.URL_LOG))
        # авторизация
        driver.find_element(*Locators.EMAIL_AUTH).send_keys(email)
        driver.find_element(*Locators.PASSWORD_AUTH).send_keys(Constants.RIGHT_PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
        # переход по клику в личный кабинет с главной страницы
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_PROFILE))
        assert driver.current_url == Constants.URL_PROFILE

    def test_sign_up_wrong_password(self, driver):
        email = faker.email()
        name = faker.name()
        driver.find_element(*Locators.MAIN_AUTH_BUTTON).click()
        driver.find_element(*Locators.REG_REF).click()
        driver.find_element(*Locators.NAME_REG).send_keys(name)
        driver.find_element(*Locators.EMAIL_REG).send_keys(email)
        # ввод пароля < 6 символов
        driver.find_element(*Locators.PASSWORD_REG).send_keys(Constants.WRONG_PASSWORD)
        WebDriverWait(driver, 100).until(EC.element_to_be_clickable(Locators.REG_BUTTON))
        driver.find_element(*Locators.REG_BUTTON).click()
        mess = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD_REG)).text
        assert mess == 'Некорректный пароль'

    def test_sign_up_and_in_from_account(self, driver):
        email = faker.email()
        name = faker.name()
        # пользователь кликает кнопку «Личный кабинет» на главной
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        # регистрация
        driver.find_element(*Locators.REG_REF).click()
        driver.find_element(*Locators.NAME_REG).send_keys(name)
        driver.find_element(*Locators.EMAIL_REG).send_keys(email)
        driver.find_element(*Locators.PASSWORD_REG).send_keys(Constants.RIGHT_PASSWORD)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.REG_BUTTON))
        driver.find_element(*Locators.REG_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_matches(Constants.URL_LOG))
        # авторизация
        driver.find_element(*Locators.EMAIL_AUTH).send_keys(email)
        driver.find_element(*Locators.PASSWORD_AUTH).send_keys(Constants.RIGHT_PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.ACCOUNT_BUTTON))
        # переход по клику в личный кабинет с главной страницы
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_PROFILE))
        assert driver.current_url == Constants.URL_PROFILE
