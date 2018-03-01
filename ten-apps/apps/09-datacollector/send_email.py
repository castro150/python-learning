from email.mime.text import MIMEText
import smtplib


def send(email, height, average_height, count):
    from_email = 'rccastropython@gmail.com'
    from_password = 'r123456a'
    to_email = email

    subject = 'Height data'
    message = 'Hey there, your height is <strong>%s</strong>. <br />Average height of all is <strong>%s</strong>. ' \
              'That is calculated out of <strong>%s</strong> people. <br />Thanks!' % (height, average_height, count)

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
