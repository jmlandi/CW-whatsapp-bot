from twilio.rest import Client
from models import Executions, db
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
flow_id = 'FW82751984a3114708b0ccfcf7b7d5a9ce'
msg_id = 'whatsapp:+17372010046'

client = Client(account_sid, auth_token)

class Sandbox():

    def response(chat_sid, message):
        client.conversations \
                        .v1 \
                        .conversations(chat_sid) \
                        .messages \
                        .create(author='system', body = message)

class Prd():
    
    def send_template(contact):
        client.messages.create(
                content_sid='HX3b06ffbe042cc634617ae08ff3675c89',
                from_=msg_id,
                to=contact
            )
      

            
