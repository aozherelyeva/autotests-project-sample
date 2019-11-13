from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group > a.btn")


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators(object):
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1)")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-success:nth-child(1) div.alertinner strong")


class BasketPageLocators(object):
    BASKET_CONTENT = (By.CSS_SELECTOR, ".basket_summary")
    NO_ITEMS_CONFIRMATION = (By.CSS_SELECTOR, "#content_inner p")
