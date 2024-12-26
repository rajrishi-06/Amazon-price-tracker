import smtplib
from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv()

class NotificationManager:
    def __init__(self):
        self.TWILLIO_SID = os.getenv("TWILLIO_SID")
        self.TWILLIO_AUTH_TOKEN = os.getenv("TWILLIO_AUTH_TOKEN")
        self.client = Client(self.TWILLIO_SID, self.TWILLIO_AUTH_TOKEN)
        self.FROM_EMAIL = os.getenv("FROM_EMAIL")
        self.EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.getenv("TWILIO_VIRTUAL_NUMBER"),
            body = message_body,
            to=os.getenv("TWILIO_VERIFIED_NUMBER")
        )
        print(message.sid)
        return True
    def send_email(self,message_body, to_email):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="rajrishi0109@gmail.com", password=self.EMAIL_PASSWORD)
            connection.sendmail(from_addr=self.FROM_EMAIL, to_addrs=to_email,
                                msg=f"{message_body}")
        return True