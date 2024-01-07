from database import db
from flask import Flask
from controllers import Controller

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)

@app.route('/')
def index():
    return Controller.index()

@app.route('/executions')
def executions():
    return Controller.executions()

@app.route('/ai-response', methods=['POST'])
def ai_response():
    return Controller.ai_response()


@app.route('/incoming-message', methods=['POST'])
def incoming_message():
    return Controller.incoming_message()


if __name__ == '__main__':
    app.run()
