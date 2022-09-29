from config import LOGIN
from page_object import CardProductPage


def test_check_name_product(run_driver_card_page: CardProductPage, name_product: str):
    card_page = run_driver_card_page
    element_head, element_right_bar = card_page.find_name_product
    assert element_head.text == name_product
    assert element_right_bar.text == name_product


def test_check_description(run_driver_card_page: CardProductPage):
    card_page = run_driver_card_page
    card_page.waiting_element(card_page.CSS_DESCRIPTION_BTN)
    card_page.waiting_element(card_page.CSS_DESCRIPTION_PRODUCT)


def test_post_review(run_driver_card_page: CardProductPage, text_for_review: str):
    card_page = run_driver_card_page
    card_page.input_description(name=LOGIN, review=text_for_review)
    card_page.click_btn_review()
    card_page.check_alert()


def test_click_images(run_driver_card_page: CardProductPage):
    card_page = run_driver_card_page
    card_page.check_images_product()


def test_check_tax_product(run_driver_card_page: CardProductPage):
    card_page = run_driver_card_page
    card_page.waiting_element(card_page.CSS_PRICE_TEXT)
    card_page.waiting_element(card_page.CSS_TAX_TEXT)


def test_product_add_basket(run_driver_card_page: CardProductPage):
    card_page = run_driver_card_page
    card_page.add_product_basket()
    card_page.check_alert()
