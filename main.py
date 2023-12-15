from assistants import Marta
from whatsapp import Whatsapp
from twilio.twiml.messaging_response import Message, MessagingResponse
from flask import Flask, request, jsonify

app = Flask('app')

@app.route('/')
def index():
    return 'API Online'




@app.route('/messages', methods=['POST'])
def messages():
    # request_data = request.get_data()
    Whatsapp.response('CHad85b100f3024b1cad2fb2e841f9529d', Marta.response(request.form.get('Body')))
    return response, 200

if __name__ == '__main__':
    app.run()


# last_message = 'Qual a melhor taxa que InfinitePay oferece?'
# Whatsapp.response('CHad85b100f3024b1cad2fb2e841f9529d', Marta.response(last_message))
