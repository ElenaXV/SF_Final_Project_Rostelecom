from selenium.webdriver.common.by import By


class Locators:
   username_locator = (By.ID, 'username')
   email_locator = (By.XPATH, '//*[@id="t-btn-tab-mail"]')
   login_locator = (By.XPATH, '//*[@id="t-btn-tab-login"]')
   personal_account = (By.XPATH, '//*[@id="t-btn-tab-ls"]')
   password_locator = (By.ID, 'password')
   button_locator = (By.ID, 'kc-login')
   user_name = (By.XPATH, '//span[contains(@class, "user-name__last-name")]')
   error_message = (By.ID, 'form-error-message')
   password_recovery = (By.ID, 'forgot_password')
   registration = (By.ID, 'kc-register')
   title = (By.CLASS_NAME, 'card-container__title')
   vk = (By.ID, 'oidc_vk')
   ok = (By.ID, 'oidc_ok')
   my_mail = (By.ID, 'oidc_mail')
   ya = (By.ID, 'oidc_ya')
   privacy_policy = (By.ID, 'rt-footer-agreement-link')
   placeholder = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
   error_message_pole = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]')