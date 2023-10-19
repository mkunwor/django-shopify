import random
from django.utils.crypto import get_random_string
import secrets
import string
from .constants import OTP_LENGTH


def generate_otp(length):
    chars = string.digits + 'Avhgdvcgywedhajgsadtwj78TFVCD'
    otp = ''.join(secrets.choice(chars) for _ in range(length))
    return otp


def send_account_activation_mail(request, user):
    from accounts.models import OtpVerificationModel
    otp = generate_otp(OTP_LENGTH)
    subject = "Account Activation OTP"
    message = f"""
    Hello, {user.get_full_name()}. Your OTP for account activation is: {otp}
    """
    from_email = "noreply@myproject.com"
    user.email_user(subject=subject, message=message, from_email=from_email)
    OtpVerificationModel.objects.create(user=user, otp=otp)
    print(otp)
