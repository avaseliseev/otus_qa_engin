from page_object.BasePage import BasePage


class HomePage(BasePage):
    CSS_LOGO = '#logo > a > img'
    TITLE = 'Your Store'
    _CSS_BTN_CURRENCY = '.btn-group'
    _CURRENCY_US = {'US': 'li:nth-child(1) [type="button"]'}
    _CURRENCY_EUR = {'EUR': 'li:nth-child(2) [type="button"]'}
    _CURRENCY_GBR = {'GBR': 'li:nth-child(3) [type="button"]'}
    _CSS_FOOTER = 'body > footer'
    _CSS_ROW = '.product-layout'

    def input_search_bar(self, name: str):
        self.input_value('[name=search]', name)
        self.waiting_element('.input-group-btn [type=button]').click()

    def input_currency(self, currency: str):
        self.waiting_element(self._CSS_BTN_CURRENCY).click()
        if currency == self._CURRENCY_US.keys():
            self.waiting_element(self._CURRENCY_US.values())
        elif currency == self._CURRENCY_EUR.keys():
            self.waiting_element(self._CURRENCY_EUR.values())
        elif currency == self._CURRENCY_GBR.keys():
            self.waiting_element(self._CURRENCY_GBR.values())

    @property
    def get_footer(self):
        return self.waiting_element(self._CSS_FOOTER)

    def click_on_the_specified_item(self, position: int):
        rows = self.find_all_elements(self._CSS_ROW)
        rows[position].click()
