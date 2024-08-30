class RegisterXpath:
    name = '//label[text()="Имя"]/parent::div/input'
    email = '//label[text()="Email"]/parent::div/input'
    password = '//label[text()="Пароль"]/parent::div/input'
    button_register = '//button[text()="Зарегистрироваться"]'
    link_to_login = '//a[@href="/login"]'
    pass_field_alert = '//p[contains(@class, "error text")]'


class LoginXpath:
    button_login = '//button[text()="Войти"]'
    email = '//label[text()="Email"]/parent::div/input'
    password = '//label[text()="Пароль"]/parent::div/input'


class StartXpath:
    button_login = '//button[text()="Войти в аккаунт"]'
    button_personal_account = '//p[text()="Личный Кабинет"]'
    button_order = '//button[text()="Оформить заказ"]'
    # button_bulki = '//span[text()="Булки"]'
    button_bulki_activated = '//span[text()="Булки"]/parent::div'
    # button_sousi = '//span[text()="Соусы"]'
    button_sousi_activated = '//span[text()="Соусы"]/parent::div'
    # button_nachinki = '//span[text()="Начинки"]'
    button_nachinki_activated = '//span[text()="Начинки"]/parent::div'


class ForgotXpath:
    link_to_login = '//a[text()="Войти"]'


class PersonXpath:
    login = '//label[text()="Логин"]'
    link_to_constructor = '//p[text()="Конструктор"]'
    logo_stellar = '//div[contains(@class, "logo")]'
    button_exit = '//button[text()="Выход"]'