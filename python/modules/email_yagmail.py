import yagmail

receiver = "your@gmail.com"
body = "Hello there from Yagmail"
filename = "document.pdf"


def send_email(sender, sender_password, recipient, subject, body, attachment):
    try:
        # Initialize the Yagmail SMTP client
        yag = yagmail.SMTP(user=sender, password=sender_password)
        
        # Send email
        yag.send(
            to=recipient,
            subject=subject,
            contents=body, 
            attachments=attachment,
        )
        print('Email sent succesfully')

    except Exception as e:
        print(f'Failed to send email: {e}')


def get_input(prompt, converter=str):
    return converter(input(prompt))


def main():
    sender = get_input('Enter your email address: ')
    password = 'nicf zozv rrpu hzzj'
    # password = get_input('Enter your gmail app password: ')
    recipient = get_input('Enter recipient email address: ')
    subject = get_input('Enter subject: ')
    message = get_input('Enter your message: ')
    attachment = 'data_file.json'

    send_email(sender, password, recipient, subject, message, attachment)


if __name__ == '__main__':
    main()


