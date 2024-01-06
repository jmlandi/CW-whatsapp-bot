from database import db

class Executions(db.Model):
    message_sid = db.Column(db.String(50), primary_key = True)
    execution_sid = db.Column(db.String(50))
    name = db.Column(db.String(30))
    contact = db.Column(db.String(30))
    status = db.Column(db.String(10))

