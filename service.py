from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

SORT_NAME_DICT = {
    'Default': 'option:nth-of-type(1)',
    'Name (A - Z)': 'option:nth-of-type(2)',
    'Name (Z - A)': 'option:nth-of-type(3)',
    'Price (Low > High)': 'option:nth-of-type(4)',
    'Price (High > Low)': 'option:nth-of-type(5)',
    'Rating (Highest)': 'option:nth-of-type(6)',
    'Rating (Lowest)': 'option:nth-of-type(7)',
    'Model (A - Z)': 'option:nth-of-type(8)',
    'Model (Z - A)': 'option:nth-of-type(9)'
}

SHOW_NAME_DICT = {
    'show 15': 'option:nth-of-type(1)',
    'show 25': 'option:nth-of-type(2)',
    'show 50': 'option:nth-of-type(3)',
    'show 75': 'option:nth-of-type(4)',
    'show 100': 'option:nth-of-type(5)'
}


def wait_title(title: str, driver: webdriver, timeout=4):
    try:
        return WebDriverWait(driver=driver, timeout=timeout).until(EC.title_is(title=title))
    except TimeoutException:
        raise AssertionError(f'Ожидаемый результат {title}, фактический {driver.title}')


def wait_element(selector: str, driver: webdriver, by=By.CSS_SELECTOR, timeout=2):
    try:
        return WebDriverWait(driver=driver, timeout=timeout).until(EC.visibility_of_element_located((by, selector)))
    except TimeoutException:
        raise AssertionError(f'Селектор {selector} не найден')

