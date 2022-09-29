from selenium import webdriver

from config import LOGIN, PASSWORD, EMAIL
from page_object import AdminPage


def test_check_page_title(run_driver_admin_page: AdminPage, base_url: str, driver: webdriver, check_title: tuple):
    admin_page = run_driver_admin_page
    admin_page.waiting_title(*check_title)


def test_check_username(run_driver_admin_page: AdminPage):
    admin_page = run_driver_admin_page
    admin_page.input_user_name(LOGIN)
    return admin_page


def test_check_password(run_driver_admin_page: AdminPage, get_login=False):
    if get_login:
        admin_page = test_check_username(run_driver_admin_page)
    else:
        admin_page = run_driver_admin_page
    admin_page.input_password(PASSWORD)
    return admin_page


def test_button_login(run_driver_admin_page: AdminPage):
    admin_page = test_check_password(run_driver_admin_page, get_login=True)
    admin_page.submit_click()
    return admin_page


def test_forgotten_password(run_driver_admin_page: AdminPage):
    admin_page = run_driver_admin_page
    admin_page.forgotten_click(admin_page)
    admin_page.input_email(EMAIL)
    admin_page.submit_click()


def test_add_product_button(run_driver_admin_page: AdminPage):
    admin_page = test_button_login(run_driver_admin_page)
    admin_page.add_product(admin_page)
    return admin_page


def test_add_product_to_catalog(run_driver_admin_page: AdminPage, data_for_page_general: dict,
                                data_for_page_data: dict):
    admin_page = test_add_product_button(run_driver_admin_page)
    admin_page.filling_out_the_product_card(data_for_page_general, admin_page)
    admin_page.click_data_page(admin_page)
    admin_page.filling_out_the_product_card(data_for_page_data, admin_page)
    admin_page.click_button_save_product(admin_page)


def test_delete_product(run_driver_admin_page: AdminPage, data_for_page_general: dict):
    admin_page = test_button_login(run_driver_admin_page)
    name_product = list(data_for_page_general.values())[0][0]
    admin_page.find_product_by_name(admin_page, name_product)
    admin_page.delete_product(admin_page)
    admin_page.get_alert.accept()
