from twilio.rest import Client
from flask import jsonify
import requests
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
flow_id = 'FW82751984a3114708b0ccfcf7b7d5a9ce'

client = Client(account_sid, auth_token)

class Sandbox():

    def response(chat_sid, message):
        client.conversations \
                        .v1 \
                        .conversations(chat_sid) \
                        .messages \
                        .create(author='system', body = message)

class Prd():
    
    def send_template():
        client.messages.create(
                content_sid='HX3b06ffbe042cc634617ae08ff3675c89',
                from_='MGd94a9cfa8b692f43cc247944988eb291',
                to='whatsapp:+5516992772621'
            )
        
    def create_flow():
        client.studio \
                  .v2 \
                  .flows(flow_id) \
                  .executions \
                  .create(to='whatsapp:+5516992772621', from_='+MGd94a9cfa8b692f43cc247944988eb291')