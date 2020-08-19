from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        """Нажимаем кнопку 'Добавить в корзину' """

        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_button.click()

    def go_to_basket_page(self):
        """Переход в корзину

        Так как корзина доступна не со всех страниц, то логично реализовать ее в классе ProductPage.
        Если реализовать в BasePage, то можно поймать ошибку в случае перехода например со страницы авторизации
        """

        basket_link = self.browser.find_element(
            *ProductPageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_message_about_adding(self):
        """Проверяем сообщение о добавлении товара"""

        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text + " has been added to your basket."
        message = self.browser.find_element(
            *ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message, "No product name in the message"

    def should_be_message_basket_total(self):
        """Проверяем цену товара добавленную в корзину"""

        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        message_basket_total = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        """Ожидаем, что сообщение о добавлении не появится"""

        assert self.is_not_element_present(
            *ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        """Ожидаем, что сообщение о добавлении исчезнет"""

        assert self.is_disappeared(
            *ProductPageLocators.MESSAGE_ABOUT_ADDING), "Success message is presented, but should be disappeared"
