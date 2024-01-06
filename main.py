from database import db
from models import Executions
from assistants import Bruno
from whatsapp import Sandbox, Prd
from flask import Flask, render_template, request, jsonify

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def index():
    return 'API Online'

@app.route('/executions')
def executions():
    executions = Executions.query.all()
    return render_template('executions.html', executions=executions)

@app.route('/direct-messages', methods=['POST'])
def sandbox_messages():
    Sandbox.response(request.form.get('MessageSid'), Bruno.response(request.form.get('Body')))
    return 200

@app.route('/chatbot-workflow', methods=['POST'])
def prd_messages():
    content = request.json
    ai_answer = Bruno.response(content['body'])
    response = {'response': ai_answer}
    return jsonify(response), 200

@app.route('/incoming-message', methods=['POST'])
def incoming_message():
    parameters = {
        'name':request.form.get('ProfileName'),
        'from':request.form.get('From'),
        'message_sid':request.form.get('MessageSid')
        }
    contact = request.form.get('From')
    Prd.create_flow(parameters, contact)
    return 200

if __name__ == '__main__':
    app.run()
