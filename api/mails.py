import smtplib
import logging

from flask import current_app as app
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def send_match_email(user, m_user):

    # set up the SMTP server
    with smtplib.SMTP(app.config['SMTP_HOST'], app.config['SMTP_PORT'],
                      timeout=10) as server:

        server.starttls()
        server.login(app.config['FROM_EMAIL'], app.config['FROM_PASSWORD'])
        msg = MIMEMultipart()
        message_template = read_template('mail_templates/new_match.txt')

        # add in the actual person name to the message template
        message = message_template.substitute(
            USER_NAME=user.firstname.title(),
            FIRSTNAME=m_user.firstname.title(),
            LASTNAME=m_user.lastname.title(),
            EMAIL=m_user.email,
        )

        # setup the parameters of the message
        msg['From'] = app.config['FROM_EMAIL']
        msg['To'] = m_user.email
        msg['Subject'] = "Your RCT match of the month!"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        server.send_message(msg)


def send_unmatched_email(users):

    # set up the SMTP server
    with smtplib.SMTP(app.config['SMTP_HOST'], app.config['SMTP_PORT'],
                      timeout=10) as server:

        server.starttls()
        server.login(app.config['FROM_EMAIL'], app.config['FROM_PASSWORD'])
        msg = MIMEMultipart()
        message_template = read_template('mail_templates/new_match.txt')

        user_emails = '\n'.join([u.email for u in users])
        # add in the actual person name to the message template
        message = message_template.substitute(
            USER_EMAILS=user_emails
        )

        # setup the parameters of the message
        msg['From'] = app.config['FROM_EMAIL']
        msg['To'] = app.config['FROM_EMAIL']
        msg['Subject'] = "RCT's round has some unmatched users!"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        server.send_message(msg)
