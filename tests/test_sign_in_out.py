from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators

faker = Faker()


class TestStellarBurgers:
    def test_sign_in_wrong_password(self, driver):
        email = faker.email()
        name = faker.name()
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
        # ввод не того пароля, который был указан при регистрации
        driver.find_element(*Locators.PASSWORD_AUTH).send_keys(Constants.WRONG_PASSWORD)
        driver.find_element(*Locators.AUTH_BUTTON).click()
        mess = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD_AUTH)).text
        assert mess == 'Некорректный пароль'

    def test_retrieve_password(self, driver):
        driver.find_element(*Locators.MAIN_AUTH_BUTTON).click()
        # пользователь нажимает ссылку «Восстановить пароль» на форме входа
        driver.find_element(*Locators.RETRIEVE_REF).click()
        WebDriverWait(driver, 5).until(EC.url_matches(Constants.FORGOT_PASSWORD))
        driver.find_element(*Locators.RETRIEVE_EMAIL).send_keys(Constants.EMAIL)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.RETRIEVE_BUTTON))
        driver.find_element(*Locators.RETRIEVE_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_RESET))
        driver.find_element(*Locators.RETRIEVE_PASSWORD).send_keys(Constants.RETRIEVE_PASSWORD)
        driver.find_element(*Locators.ONE_TIME_PASSWORD).send_keys(Constants.ONE_TIME_PASSWORD)
        assert driver.current_url == Constants.URL_RESET

    def test_sign_in_from_retrieve(self, driver):
        driver.find_element(*Locators.MAIN_AUTH_BUTTON).click()
        driver.find_element(*Locators.RETRIEVE_REF).click()
        WebDriverWait(driver, 5).until(EC.url_matches(Constants.FORGOT_PASSWORD))
        driver.find_element(*Locators.RETRIEVE_AUTH).click()
        WebDriverWait(driver, 5)
        assert driver.current_url == Constants.URL_LOG

    def test_sign_out(self, driver, login):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
        # переход по клику в личный кабинет с главной страницы
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_PROFILE))
        # выход по кнопке «Выйти» в личном кабинете
        driver.find_element(*Locators.SIGN_OUT).click()
        WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_LOG))
        assert driver.current_url == Constants.URL_LOG
