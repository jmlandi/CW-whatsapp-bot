from database import db
from models import Threads
from assistants import Bruno
from flask import jsonify

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
            thread_id = thread.id
            new_thread = Threads(flow_id = flow_id, thread_id = thread_id, topic = topic)
            db.session.add(new_thread)
            db.session.commit()


            Bruno.thread_message(thread_id, message)
            run = Bruno.thread_run(thread_id, f"O cliente com interesse no {topic}")
            retrieve = Bruno.thread_retrieve_run(thread_id, run)
            while True:
                retrieve = Bruno.thread_retrieve_run(thread_id, run)
                if retrieve.status != "in_progress":
                    assistant_response = Bruno.thread_assitant_reponse(thread_id)
                    if (assistant_response == message):
                        return 500
                    response = {'response': assistant_response}
                    return jsonify(response), 200
              
        else:
            conversation = Threads.query.filter_by(flow_id=flow_id).first()

            Bruno.thread_message(conversation.thread_id, message)
            run = Bruno.thread_run(conversation.thread_id, f"O cliente com interesse no {conversation.topic}")
            retrieve = Bruno.thread_retrieve_run(conversation.thread_id, run)
            while True:
                retrieve = Bruno.thread_retrieve_run(conversation.thread_id, run)
                if retrieve.status != "in_progress":
                    assistant_response = Bruno.thread_assitant_reponse(conversation.thread_id)
                    if (assistant_response == message):
                        return 500
                    response = {'response': assistant_response}
                    return jsonify(response), 200
                
    def ai_completion(prompt):
        completion = Bruno.bruno_completion(prompt)
        response = {'response': completion}
        return jsonify(response), 200
            
        