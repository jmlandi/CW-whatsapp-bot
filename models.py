from database import db

class Threads(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    flow_id = db.Column(db.String(255))
    thread_id = db.Column(db.String(255))
    topic = db.Column(db.String(25))


