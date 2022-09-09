from selenium import webdriver

from config import LOGIN, PASSWORD, TELEPHONE, EMAIL
from service import wait_element


def send_personal_details(driver: webdriver, timeout: float):
    # input First Name
    wait_element('#input-firstname', driver, timeout=timeout).send_keys(LOGIN)
    # input Last Name
    wait_element('#input-lastname', driver, timeout=timeout).send_keys(LOGIN)
    # input email
    wait_element('#input-email', driver, timeout=timeout).send_keys(EMAIL)
    # input telephone
    wait_element('#input-telephone', driver, timeout=timeout).send_keys(TELEPHONE)


def send_password(driver: webdriver, timeout: float):
    # input Password
    wait_element('#input-password', driver, timeout=timeout).send_keys(PASSWORD)
    # input Password Confirm
    wait_element('#input-confirm', driver, timeout=timeout).send_keys(PASSWORD)
