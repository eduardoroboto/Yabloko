from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def configure(app):
  db.init_app(app)
  app.db = db

class Ticket(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  position = db.Column(db.Integer,nullable=False)
  subject = db.Column(db.String(200),nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.now())
  date_called = db.Column(db.DateTime, default=None)
  date_end = db.Column(db.DateTime, default=None)
  

class Clerk(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  position = db.Column(db.Integer, nullable=False)
  name = db.Column(db.String(200),nullable=False)
  subjects = db.Column(db.String(200),nullable=False)
  password =db.Column(db.String(200),nullable=True)

class History(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  ticket_id = db.Column(db.Integer, db.ForeignKey('ticket.id'),nullable=False)
  clerk_id = db.Column(db.Integer, db.ForeignKey('clerk.id'),nullable=False)
