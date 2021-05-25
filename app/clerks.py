from flask import Blueprint, current_app, request, jsonify
from marshmallow import ValidationError

from app.model import Clerk
from app.serializer import ClerkSchema


bp_clerks = Blueprint('clerks',__name__)

@bp_clerks.route('/clerk/mostrar', methods=['GET'])
def mostrar():
    cs = ClerkSchema(many=True)
    result = Clerk.query.all()
    return cs.jsonify(result), 200

@bp_clerks.route('/clerk/deletar/<identificador>', methods=['GET'])
def deletar(identificador):
    Clerk.query.filter(Clerk.id == identificador).delete()
    current_app.db.session.commit()
    return jsonify(f"Clerk de id={identificador} deletado!!")


@bp_clerks.route('/clerk/modificar/<identificador>', methods=['POST'])
def modificar(identificador):
    cs = ClerkSchema()
    query = Clerk.query.filter(Clerk.id == identificador)
    query.update(request.json)
    current_app.db.session.commit()
    return cs.jsonify(query.first()), 201

@bp_clerks.route('/clerk/adicionar', methods=['POST'])
def adicionar():
    cs = ClerkSchema()

    try:
        clerk = cs.load(request.json)
    except ValidationError as e:
        return e.messages,401

    current_app.db.session.add(clerk)
    current_app.db.session.commit()
    return cs.jsonify(clerk), 201