#!/usr/bin/python3
import smtplib
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def is_valid_email(email):
    """Return True if the email address is valid, False otherwise."""
    if not email:
        return False
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

from_addr = input("Enter sender email address: ").strip()
to_addr = input("Enter receiver email address: ").strip()

if not is_valid_email(from_addr):
    print("Invalid sender email address.")
    exit()

if not is_valid_email(to_addr):
    print("Invalid receiver email address.")
    exit()

subject = input("Enter email subject: ")
body = input("Enter email message: ")
filename = "attachment.txt"

try:
    if not from_addr or not to_addr or not subject or not body:
        raise Exception("Error: Missing information")

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(body))

    with open(filename, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='txt')
        attachment.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(attachment)

    smtp_server = 'smtp.ionos.de'
    smtp_port = 587
    smtp_username = ''
    smtp_password = ''

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(smtp_username, smtp_password)
        smtp.sendmail(from_addr, to_addr, msg.as_string())
        print(f'Email sent successfully to: {to_addr}')
except Exception as e:
    print(f"An error occurred: {e}")