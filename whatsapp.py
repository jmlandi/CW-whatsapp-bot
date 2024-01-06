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
    
    def send_template():
        client.messages.create(
                content_sid='HX3b06ffbe042cc634617ae08ff3675c89',
                from_='MGd94a9cfa8b692f43cc247944988eb291',
                to='whatsapp:+5516992772621'
            )
        
    def create_flow():    
        client.studio.v2.flows.create(
            webhook_url='https://webhooks.twilio.com/v1/Accounts/AC15fac1d0add7090595bdda2dd3af4b03/Flows/FW82751984a3114708b0ccfcf7b7d5a9ce',
            commit_message='First draft',
            friendly_name='Main IVR',
            status='draft',
            definition={
                'description': 'A New Flow',
                'states': [
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
                ],
                'initial_state': 'Trigger',
                'flags': {
                    'allow_concurrent_calls': True
                }
                }
        )


