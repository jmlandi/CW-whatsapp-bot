from database import db
from flask import Flask, request
from controllers import Controller
from assistants import gpt_init

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
gpt_init()

@app.route('/')
def index():
    return Controller.index()

@app.route('/ai-response', methods=['POST'])
def ai_response():
    content = request.get_json()
    return Controller.ai_response(content)

@app.route('/ai-completion', methods=['POST'])
def ai_completion():
    content = request.get_json()
    return Controller.ai_completion(content.body)
    return Controller.incoming_message()

with app.app_context():
  db.create_all()

if __name__ == '__main__':
    app.run()
