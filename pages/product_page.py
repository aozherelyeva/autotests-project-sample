from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_adding_confirmation(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not present"

    def name_added_should_be_correct(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        added_item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_MESSAGE).text
        assert item_name in added_item_name, "The added item's name is not corresponding with the item's name"
