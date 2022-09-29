from config import URL_ADMIN_PAGE
from page_object.BasePage import BasePage


class AdminPage(BasePage):
    _CSS_USER_NAME = '#input-username'
    _CSS_FORGOTTEN_PASS = '[href*=forgotten]'
    _CSS_MENU_CATALOG = '[id=menu-catalog]'
    _CSS_PRODUCT_PAGE = '[href*="product"]'
    _CSS_ADD_BUTTON = '.fa-plus'
    _CSS_DATA_PAGE = '[href*=data]'
    _CSS_SAVE_PRODUCT = '.fa-save'
    _CSS_PRODUCT_NAME = '[id=input-name]'
    _CSS_BUTTON_FILTER = '[id=button-filter]'
    _CSS_ALL_SELECT = '.text-center [onclick*=checked]'
    _CSS_DELETE = '.btn-danger'

    def input_user_name(self, user_name: str):
        self.input_value(self._CSS_USER_NAME, user_name)

    def filling_out_the_product_card(self, dict_elements: dict, admin_page: BasePage):
        for k, v in dict_elements.items():
            admin_page.input_value(v[1], v[0])

    def forgotten_click(self, admin_page: BasePage):
        admin_page.waiting_element(self._CSS_FORGOTTEN_PASS).click()

    def add_product(self, admin_page: BasePage):
        admin_page.waiting_element(self._CSS_MENU_CATALOG).click()
        admin_page.waiting_element(self._CSS_PRODUCT_PAGE).click()
        admin_page.waiting_element(self._CSS_ADD_BUTTON).click()

    def find_product_by_name(self, admin_page: BasePage, name: str):
        admin_page.waiting_element(self._CSS_MENU_CATALOG).click()
        admin_page.waiting_element(self._CSS_PRODUCT_PAGE).click()
        admin_page.waiting_element(self._CSS_PRODUCT_NAME).send_keys(name)
        admin_page.waiting_element(self._CSS_BUTTON_FILTER).click()

    def click_data_page(self, admin_page: BasePage):
        admin_page.waiting_element(self._CSS_DATA_PAGE).click()

    def click_button_save_product(self, admin_page: BasePage):
        admin_page.waiting_element(self._CSS_SAVE_PRODUCT).click()

    def delete_product(self, admin_page: BasePage):
        admin_page.waiting_element(self._CSS_ALL_SELECT).click()
        admin_page.waiting_element(self._CSS_DELETE).click()
