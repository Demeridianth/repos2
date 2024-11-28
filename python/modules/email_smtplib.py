import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Simple Mail Transfer Protocol (SMTP)


def send_mail(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Set up email details
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        

        # Attach the email body
        msg.attach(MIMEText(message, 'plain'))
        # msg.attach(MIMEText(message, 'HTML'))

        # Connect the SMTP server and send mail
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Starts TLS encryption
            server.login(sender_email, sender_password)  # Log in to SMTP server
            server.send_message(msg)  # send email
            print('email sent succesfully')

    except Exception as e:
        print(f'Failed to send email: {e}')


def get_input(prompt, converter=str):
    return converter(input(prompt))


def main():
    sender = get_input('Enter your email address: ')
    password = get_input('Enter you gmail app password: ')
    recipient = get_input('Enter recipient email address: ')
    subject = get_input('Enter subject: ')
    message = get_input('Enter message: ')

    send_mail(sender, password, recipient, subject, message)


if __name__ == '__main__':
    main()

# pass =  'nicf zozv rrpu hzzj'