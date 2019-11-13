import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
main_link = "http://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.login
class TestLoginFromProductPage:
    @pytest.mark.parametrize('link', [product_base_link])
    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    @pytest.mark.parametrize('link', [product_base_link])
    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)
        page.should_be_login_page()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "@fakepass"
        login_page = LoginPage(browser, main_link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.parametrize('link', [product_base_link])
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_item_to_basket()
        page.should_be_adding_confirmation()
        page.name_added_should_be_correct()

    @pytest.mark.parametrize('link', [product_base_link])
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.no_success_message()


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_can_add_product_to_basket(self, browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_be_adding_confirmation()
    page.name_added_should_be_correct()


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_cant_see_success_message(self, browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.no_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', [product_base_link])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.no_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', [product_base_link])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.success_message_is_disappeared()


@pytest.mark.parametrize('link', [product_base_link])
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, browser.current_url)
    page.basket_should_be_empty()
    page.should_be_message_empty_basket()
