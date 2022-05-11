from email.message import EmailMessage
import mimetypes
def generate_message(sender, recipient, subject, body, attachment_path, filename):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment_path, 'rb') as f:
        message.add_attachment(f.read(),
                            maintype=mime_type,
                            subtype=mime_subtype,
                            filename=(filename))

    return message

import smtplib
def send_message(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()

if __name__ == '__main__':
    message = generate_message('automation@example.com', 'student-02-f909838ffa9b@example.com', 'Upload Completed - Online Fruit Store', 'All fruits $')
    send_message(message)
