import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from_addr = input("Enter sender email address: ").strip()
to_addr = input("Enter receiver email address: ").strip()
subject = input("Enter email subject: ")
body = input("Enter email message: ")
filename = "attachment.txt"

if from_addr.isempty() or to_addr.isempty() or subject.isempty() or body.isempty():
    print("Error: Missing information")
    exit()

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject

msg.attach(MIMEText(body))

with open(filename, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='txt')
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(attachment)

#smtp_server = 'smtp.freesmtpservers.com'
#smtp_port = 25

smtp_server = 'smtp.ionos.de'
smtp_port = 587
smtp_username = ''
smtp_password = ''

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(from_addr, to_addr, msg.as_string())
    print(f'Email sent successfully to: {to_addr}')