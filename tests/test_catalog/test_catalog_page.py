from page_object import CatalogPage


def test_add_product_compare(run_driver_catalog_page: CatalogPage):
    catalog_page = run_driver_catalog_page
    catalog_page.add_product_compare()
    catalog_page.waiting_element(catalog_page.CSS_BTN_COMPARE_TOTAL).click()


def test_button_sort_by(run_driver_catalog_page: CatalogPage, dict_of_sorting_elements: dict):
    catalog_page = run_driver_catalog_page
    catalog_page.waiting_element(catalog_page.CSS_INPUT_SORT)
    catalog_page.check_elements(dict_of_sorting_elements)


def test_button_click_show(run_driver_catalog_page: CatalogPage, dict_of_show_elements: dict):
    catalog_page = run_driver_catalog_page
    catalog_page.waiting_element(catalog_page.CSS_INPUT_SHOW)
    catalog_page.check_elements(dict_of_show_elements)


def test_click_display(run_driver_catalog_page: CatalogPage, dict_view_elements):
    catalog_page = run_driver_catalog_page
    catalog_page.check_elements(dict_view_elements)
