from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    SWITCH_TO_QR_CODE_BUTTON = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    SWITCH_TO_LOGIN_BUTTON = (By.XPATH, '//a[@data-l="t,login_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//button[.//span[normalize-space()="Войти"]]')
    ENTER_BY_QR_CODE_BUTTON = (By.XPATH, '//button[.//span[normalize-space()="Войти по QR-коду"]]')
    RECOVERY_BUTTON = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[.//span[normalize-space()="Зарегистрироваться"]]')
    VK_BUTTON = (By.CLASS_NAME, 'i ic social-icon __s __vk_id')
    MAILRU_BUTTON = (By.CLASS_NAME, 'i ic social-icon __s __mailru')
    YANDEX_BUTTON = (By.CLASS_NAME, 'i ic social-icon __s __yandex')

class LoginPageHelper(BasePage):
    pass
