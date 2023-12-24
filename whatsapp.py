from twilio.rest import Client
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

class Sandbox():

    def response(chat_sid, message):
        client.conversations \
                        .v1 \
                        .conversations(chat_sid) \
                        .messages \
                        .create(author='system', body = message)

class Prd():

    def response(chat_sid, message):
        client.conversations \
                        .v1 \
                        .conversations(chat_sid) \
                        .messages \
                        .create(author='system', body = message)

Prd.response('SM2a420ae56963140b5ac4fe0606657379', 'teste')