import pandas as pd
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(subject, message, recipient_email):
    """
    This method send email to a recipient
    """
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.getenv('EMAIL')
    msg["To"] = recipient_email
    msg.set_content(message)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(os.getenv('EMAIL'), os.getenv('EMAIL_PASS'))
            smtp.send_message(msg)
            print("Email sent to ", recipient_email)
    except Exception as e:
        print("Failed to send to: ", recipient_email, str(e))

#df = pd.read_csv("recipients.csv")

# for index, row in df.iterrows():
#     name = row["name"]
#     email = row["email"]
#     subject = row["subject"]
#     message = f"""
#     Dear {name},

#     {row['message']}

#     Best regards,
#     Your Name
#     """
#     send_email(subject, message, email)

subject = 'Inquiry about you'
recipient = os.getenv('RECIPIENT')
msg = 'Hello, how are you doing? I am just checking on you.'
send_email(subject, msg, recipient)
