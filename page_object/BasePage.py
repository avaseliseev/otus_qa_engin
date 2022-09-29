import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _CSS_ALERT = '.alert-success'
    _CSS_SUBMIT = '[type=submit]'
    _CSS_EMAIL = '#input-email'
    _CSS_PASSWORD = '#input-password'

    def __init__(self, driver, path=None):
        self.driver = driver
        self.path = path

    def waiting_title(self, title: str, timeout=2):
        try:
            return WebDriverWait(driver=self.driver, timeout=timeout).until(EC.title_is(title=title))
        except TimeoutException:
            raise AssertionError(f'Ожидаемый результат {title}, фактический {self.driver.title}')

    def waiting_element(self, selector: str, by=By.CSS_SELECTOR, timeout=2):
        try:
            return WebDriverWait(driver=self.driver, timeout=timeout).until(
                EC.visibility_of_element_located((by, selector)))
        except TimeoutException:
            raise AssertionError(f'Селектор {selector} не найден')

    def find_all_elements(self, selector: str, by=By.CSS_SELECTOR, timeout=2) -> object:
        try:
            time.sleep(timeout)
            return self.driver.find_elements(by, selector)
        except TimeoutException:
            raise AssertionError(f'Селектор {selector} не найден')

    def open_browser(self, driver: webdriver, base_url: str, path=None):
        if path is None:
            path = ''
        driver.get(f'{base_url}{path}')

    @property
    def get_alert(self) -> Alert:
        return WebDriverWait(self.driver, 2).until((EC.alert_is_present()))

    def input_value(self, css_selector: str, value: str):
        self.waiting_element(css_selector).clear()
        self.waiting_element(css_selector).send_keys(value)

    def check_alert(self):
        self.waiting_element(self._CSS_ALERT)

    def submit_click(self):
        self.waiting_element(self._CSS_SUBMIT).click()

    def input_email(self, email: str):
        self.input_value(self._CSS_EMAIL, email)

    def input_password(self, password: str):
        self.input_value(self._CSS_PASSWORD, password)
