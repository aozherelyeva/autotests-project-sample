import pytest
from pages.main_page import MainPage

product_base_link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_can_go_to_login_link(browser, link):
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_should_see_login_link(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    basket_page = page.go_to_basket_page()
    basket_page.basket_should_be_empty()
    basket_page.should_be_message_empty_basket()