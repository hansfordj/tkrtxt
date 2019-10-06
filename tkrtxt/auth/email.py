from flask import render_template
from tkrtxt import app, mail
from tkrtxt.email import send_email


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[TkrTxt] Reset Your Password', sender=app.config['ADMINS'], recipients=[user.email], text_body=render_template(
        'email/reset_password.txt', user=user, token=token), html_body=render_template('email/reset_password.html', user=user, token=token))
