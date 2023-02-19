class BaseError(Exception):
    message = NotImplemented

class UserError(BaseError):
    message = NotImplemented

class PasswordWrong(UserError):
    message = 'Неверный пароль'

