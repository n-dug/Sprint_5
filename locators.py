from selenium.webdriver.common.by import By


class Locators:
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    AUTH_BUTTON = (By.XPATH, '//button[@class="auth-form__button"]')
    STATUS_MESSAGE = (By.XPATH, '//p[@class="popup__status-message"]')