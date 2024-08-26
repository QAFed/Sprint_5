class URLpage:
    REGISTER = 'https://stellarburgers.nomoreparties.site/register'
    LOGIN = 'https://stellarburgers.nomoreparties.site/login'
    START = 'https://stellarburgers.nomoreparties.site/'
    FORGOT = 'https://stellarburgers.nomoreparties.site/forgot-password'

class RegisterXpath:
    name = '/html/body/div/div/main/div/form/fieldset[1]/div/div/input'
    email = '/html/body/div/div/main/div/form/fieldset[2]/div/div/input'
    password = '/html/body/div/div/main/div/form/fieldset[3]/div/div/input'
    button_register = '/html/body/div/div/main/div/form/button[text()="Зарегистрироваться"]'
    link_to_login = '/html/body/div/div/main/div/div/p/a[text()="Войти"]'

class RegisterCSS:
    pass_field_alert = '#root > div > main > div > form > fieldset:nth-child(3) > div > p'


class LoginXpath:
    button_login = '//button[text()="Войти"]'

class StartXpath:
    button_login = '/html/body/div/div/main/section[2]/div/button[text()="Войти в аккаунт"]'
    button_personal_account = '/html/body/div/div/header/nav/a/p[text()="Личный Кабинет"]'


class ForgotXpath:
    link_to_login = '/html/body/div/div/main/div/div/p/a[text()="Войти"]'