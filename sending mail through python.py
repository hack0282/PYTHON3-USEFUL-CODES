#email module
import smtplib
from email.message import EmailMessage
email=EmailMessage()
email ['from']='Rohith'
email ['to']='xyz@gmail.com'
email['subject']='you won 1000 dollars'
email.set_content('hi iam python master')
with smtplib.SMTP(host='smtp.gmail.com',port='587')as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('emailid@gmail.com',"emailpassword")
    smtp.send_message(email)
    print('EMAIL SENT')