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
        
        name = request.form.get('Name')
        contact = request.form.get('From')
        message_sid = request.form.get('MessageSid')
        body = request.form.get('Body')

        if Prd.check_flow_execution(contact) == False:
            parameters = {
                'name': name,
                'from': contact,
                'message_sid': message_sid,
                'body': body
                }
            Prd.create_flow(parameters, contact)
            return 200
        
    def ai_response():
        content = request.json
        ai_answer = Bruno.response(content['body'])
        response = {'response': ai_answer}
        return jsonify(response), 200