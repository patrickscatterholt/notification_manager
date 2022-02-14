from twilio.rest import Client


TWILIO_SID = "AC592fdffd6f2a6a7d87a36b10103eff2a"
TWILIO_AUTH_TOKEN = "a3c80c98e0a7675fffb61d2ff431ce58"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
