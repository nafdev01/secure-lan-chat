from validation_backend_backend import *

# from auth_backend import *


class SignUp:
    def __init__(self, username, password, confirm_password, two_factor_code):
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.two_factor_code = two_factor_code
        self.form_data = None
        self.VALIDATORS = [
            UserNameValidator,
            PasswordValidator,
            ConfirmPasswordValidator,
            TwoFactorValidator
        ]
        self.errors = dict()
        self.is_valid = False

    def process_form(self):
        self.form_data = self.get_form_data()

    def get_form_data(self):
        data = {
            "username": self.username,
            "password": self.password,
            "confirm_password": self.confirm_password,
            "two_factor_code": self.two_factor_code,
        }
        return data

    def validate_form(self):
        self.errors.clear()
        for validator_class in self.VALIDATORS:
            validator = validator_class(self.form_data)
            if not validator.is_valid():
                self.errors.update(validator.errors)

        if self.errors:
            # Handle validation errors
            self.is_valid = False
        else:
            # Process form data
            self.is_valid = True
