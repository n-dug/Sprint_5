from selenium.webdriver.common.by import By


class Locators:
    # поле "Имя" на форме регистрации
    SIGN_UP_NAME = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')
    # поле "Email" на форме регистрации
    SIGN_UP_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    # поле "Пароль" на форме регистрации
    SIGN_UP_PASSWORD = (By.XPATH, '//label[text()="Пароль"]/following-sibling::input')
    # кнопка регистрации
    SIGN_UP_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
    # ссылка на авторизацию на форме регистрации
    AUTH_REF_FROM_REG = (By.CSS_SELECTOR, 'a[href="/login"]')
    # поле "Пароль" на форме авторизации
    SIGN_IN_PASSWORD = (By.NAME, 'Пароль')
    # ошибка пароля
    INCORRECT_PASSWORD = (By.XPATH, '//p[@class="input__error text_type_main-default"]')
    # вход с главной страницы
    MAIN_PAGE_SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # email для авторизации
    SIGN_IN_EMAIL = (By.NAME, 'name')
    # кнопка "Войти" на форме авторизации, регистрации и на главной странице
    SIGN_IN_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")
    # кнопка "Войти", если есть аккаунт
    SIGN_IN_EXIST_ACCOUNT = (By.CSS_SELECTOR, 'a[href="/login"]')
    # страница входа
    SIGN_IN_PAGE = (By.XPATH, '//h2[text()="Вход"]')
    # ссылка на регистрацию на форме авторизации
    SIGN_UP_REF = (By.CSS_SELECTOR, 'a[href="/register"]')
    # кнопка "Личный кабинет" на главной странице
    ACCOUNT_BUTTON = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    # кнопка восстановления пароля
    RETRIEVE_BUTTON = (By.XPATH, "//button[contains(text(),'Восстановить')]")
    # ссылка на восстановление пароля на форме авторизации
    RETRIEVE_REF = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')
    # ссылка на авторизацию на форме восстановления
    RETRIEVE_AUTH = (By.CLASS_NAME, 'Auth_link__1fOlj')
    # поле кода на почту на форме восстановления
    ONE_TIME_PASSWORD = (By.XPATH, '//input[@name="name"]')
    # поле для нового пароля
    RETRIEVE_PASSWORD = (By.NAME, 'Введите новый пароль')
    # кнопка "Сохранить" на ф. восстановления
    SAVE_BUTTON = (By.XPATH, "//button[contains(text(),'Сохранить')]")
    # опция "Конструктор"
    CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # кнопка "Собери бургер"
    TEXT_CONSTRUCTOR = (By.XPATH, '//h1[contains(text(),"Соберите бургер")]')
    # логотип сайта
    LOGO = (By.XPATH, '//div/a[@href= "/"]')
    # вкладка "Соусы"
    SAUCES = (By.XPATH, '//span[text()="Соусы"]/parent::div')
    # вкладка "Начинки"
    TOPPINGS = (By.XPATH, '//span[text()="Начинки"]/parent::div')
    # вкладка "Булки"
    BUNS = (By.XPATH, '//span[text()="Булки"]/parent::div')
    # опция "Выйти" в личном кабинете
    SIGN_OUT = (By.XPATH, "//button[text()='Выход']")
    # заполненный Email в ЛК
    EMAIL_IN_ACCOUNT = (By.XPATH, '//input[@name="name"]')
