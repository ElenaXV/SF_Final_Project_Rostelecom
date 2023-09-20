
from time import sleep

from pages.main_page import *

#EXP-001 - Проверка загрузки страницы
def test_main(driver):
    main_page = MainPage(driver)
    main_page.load()
    assert main_page.is_loaded()

#EXP-002 - Проверка расположения блоков на странице Авторизации (сохранить скриншот)
def test_vision(driver):
    main_page = MainPage(driver)
    main_page.load()
    main_page.is_loaded()
    main_page.driver.save_screenshot('form.png')

#EXP-003 - Успешная проверка автосмены "плесхолдера" при переключении таба "Телефон", "Почта", "Логин", "Лицевой счет"
def test_tab_and_placeholder(driver):
    AuthForm(driver).tab_and_placeholder()

#EXP-004 - успешная авторизация клиента по номеру телефона с неверными данными
def test_auth(driver):
    AuthForm(driver).authorization_by_phone()

#EXP-005 - Не успешная авторизация клиента по номеру телефона с неверными данными
def test_auth_failed(driver):
    AuthForm(driver).failed_authorization_by_phone()

#EXP-006 - Успешная авторизация клиента c корректным email и паролем
def test_auth_email(driver):
    AuthForm(driver).authorization_by_email()

#EXP-007 - Не успешная авторизация клиента с помощью не корректной электронной почты и пароля
def test_auth_failed_email(driver):
    AuthForm(driver).failed_authorization_by_email()

#EXP-008 - Успешная авторизация клиента по логину
def test_auth_login(driver):
    AuthForm(driver).authorization_by_login()

#EXP-009 - Не успешная авторизация клиента с помощью неверного логина и пароля
def test_auth_failed_login(driver):
    AuthForm(driver).failed_authorization_by_login()

#EXP-018 - Проверить основные элементы на странице "Восстановление пароля"
def test_vision_form_password_recovery(driver):
    AuthForm(driver).form_password_recovery()

#EXP-022 Проверка основных элементов на странице форма регистрации
def test_vision_form_registration(driver):
    AuthForm(driver).form_registration()

#EXP-023 Авторизация через соцсеть Вконтакте
def test_auth_by_vk(driver):
    AuthForm(driver).auth_by_vk()
    assert driver.current_url.startswith('https://id.vk.com/')

#EXP-024 Авторизация через соцсеть Одноклассники
def test_auth_by_ok(driver):
    AuthForm(driver).auth_by_ok()
    assert driver.current_url.startswith('https://connect.ok.ru/')

#EXP-025 Авторизация через соцсеть Мой мир
def test_auth_by_my_mail(driver):
    AuthForm(driver).auth_by_my_mail()
    assert driver.current_url.startswith('https://connect.mail.ru/')

#EXP-027 Корректная работа ссылки с "Политикой конфиденциальности"
def test_privacy_policy(driver):
    AuthForm(driver).privacy_policy()
    assert driver.current_url('https://b2c.passport.rt.ru/sso-static/agreement/agreement.html')

#EXP-028 проверка авторизации с пустыми полями.
def test_authorization_with_empty(driver):
    AuthForm(driver).failed_authorization_with_empty()


