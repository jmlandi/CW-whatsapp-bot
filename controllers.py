from database import db
from models import Executions, Threads
from assistants import Bruno
from whatsapp import Prd
from flask import render_template, request, jsonify

class Controller():
    
    def index():
        return 'API Online'
          
    def ai_response():
        content = request.json
        
        flow_id = content.flow
        message = content.Body
        topic = content.knowledge
        start = content.start
        
        if start == 'true':

            thread = Bruno.thread_init()
            Bruno.thread_message(thread, message)
            
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