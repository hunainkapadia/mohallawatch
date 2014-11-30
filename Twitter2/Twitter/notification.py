__author__ = 'hkapadia'
#twilio message sending setup

from twilio.rest import TwilioRestClient

# To find these visit https://www.twilio.com/user/account
account = "AC9c2c135bac6928d1cbfff1aebc97312a"
token = "ce64d25db86862fc027e0c7649316d93"

client = TwilioRestClient(account, token)


def sendmessage(receiver,body):
    message = client.sms.messages.create(to=receiver,
                                     from_="+15085027592",
                                     body=body)
    return message