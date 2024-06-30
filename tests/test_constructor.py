from conftest import *
from locators import *


@pytest.mark.parametrize('tab1, tab2', [(Locators.SAUCES, Locators.BUNS),
                                        (Locators.TOPPINGS, Locators.SAUCES),
                                        (Locators.SAUCES, Locators.TOPPINGS)])
def test_current_tab(driver, tab1, tab2):
    driver.get(Constants.URL)
    driver.find_element(*tab1).click()
    current_tab = driver.find_element(*tab2)
    current_tab.click()
    tab = current_tab.get_attribute('class')
    assert 'current' in tab
