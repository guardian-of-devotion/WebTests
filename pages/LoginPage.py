import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    QR_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    LOGIN_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//button[.//span[normalize-space()="Войти"]]')
    ENTER_BY_QR_CODE_BUTTON = (By.XPATH, '//button[.//span[normalize-space()="Войти по QR-коду"]]')
    RECOVERY_BUTTON = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[.//span[normalize-space()="Зарегистрироваться"]]')
    VK_BUTTON = (By.XPATH, '//i[@class="i ic social-icon __s __vk_id"]')
    MAILRU_BUTTON = (By.XPATH, '//i[@class="i ic social-icon __s __mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//i[@class="i ic social-icon __s __yandex"]')
    NO_LOGIN_ERROR_TEXT = (By.XPATH, '//span[text()="Введите логин"]')
    NO_PASSWORD_ERROR_TEXT = (By.XPATH, '//span[text()="Введите пароль"]')
    RESTORE_ACCOUNT_BUTTON = (By.XPATH, '//a[.//span[normalize-space()="Восстановить"]]')
    GO_BACK_BUTTON = ('//button[.//span[normalize-space()="Отмена"]]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.ENTER_BY_QR_CODE_BUTTON)
        self.find_element(LoginPageLocators.RECOVERY_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_BUTTON)
        self.find_element(LoginPageLocators.MAILRU_BUTTON)
        self.find_element(LoginPageLocators.YANDEX_BUTTON)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получаем текст ошибки отсутствия логина')
    def get_no_login_error_text(self):
        self.attach_screenshot()
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.NO_LOGIN_ERROR_TEXT)).text

    @allure.step('Получаем текст ошибки отсутствия пароля')
    def get_no_password_error_text(self):
        self.attach_screenshot()
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.NO_PASSWORD_ERROR_TEXT)).text

    @allure.step('Нажимаем на поле логина')
    def click_login_field(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_FIELD).click()

    @allure.step('Заполняем поле логина')
    def fill_login_field(self, login):
        self.driver.find_element(*LoginPageLocators.LOGIN_FIELD).send_keys(login)
        self.attach_screenshot()

    @allure.step('Заполняем поле пароля')
    def fill_password_field(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.attach_screenshot()

    @allure.step('Переходим к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.driver.find_element(*LoginPageLocators.RECOVERY_BUTTON).click()


