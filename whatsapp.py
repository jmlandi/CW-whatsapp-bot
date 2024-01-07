from twilio.rest import Client
from models import Executions, db
import os

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
flow_id = 'FW82751984a3114708b0ccfcf7b7d5a9ce'
msg_id = 'MGd94a9cfa8b692f43cc247944988eb291'

client = Client(account_sid, auth_token)

class Sandbox():

    def response(chat_sid, message):
        client.conversations \
                        .v1 \
                        .conversations(chat_sid) \
                        .messages \
                        .create(author='system', body = message)

class Prd():
    
    '''
    def send_template(contact):
        client.messages.create(
                content_sid='HX3b06ffbe042cc634617ae08ff3675c89',
                from_=msg_id,
                to=contact
            )
    '''
        
    def create_flow(parameters, contact):
        execution = client.studio \
                  .v2 \
                  .flows(flow_id) \
                  .executions \
                  .create(
                      parameters=parameters,
                      to=contact,
                      from_=msg_id)
        
        new_flow_execution = Executions(
            message_sid = parameters['message_sid'],
            execution_sid = execution.sid,
            name = parameters['name'],
            contact = contact,
            status = execution.status
        )

        db.session.add(new_flow_execution)
        db.session.commit()

    def check_flow_execution(contact):
        
        contact_info = Executions.query.filter_by(contact=contact).first()
        if contact_info == None:
            return False
        else:
            execution = client.studio \
                  .v2 \
                  .flows(flow_id) \
                  .executions(contact_info.execution_sid) \
                  .fetch()
            if execution.status != 'active':
                return False
            else:
                return True

            
