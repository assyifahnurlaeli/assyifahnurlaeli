#!/usr/bin/env python3
"""
email_sender.py
Simple email sender (SMTP). Configure via environment variables:
EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASS, EMAIL_TO
Usage: python email_sender.py report.txt
"""
import sys, os
from email.mime.text import MIMEText
import smtplib

def send(report_file):
    host = os.getenv('EMAIL_HOST','smtp.gmail.com')
    port = int(os.getenv('EMAIL_PORT','587'))
    user = os.getenv('EMAIL_USER')
    pwd = os.getenv('EMAIL_PASS')
    to = os.getenv('EMAIL_TO')
    if not all([user,pwd,to]):
        print("Set EMAIL_USER, EMAIL_PASS, and EMAIL_TO environment variables before running.")
        return
    with open(report_file,'r',encoding='utf-8') as f:
        body = f.read()
    msg = MIMEText(body)
    msg['Subject'] = 'Automated Daily Sales Report'
    msg['From'] = user
    msg['To'] = to
    s = smtplib.SMTP(host,port)
    s.starttls()
    s.login(user,pwd)
    s.sendmail(user,[to],msg.as_string())
    s.quit()
    print("Email sent.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python email_sender.py report.txt")
    else:
        send(sys.argv[1])
