class URLpage:
    REGISTER = 'https://stellarburgers.nomoreparties.site/register'
    LOGIN = 'https://stellarburgers.nomoreparties.site/login'

class RegisterXpath:
    name = '/html/body/div/div/main/div/form/fieldset[1]/div/div/input'
    email = '/html/body/div/div/main/div/form/fieldset[2]/div/div/input'
    password = '/html/body/div/div/main/div/form/fieldset[3]/div/div/input'
    button_register = '/html/body/div/div/main/div/form/button[text()="Зарегистрироваться"]'

class RegisterCSS:
    pass_field_alert = '#root > div > main > div > form > fieldset:nth-child(3) > div > p'

class LoginXpath:
    button_login = '//button[text()="Войти"]'