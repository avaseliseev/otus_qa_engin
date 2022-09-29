from page_object.BasePage import BasePage


class CatalogPage(BasePage):
    CSS_BTN_ADD_COMPARE = '[class="fa fa-exchange"]'
    CSS_BTN_COMPARE_TOTAL = '#compare-total'
    CSS_INPUT_SORT = '[id=input-sort]'
    CSS_INPUT_SHOW = '[id=input-limit]'

    def add_product_compare(self):
        self.waiting_element(self.CSS_BTN_ADD_COMPARE).click()
        self.check_alert()

    def check_elements(self, dict_elements: dict):
        for element in dict_elements.values():
            element_page = self.waiting_element(element)
            element_page.click()
