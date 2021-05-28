from datetime import datetime
from flask import Blueprint, current_app, request, jsonify
from app.model import Ticket
from app.serializer import TicketSchema
from marshmallow import ValidationError


bp_tickets = Blueprint('tickets', __name__)

@bp_tickets.route('/ticket/mostrar', methods=['GET'])
def mostrar():
  ts = TicketSchema(many=True)
  result = Ticket.query.all()
  return ts.jsonify(result), 200

@bp_tickets.route('/ticket/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
  Ticket.query.filter(Ticket.id == identificador).delete()
  current_app.db.session.commit()
  return jsonify(f"Ticket de id={identificador} deletado!!")


@bp_tickets.route('/ticket/modificar/<identificador>', methods=['POST'])
def modificar(identificador):
  ts = TicketSchema()
  query = Ticket.query.filter(Ticket.id == identificador)
  query.update(request.json)
  current_app.db.session.commit()
  return ts.jsonify(query.first()), 201

@bp_tickets.route('/ticket/adicionar', methods=['POST'])
def adicionar():
  ts = TicketSchema()

  try:
    ticket = ts.load(request.json)
  except ValidationError as e:
    print(e.messages)
    return e.messages,401

  current_app.db.session.add(ticket)
  current_app.db.session.commit()
  #print(ticket.id,ticket.position,ticket.subject,ticket.date_created)
  return ts.jsonify(ticket), 201


@bp_tickets.route('/ticket/start/<identificador>', methods=['GET'])
def add_date_called(identificador):
  ts = TicketSchema()
  ticket = Ticket.query.filter_by(id=identificador).first()
  date_called=  datetime.now()
  ticket.date_called = date_called
  current_app.db.session.commit()
  print(ticket.date_called)
  return ts.jsonify(ticket), 201


@bp_tickets.route('/ticket/end/<identificador>', methods=['GET'])
def add_date_end(identificador):
  ts = TicketSchema()
  ticket = Ticket.query.filter_by(id=identificador).first()
  date_called = datetime.now()
  ticket.date_end = date_called
  current_app.db.session.commit()
  print(ticket.date_end)
  return ts.jsonify(ticket), 201
