from database import db

class Executions(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    message_sid = db.Column(db.String(50))
    execution_sid = db.Column(db.String(50))
    name = db.Column(db.String(30))
    contact = db.Column(db.String(30))
    status = db.Column(db.String(10))


class Threads(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    flow_id = db.Column(db.String(50))
    thread_id = db.Column(db.String(50))
    topic = db.Column(db.String(20))
    messages = db.Column(db.String(999))


