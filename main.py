from assistants import Bruno
from whatsapp import Sandbox, Prd
from flask import Flask, request

app = Flask('app')

@app.route('/')
def index():
    return 'API Online'

# SANDBOX ENV // application/x-www-form-urlencoded
@app.route('/sandbox-messages', methods=['POST'])
def sandbox_messages():
    Sandbox.response(request.form.get('MessageSid'), Bruno.response(request.form.get('Body')))
    return 200

# PRD ENV // application/json
@app.route('/16693335835-messages', methods=['POST'])
def prd_messages():
    content = request.json
    Prd.response(content['message_sid'], Bruno.response(content['body']))
    return 200

if __name__ == '__main__':
    app.run()
