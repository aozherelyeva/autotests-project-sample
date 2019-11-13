from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT)

    def should_be_message_empty_basket(self):
        assert 'Your basket is empty' in self.browser.find_element(*BasketPageLocators.NO_ITEMS_CONFIRMATION).text
