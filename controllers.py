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
            run = Bruno.thread_run(thread, "O produto InfinitePay em questão é: {topic}")
            retrieve = Bruno.thread_retrieve_run(thread, run)
            while True:
                retrieve = Bruno.thread_retrieve_run(thread, run)
                if retrieve != "in_progress":
                    assistant_response = Bruno.thread_assitant_reponse(thread)
                    break


            new_thread = Threads(
                flow_id = flow_id,
                thread_id = thread.id,
                topic = topic
            )
            db.session.add(new_thread)
            db.session.commit()
        
        '''
        else:
            conversation = Threads.filter_by(flow_id=flow_id).first()
            Bruno.thread_message(conversation.thread_id, message)
            run = Bruno.thread_run(conversation.thread_id)
            retrieve, cont_retrieve = Bruno.thread_retrieve_run(thread, run), 0
            while retrieve.status != "completed":
                retrieve = Bruno.thread_retrieve_run(thread, run)
                time.sleep(0.5)
                cont_retrieve += 1
                if cont_retrieve > 5:
                    break
            assistant_response = Bruno.thread_assitant_reponse(conversation.thread_id)
        '''
            
        response = {'response': assistant_response}
        return jsonify(response), 200