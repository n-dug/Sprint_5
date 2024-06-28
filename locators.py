from selenium.webdriver.common.by import By


class Locators:
    # поле "Имя" на форме регистрации
    NAME_REG = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    # поле "Email" на форме регистрации
    EMAIL_REG = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    # поле "Пароль" на форме регистрации
    PASSWORD_REG = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
    # кнопка "Войти" на форме регистрации
    AUTH_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    # кнопка "Войти" на главной странице
    MAIN_AUTH_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    # ссылка на регистрацию на форме авторизации
    REG_REF = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')
    # ссылка на авторизацию на форме регистрации
    AUTH_REF_FROM_REG = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')
    # кнопка регистрации
    REG_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    # кнопка "Личный кабинет" на главной странице
    ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')
    # поле "Email" на форме авторизации
    EMAIL_AUTH = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    # поле "Пароль" на форме авторизации
    PASSWORD_AUTH = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    # текст ошибки, что поле "Пароль" на форме регистрации заполнено неверно
    INCORRECT_PASSWORD_REG = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')
    # текст ошибки, что поле "Пароль" на форме авторизации заполнено неверно
    INCORRECT_PASSWORD_AUTH = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/p')
    # кнопка восстановления пароля
    RETRIEVE_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    # ссылка на восстановление пароля на форме авторизации
    RETRIEVE_REF = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a')
    # ссылка на авторизацию на форме восстановления
    RETRIEVE_AUTH = (By.CLASS_NAME, 'Auth_link__1fOlj')
    # поле "Email" на форме восстановления
    RETRIEVE_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    # поле "Пароль" на форме восстановления
    RETRIEVE_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    # поле кода на почту на форме восстановления
    ONE_TIME_PASSWORD = (By.XPATH, '//label[text()="Введите код из письма"]/following-sibling::input')
    # опция "Конструктор"
    CONSTRUCTOR = (By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p')
    # логотип сайта
    LOGO = (By.XPATH, '//div/a[@href= "/"]')
    # опция "Выйти" в личном кабинете
    SIGN_OUT = (By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button')
    # вкладка "Соусы"
    SAUCES = (By.XPATH, '//span[text()="Соусы"]/parent::div')
    # вкладка "Начинки"
    TOPPINGS = (By.XPATH, '//span[text()="Начинки"]/parent::div')
    # вкладка "Булки"
    BUNS = (By.XPATH, '//span[text()="Булки"]/parent::div')
