from database import db
from models import Executions, Threads
from assistants import Bruno
from whatsapp import Prd
from flask import render_template, request, jsonify

class Controller():
    
    def index():
        return 'API Online'
          
    def ai_response(content):
        
        flow_id = content['flow']
        message = content['body']
        topic = content['knowledge']
        start = content['start']
        
        if start == 'true':

            thread = Bruno.thread_init()
            Bruno.thread_message(thread, message)
            Bruno.thread_run(thread, "O produto InfinitePay em questão é: {topic}")
            assistant_response = Bruno.thread_assitant_reponse(thread)

            new_thread = Threads(
                flow_id = flow_id,
                thread_id = thread.id,
                topic = topic
            )
            db.session.add(new_thread)
            db.session.commit()
        
        else:
            conversation = Threads.filter_by(flow_id=flow_id).first()
            Bruno.thread_message(conversation.thread_id, message)
            Bruno.thread_run(conversation.thread_id)
            assistant_response = Bruno.thread_assitant_reponse(conversation.thread_id)
            


        response = {'response': assistant_response}
        return jsonify(response), 200