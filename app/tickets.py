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
    return e.messages,401

  current_app.db.session.add(ticket)
  current_app.db.session.commit()
  return ts.jsonify(ticket), 201