import pyotp
import qrcode


class TwoFactorAuth:
    def __init__(self):
        self.secret_key = pyotp.random_base32()

    def generate(self):
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        # The provisioning_uri is used to create the QR code
        provisioning_uri = pyotp.totp.TOTP(self.secret_key).provisioning_uri(
            "nickname", issuer_name="Secure LAN Chat"
        )
        # Add the provisioning_uri data to the QR code object
        qr.add_data(provisioning_uri)
        qr.make(fit=True)
        # Create an image of the QR code
        img = qr.make_image(fill_color="black", back_color="white")
        return img

    def authenticate(self, user_code):
        # Create the TOTP object
        totp = pyotp.TOTP(self.secret_key)
        # Verify the user's code
        if totp.verify(user_code):
            return True
        else:
            return False
