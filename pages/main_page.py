from settings import *
from .locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get('https://b2c.passport.rt.ru/')

    def is_loaded(self) -> bool:
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.presence_of_element_located(Locators.username_locator))
            return True
        except:
            return False


class AuthForm(MainPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.load()
        self.is_loaded()
        self.wait = WebDriverWait(self.driver, timeout=10)


    # EXP-003 - Успешная проверка автосмены "плесхолдера" при переключении таба "Телефон", "Почта", "Логин", "Лицевой счет"
    def tab_and_placeholder(self):
        self.driver.find_element(*Locators.username_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.placeholder, text_="Мобильный телефон"))
        self.driver.find_element(*Locators.email_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.placeholder, text_="Электронная почта"))
        self.driver.find_element(*Locators.login_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.placeholder, text_="Логин"))
        self.driver.find_element(*Locators.personal_account).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.placeholder, text_="Лицевой счёт"))


    # EXP-004 - успешная авторизация клиента по номеру телефона с неверными данными
    def authorization_by_phone(self):
        self.driver.find_element(*Locators.username_locator).send_keys(valid_phone)
        self.driver.find_element(*Locators.password_locator).send_keys(valid_pass)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.user_name, text_="Смаль"), message='login failed')
        print("login success")


    # EXP-005 - Не успешная авторизация клиента по номеру телефона с неверными данными
    def failed_authorization_by_phone(self):
        self.driver.find_element(*Locators.username_locator).send_keys(invalid_phone)
        self.driver.find_element(*Locators.password_locator).send_keys(invalid_pass)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message, text_="Неверный логин или пароль"))
        print("login failed")


    # EXP-006 - Успешная авторизация клиента c корректным email и паролем
    def authorization_by_email(self):
        self.driver.find_element(*Locators.email_locator).click()
        self.driver.find_element(*Locators.username_locator).send_keys(valid_email)
        self.driver.find_element(*Locators.password_locator).send_keys(valid_pass_email)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.user_name, text_="Иванов"), message='login failed')
        print("login success")


    # EXP-007 - Не успешная авторизация клиента с помощью не корректной электронной почты и пароля
    def failed_authorization_by_email(self):
        self.driver.find_element(*Locators.email_locator).click()
        self.driver.find_element(*Locators.username_locator).send_keys(invalid_email)
        self.driver.find_element(*Locators.password_locator).send_keys(invalid_pass_email)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message, text_="Неверный логин или пароль"))
        print("login failed")


    # EXP-008 - Успешная авторизация клиента по логину
    def authorization_by_login(self):
        self.driver.find_element(*Locators.login_locator).click()
        self.driver.find_element(*Locators.username_locator).send_keys(valid_login)
        self.driver.find_element(*Locators.password_locator).send_keys(valid_pass)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.user_name, text_="Смаль"), message='login failed')
        print("login success")


    # EXP-009 - Не успешная авторизация клиента с помощью неверного логина и пароля
    def failed_authorization_by_login(self):
        self.driver.find_element(*Locators.login_locator).click()
        self.driver.find_element(*Locators.username_locator).send_keys(invalid_login)
        self.driver.find_element(*Locators.password_locator).send_keys(invalid_pass)
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message, text_="Неверный логин или пароль"))
        print("login failed")


    # EXP-018 - Проверить основные элементы на странице "Восстановление пароля"
    def form_password_recovery(self):
        self.driver.find_element(*Locators.password_recovery).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.title, text_="Восстановление пароля"))
        self.driver.save_screenshot('form_password_recover.png')


    # EXP-022 Проверка основных элементов на странице форма регистрации
    def form_registration(self):
        self.driver.find_element(*Locators.registration).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.title, text_="Регистрация"))
        self.driver.save_screenshot('form_registration.png')


    # EXP-023 Авторизация через соцсеть Вконтакте
    def auth_by_vk(self):
        self.driver.find_element(*Locators.vk).click()


    # EXP-024 Авторизация через соцсеть Одноклассники
    def auth_by_ok(self):
        self.driver.find_element(*Locators.ok).click()


    # EXP-025 Авторизация через соцсеть Мой мир
    def auth_by_my_mail(self):
        self.driver.find_element(*Locators.my_mail).click()


    # EXP-027 Корректная работа ссылки с "Политикой конфиденциальности"
    def privacy_policy(self):
        self.driver.find_element(*Locators.privacy_policy).click()


    # EXP-028  проверка авторизации с пустыми полями.
    def failed_authorization_with_empty(self):
        self.driver.find_element(*Locators.email_locator).click()
        self.driver.find_element(*Locators.button_locator).click()
        self.wait.until(EC.text_to_be_present_in_element(
            locator=Locators.error_message_pole, text_="Введите адрес, указанный при регистрации"))
        print("empty field")