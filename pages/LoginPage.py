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

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
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

    def click_login(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def get_no_login_error_text(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.NO_LOGIN_ERROR_TEXT)).text

    def get_no_password_error_text(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LoginPageLocators.NO_PASSWORD_ERROR_TEXT)).text

    def click_login_field(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_FIELD).click()

    def fill_login_field(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_FIELD).send_keys("asadasds")