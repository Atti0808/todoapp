from . import db

class Todo(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    task = db.Column(db.String(300),unique = True)
    complete = db.Column (db.Boolean , default = False)
    urgency = db.Column(db.Integer  )
    
class Comment(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    comment = db.Column(db.String(300),unique = True)
    complete = db.Column (db.Boolean , default = False)
