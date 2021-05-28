from flask import Blueprint, current_app, request, jsonify,render_template

fe_tickets = Blueprint('ticketsMachine', __name__)


@fe_tickets.route("/tickets/machine")
def ticket_machine():
    with open("app/data/assuntos.csv","r") as file:
        assuntos = file.read().split("\n")
    return render_template('ticket_machine.html',assuntos=assuntos)