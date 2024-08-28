class URLpage:
    REGISTER = 'https://stellarburgers.nomoreparties.site/register'
    LOGIN = 'https://stellarburgers.nomoreparties.site/login'
    START = 'https://stellarburgers.nomoreparties.site/'
    FORGOT = 'https://stellarburgers.nomoreparties.site/forgot-password'
    PERSON = 'https://stellarburgers.nomoreparties.site/account/profile'

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
    email = '/html/body/div/div/main/div/form/fieldset[1]/div/div/input'
    password = '/html/body/div/div/main/div/form/fieldset[2]/div/div/input'

class StartXpath:
    button_login = '/html/body/div/div/main/section[2]/div/button[text()="Войти в аккаунт"]'
    button_personal_account = '/html/body/div/div/header/nav/a/p[text()="Личный Кабинет"]'
    button_order = '//button[text()="Оформить заказ"]'
    button_bulki = '/html/body/div/div/main/section[1]/div[1]/div[1]'
    button_bulki_activated = '/html/body/div/div/main/section[1]/div[1]/div[1][contains(@class,"current")]'
    button_sousi = '/html/body/div/div/main/section[1]/div[1]/div[2]'
    button_sousi_activated = '/html/body/div/div/main/section[1]/div[1]/div[2][contains(@class,"current")]'
    button_nachinki = '/html/body/div/div/main/section[1]/div[1]/div[3]'
    button_nachinki_activated = '/html/body/div/div/main/section[1]/div[1]/div[3][contains(@class,"current")]'

class ForgotXpath:
    link_to_login = '/html/body/div/div/main/div/div/p/a[text()="Войти"]'

class PersonXpath:
    login = '/html/body/div/div/main/div/div/div/ul/li[2]/div/div/input'
    link_to_constructor = '/html/body/div/div/header/nav/ul/li[1]/a/p[text()="Конструктор"]'
    logo_stellar = '/html/body/div/div/header/nav/div/a'
    button_exit = '/html/body/div/div/main/div/nav/ul/li[3]/button'

