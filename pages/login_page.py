from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        """Проверяем, что находимся на странице регистрации"""

        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяем, что текущая ссылка это содержит login"""

        assert self.browser.current_url.find("login") != 0, "Is not login url"

    def should_be_login_form(self):
        """Проверяем, что форма авторизации есть"""

        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        """Проверяем, что форма регистрации есть"""

        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form not found"

    def register_new_user(self, email, password):
        """Регистрация нового пользователя"""

        self.browser.find_element(
            *LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.PASSWORD).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REG_BTN).click()
