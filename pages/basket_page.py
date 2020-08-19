from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_is_empty(self):
        assert self.browser.find_element(
            *BasketPageLocators.BASKET_CONTENT).text == "Your basket is empty. Continue shopping"
