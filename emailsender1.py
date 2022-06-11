import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email ['from'] = 'Mail sender name here'
email ['to'] = 'first@gmail.com', 'second@gmail.com', 'third@gmail.com', 'fourth@gmail.com', 'fifth@gmail.com'
email ['subject'] = 'Mail title here'

#email.set_content('Hello there, this is my second Python email sender project, Happy to learn')
email.set_content(html.substitute({'name': 'enter name', 'amount': 'enter amount', 'Age': enter age here (number) without quote}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender@gmail.com', 'sendergmailpassword')
    smtp.send_message(email)
    print('Message sent, Any other task?')