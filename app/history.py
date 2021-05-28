from flask import Blueprint, current_app, request, jsonify
from marshmallow import ValidationError

from app.model import History
from app.serializer import HistorySchema

bp_history = Blueprint('history', __name__)

@bp_history.route('/history/mostrar', methods=['GET'])
def mostrar():
  ts = HistorySchema(many=True)
  result = History.query.all()
  return ts.jsonify(result), 200

@bp_history.route('/history/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
  History.query.filter(History.id == identificador).delete()
  current_app.db.session.commit()
  return jsonify(f"History de id={identificador} deletado!!")


@bp_history.route('/history/modificar/<identificador>', methods=['POST'])
def modificar(identificador):
  ts = HistorySchema()
  query = History.query.filter(History.id == identificador)
  query.update(request.json)
  current_app.db.session.commit()
  return ts.jsonify(query.first()), 201

@bp_history.route('/history/adicionar', methods=['POST'])
def adicionar():
  hs = HistorySchema()

  try:
    history = hs.load(request.json)
  except ValidationError as e:
    print(e.messages)
    return e.messages,401

  current_app.db.session.add(history)
  current_app.db.session.commit()
  print("History =>",history.id,history.ticket_id,history.clerk_id)
  return hs.jsonify(history), 201