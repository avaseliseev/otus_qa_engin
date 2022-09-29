import random

from page_object.BasePage import BasePage


class CardProductPage(BasePage):
    _CSS_INPUT_NAME = '#input-name'
    _CSS_INPUT_REVIEW = '[id=input-review]'
    _CSS_SEND_REVIEW = '#button-review.btn-primary'
    _CSS_RATING_GOOD = '[type=radio]:last-child'
    _CSS_REVIEW_BTN = '[href*=tab-review]'
    _CSS_HEAD_PROD_IMAC = '.breadcrumb > li:nth-child(4) > a'
    _CSS_TITLE_PROD_IMAC = 'div.col-sm-4:nth-child(2) > h1'
    CSS_DESCRIPTION_BTN = '[href*=description]'
    CSS_DESCRIPTION_PRODUCT = '#tab-description.active'
    _CSS_BTN_LEFT = 'button.mfp-arrow:nth-child(3)'
    _CSS_BTN_RIGHT = 'button.mfp-arrow:nth-child(4)'
    _CSS_IMAGE_PROD = '.thumbnails > li:nth-child(1) > a:nth-child(1) > img'
    _CSS_BTN_IMAGE_CLS = '.mfp-close'
    CSS_PRICE_TEXT = 'li h2'
    CSS_TAX_TEXT = 'div.col-sm-4:nth-child(2) > ul:nth-child(4) > li:nth-child(2)'
    _CSS_COUNT = '#input-quantity'
    _CSS_RANDOM_COUNT = str(random.randint(1, 10))
    _CSS_BTN_CART = '#button-cart'

    def input_name(self, login: str):
        self.input_value(self._CSS_INPUT_NAME, login)

    def input_review(self, text: str):
        self.input_value(self._CSS_INPUT_REVIEW, text)

    @property
    def find_name_product(self):
        head_elem = self.waiting_element(self._CSS_HEAD_PROD_IMAC)
        right_elem = self.waiting_element(self._CSS_TITLE_PROD_IMAC)
        return head_elem, right_elem

    def input_description(self, name: str, review: str):
        self.waiting_element(self._CSS_REVIEW_BTN).click()
        self.input_name(name)
        self.input_review(review)
        self.waiting_element(self._CSS_RATING_GOOD).click()

    def click_btn_review(self):
        self.waiting_element(self._CSS_SEND_REVIEW).click()

    def _click_image_left(self):
        self.waiting_element(self._CSS_BTN_LEFT).click()

    def _click_image_right(self):
        self.waiting_element(self._CSS_BTN_RIGHT).click()

    def check_images_product(self):
        self.waiting_element(self._CSS_IMAGE_PROD).click()
        self._click_image_right()
        self._click_image_right()
        self._click_image_left()
        self.waiting_element(self._CSS_BTN_IMAGE_CLS).click()

    def add_product_basket(self):
        self.input_value(self._CSS_COUNT, self._CSS_RANDOM_COUNT)
        self.waiting_element(self._CSS_BTN_CART).click()
