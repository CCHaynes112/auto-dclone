from twilio.rest import Client

SMS_BODY = "Dclone is spawning! Go get him!"

class Notifier:
    def __init__(self, twilio_account_sid, twilio_auth_token, sms_from_number, sms_to_number):
        self.client = Client(twilio_account_sid, twilio_auth_token)
        self.sms_from_number = sms_from_number
        self.sms_to_number = sms_to_number

    def send_sms(self):
        print("Sending sms notification...")
        self.client.messages.create(
            from_=self.sms_from_number,
            body=SMS_BODY,
            to=self.sms_to_number,
        )
        print("SMS sent!")
