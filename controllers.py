from database import db
from models import Executions, Threads
from assistants import Bruno
from whatsapp import Prd
from flask import render_template, request, jsonify
import requests

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
        
        flow_id = content.flow
        body = content.body
        message = content.Body
        topic = content.knowledge
        start = content.start
        
        if start == 'true':

            thread = Bruno.thread_init()
            Bruno.thread_message(thread, body)
            
            run = Bruno.thread_run(thread)
            Bruno.thread_response(thread, run)

            messages = Bruno.thread_messages_list(thread)

            new_thread = Threads(
                flow_id = flow_id,
                thread_id = thread.id,
                topic = topic,
                messages = messages
            )
            db.session.add(new_thread)
            db.session.commit()


        response = {'response': jsonify(Bruno.thread_assitant_reponse(thread))}
        return jsonify(response), 200