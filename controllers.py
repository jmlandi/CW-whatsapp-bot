from database import db
from models import Executions, Threads
from assistants import Bruno
from whatsapp import Prd
from flask import render_template, request, jsonify
import time

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
            new_thread = Threads(flow_id = flow_id, thread_id = thread.id, topic = topic)
            db.session.add(new_thread)
            db.session.commit()


            Bruno.thread_message(thread, message)
            run = Bruno.thread_run(thread, "O assunto da conversa é o produto {topic} da InfinitePay.")
            retrieve = Bruno.thread_retrieve_run(thread, run)
            while True:
                retrieve = Bruno.thread_retrieve_run(thread, run)
                if retrieve.status != "in_progress":
                    assistant_response = Bruno.thread_assitant_reponse(thread)
                    response = {'response': assistant_response}
                    return jsonify(response), 200
                time.sleep(0.5)
              
        else:
            conversation = Threads.query.filter_by(flow_id=flow_id).first()
            thread = {"id":conversation.thread_id}

            Bruno.thread_message(thread, message)
            run = Bruno.thread_run(thread)
            retrieve = Bruno.thread_retrieve_run(thread, run)
            while True:
                retrieve = Bruno.thread_retrieve_run(thread, run)
                if retrieve.status != "in_progress":
                    assistant_response = Bruno.thread_assitant_reponse(thread)
                    response = {'response': assistant_response}
                    return jsonify(response), 200
                time.sleep(0.5)
            
        