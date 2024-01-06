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
    
    def template_sender():
        client.messages.create(
                content_sid='HX3b06ffbe042cc634617ae08ff3675c89',
                from_='MGd94a9cfa8b692f43cc247944988eb291',
                to='whatsapp:+5516992772621'
            )


