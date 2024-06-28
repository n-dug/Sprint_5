from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestStellarBurgers:
    def test_click_tabs(self, driver):
        WebDriverWait(driver, 5)
        driver.find_element(*Locators.SAUCES).click()
        WebDriverWait(driver, 5)
        driver.find_element(*Locators.TOPPINGS).click()
        WebDriverWait(driver, 5)
        driver.find_element(*Locators.BUNS).click()
        WebDriverWait(driver, 5)
        active_tab_class = driver.find_element(*Locators.BUNS).get_attribute('class')
        WebDriverWait(driver, 5)
        # проверка, что активна вкладка, на которую перешли с "Соусов" и "Начинок"
        assert 'current' in active_tab_class
