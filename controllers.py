from database import db
from models import Executions
from assistants import Bruno
from whatsapp import Prd
from flask import render_template, request, jsonify

class Controller():
    
    def index():
        return 'API Online'
    
    def executions():
        executions = Executions.query.all()
        return render_template('executions.html', executions=executions)
    
    def incoming_message():
        
        name = request.form.get('ProfileName')
        contact = request.form.get('From')
        message_sid = request.form.get('MessageSid')
        body = request.form.get('Body')
        content = request.get_data()

        if Prd.check_flow_execution(contact) == False:
            parameters = {
                'name': name,
                'from': contact,
                'message_sid': message_sid,
                'body': body
                }
            Prd.create_flow(parameters, contact)
            return 200
        else:
            request.post('https://webhooks.twilio.com/v1/Accounts/AC15fac1d0add7090595bdda2dd3af4b03/Flows/FW82751984a3114708b0ccfcf7b7d5a9ce', json=content)
        
    def ai_response():
        content = request.json
        ai_answer = Bruno.response(content['body'])
        response = {'response': ai_answer}
        return jsonify(response), 200