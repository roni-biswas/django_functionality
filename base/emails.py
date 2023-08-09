from django.conf import settings
from django.core.mail import send_mail


def send_emali_token(email, email_token):
    try:
        subject = 'Your accounts need to be verified.'
        message = f'Click on the link to verify http://localhost:8000/verify/{email_token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail( subject, message, email_from, recipient_list )

    except Exception as e:
        return False

    return True