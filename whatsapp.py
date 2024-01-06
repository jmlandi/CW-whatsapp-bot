from twilio.rest import Client
from flask import jsonify
import requests
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
flow_url = 'https://studio.twilio.com/v2/Flows/FW82751984a3114708b0ccfcf7b7d5a9ce/Executions'

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
        friendly_name = 'teste'
        status = 'draft'
        definition = jsonify([
                        {
                            'name': 'Trigger',
                            'type': 'trigger',
                            'transitions': [
                            ],
                            'properties': {
                                'offset': {
                                    'x': 0,
                                    'y': 0
                                }
                            }
                        }
                    ])

        client.studio.v2.flows.create(
                friendly_name = friendly_name,
                status = status,
                definition = definition
            )



        '''
        flow = {
            'friendly_name':friendly_name,
            'status':status,
            'definition': definition
            }    
        res = requests.post(flow_url, json=flow)
        return f'Server response: {res.text}'
        '''

