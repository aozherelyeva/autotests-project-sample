import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage

product_base_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    link = browser.current_url
    page = LoginPage(browser, link)
    page.should_be_login_page()


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_be_adding_confirmation()
    page.name_added_should_be_correct()


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.no_success_message()


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.no_success_message()


@pytest.mark.parametrize('link', [product_base_link])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.success_message_is_disappeared()


