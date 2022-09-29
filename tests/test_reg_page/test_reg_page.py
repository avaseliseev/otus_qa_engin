import pytest

from page_object.RegPage import RegPage
from tests.test_reg_page.user_data import get_user_data, get_pass


@pytest.mark.parametrize('req_name',
                         ['First Name',
                          'Last Name',
                          'E-Mail',
                          'Telephone',
                          'Password',
                          'Password Confirm'])
def test_check_required_elements(run_driver_reg_page: RegPage, req_name: str):
    reg_page = run_driver_reg_page
    list_elements = reg_page.find_all_elements(reg_page.CSS_REG_DETAILS)
    assert req_name in reg_page.convert_tuple(list_elements)


def test_click_subscribe_panel(run_driver_reg_page: RegPage, reg_page=None):
    if reg_page is None:
        reg_page = run_driver_reg_page
    reg_page.click_subscribe_btn_no()
    reg_page.click_subscribe_btn_yes()


def test_privacy_policy(run_driver_reg_page: RegPage):
    reg_page = run_driver_reg_page
    reg_page.click_agree_policy()
    reg_page.check_privacy_policy()


def test_login_page(run_driver_reg_page: RegPage):
    reg_page = run_driver_reg_page
    reg_page.input_login_page(get_user_data()['First Name'], get_pass()['password'])
    reg_page.submit_click()


def test_created_account(run_driver_reg_page: RegPage):
    reg_page = run_driver_reg_page
    reg_page.input_user_data(get_user_data())
    reg_page.input_password_confirm(get_pass())
    test_click_subscribe_panel(reg_page)
    test_privacy_policy(reg_page)
    reg_page.submit_click()
    reg_page.check_text_create_account()
