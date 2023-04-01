import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# email details
from_addr = 'sender@example.com'
to_addr = 'recipient@example.com'
subject = 'Email with Attachment'

# create a message container
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject

# add body text
body = 'This email contains an attachment.'
msg.attach(MIMEText(body))

# add attachment
filename = 'attachment.txt'
with open(filename, 'rb') as f:
    attachment = MIMEApplication(f.read(), _subtype='txt')
    attachment.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(attachment)

# connect to SMTP server and send email
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'username'
smtp_password = 'password'

with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    smtp.sendmail(from_addr, to_addr, msg.as_string())
