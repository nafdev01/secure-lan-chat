import re


class FormValidator:
    def __init__(self, data):
        self.data = data
        self.errors = {}

    def validate(self):
        pass

    def is_valid(self):
        self.validate()
        return not bool(self.errors)


class UserNameValidator(FormValidator):
    def validate(self):
        username = self.data["username"]
        if not username:
            self.errors["username"] = "Username is required"
        elif len(username) < 6:
            self.errors["username"] = "Username must be at least 6 characters"


class SecretKeyValidator(FormValidator):
    def validate(self):
        secret_key = self.data.get("secret_key")
        if not secret_key:
            self.errors["secret_key"] = "Generate a QRCode Before You Scan"


class PasswordValidator(FormValidator):
    def validate(self):
        password = self.data.get("password")
        if not password:
            self.errors["password"] = "Password is required"
        elif len(password) < 8:
            self.errors["password"] = "Password must be at least 8 characters"
        elif not re.search(r"[A-Z]", password):
            self.errors[
                "password"
            ] = "Password must contain at least one uppercase letter"
        elif not re.search(r"[a-z]", password):
            self.errors[
                "password"
            ] = "Password must contain at least one lowercase letter"
        elif not re.search(r"\d", password):
            self.errors["password"] = "Password must contain at least one integer"
        elif not re.search(r"[!@#$%^&*_]", password):
            self.errors[
                "password"
            ] = "Password must contain at least one special character"


class ConfirmPasswordValidator(FormValidator):
    def validate(self):
        password = self.data.get("password")
        confirm_password = self.data.get("confirm_password")
        if not confirm_password:
            self.errors["confirm_password"] = "Confirm password is required"
        elif password != confirm_password:
            self.errors["confirm_password"] = "Passwords do not match"


class TwoFactorValidator(FormValidator):
    def validate(self):
        two_factor_code = self.data.get("two_factor_code")
        if not two_factor_code:
            self.errors["two_factor_code"] = "Enter Two Factor Code"
