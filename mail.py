
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

FROM_ADDRESS = 'mtpd7700@gmail.com'
MY_PASSWORD = '5WjBl4vc'
TO_ADDRESS = 'mtpd7700@gmail.com'
# BCC = 'receiver2@test.net'
SUBJECT = 'Calculation is ended!!'
BODY = 'PMFs is outputed!'


def create_message(from_addr, to_addr, subject, body):
# def create_message(from_addr, to_addr, bcc_addrs, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    # msg['Bcc'] = bcc_addrs
    msg['Date'] = formatdate()
    return msg


def send(from_addr, to_addrs, msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS, MY_PASSWORD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()


if __name__ == '__main__':

    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY

    msg = create_message(FROM_ADDRESS, to_addr, subject, body)
    #msg = create_message(FROM_ADDRESS, to_addr, BCC, subject, body)
    send(FROM_ADDRESS, to_addr, msg)
