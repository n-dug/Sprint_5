from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators

faker = Faker()


def test_sign_in(driver):
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
    WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_PROFILE))
    assert driver.current_url == Constants.URL_PROFILE


def test_sign_in_from_sign_up(driver):
    # проверка входа в сущ. аккаунт с формы регистрации
    driver.find_element(*Locators.MAIN_PAGE_SIGN_IN_BUTTON).click()
    driver.find_element(*Locators.SIGN_UP_REF).click()
    driver.find_element(*Locators.AUTH_REF_FROM_REG).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_EMAIL))
    driver.find_element(*Locators.SIGN_IN_EMAIL).send_keys(*Constants.EMAIL)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_PASSWORD))
    driver.find_element(*Locators.SIGN_IN_PASSWORD).send_keys(*Constants.RIGHT_PASSWORD)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_BUTTON))
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.ACCOUNT_BUTTON))
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.url_contains(Constants.URL_PROFILE))
    assert driver.current_url == Constants.URL_PROFILE


def test_sign_in_wrong_password(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.MAIN_PAGE_SIGN_IN_BUTTON))
    driver.find_element(*Locators.MAIN_PAGE_SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_EMAIL))
    driver.find_element(*Locators.SIGN_IN_EMAIL).send_keys(*Constants.EMAIL)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_PASSWORD))
    driver.find_element(*Locators.SIGN_IN_PASSWORD).send_keys(*Constants.WRONG_PASSWORD)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_BUTTON))
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    mess = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD)).text
    assert mess == 'Некорректный пароль'


def test_retrieve_password(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.MAIN_PAGE_SIGN_IN_BUTTON))
    driver.find_element(*Locators.MAIN_PAGE_SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.RETRIEVE_REF))
    driver.find_element(*Locators.RETRIEVE_REF).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_EMAIL))
    driver.find_element(*Locators.SIGN_IN_EMAIL).send_keys(Constants.EMAIL)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.RETRIEVE_BUTTON))
    driver.find_element(*Locators.RETRIEVE_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.RETRIEVE_PASSWORD))
    driver.find_element(*Locators.RETRIEVE_PASSWORD).send_keys(Constants.RETRIEVE_PASSWORD)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.ONE_TIME_PASSWORD))
    driver.find_element(*Locators.ONE_TIME_PASSWORD).send_keys(Constants.ONE_TIME_PASSWORD)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SAVE_BUTTON))
    mess = driver.find_element(*Locators.SAVE_BUTTON).text
    assert mess == 'Сохранить'


def test_sign_out(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.MAIN_PAGE_SIGN_IN_BUTTON))
    driver.find_element(*Locators.MAIN_PAGE_SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_EMAIL))
    driver.find_element(*Locators.SIGN_IN_EMAIL).send_keys(*Constants.EMAIL)
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(Locators.SIGN_IN_PASSWORD))
    driver.find_element(*Locators.SIGN_IN_PASSWORD).send_keys(*Constants.RIGHT_PASSWORD)
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SIGN_IN_BUTTON))
    driver.find_element(*Locators.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ACCOUNT_BUTTON))
    driver.find_element(*Locators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.SIGN_OUT))
    driver.find_element(*Locators.SIGN_OUT).click()
    WebDriverWait(driver, 2).until(EC.element_to_be_clickable(Locators.SIGN_IN_BUTTON))
    text = driver.find_element(*Locators.SIGN_IN_BUTTON).text
    assert text == 'Войти'
