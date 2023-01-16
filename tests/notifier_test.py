import pytest
from unittest.mock import Mock
from twilio.rest import Client

from src.auto_dclone.notifier import Notifier, SMS_BODY

def test_send_sms():
    twilio_account_sid = "123"
    twilio_auth_token = "456"
    sms_from_number = "789"
    sms_to_number = "012"

    client = Mock(spec=Client)
    notifier = Notifier(twilio_account_sid, twilio_auth_token, sms_from_number, sms_to_number)
    notifier.client = client

    notifier.send_sms()

    client.messages.create.assert_called_once_with(
        from_=sms_from_number,
        body=SMS_BODY,
        to=sms_to_number,
    )
