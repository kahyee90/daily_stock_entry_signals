import smtplib
from email.mime.text import MIMEText
import os

# Read output
with open("output.txt", "r") as f:
    content = f.read()

msg = MIMEText(content)
msg['Subject'] = 'Daily Python Output'
msg['From'] = os.environ['EMAIL_USER']
msg['To'] = os.environ['EMAIL_USER']

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(os.environ['EMAIL_USER'], os.environ['EMAIL_PASS'])
    server.send_message(msg)
