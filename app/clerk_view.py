from flask import Blueprint, request, redirect, url_for, render_template, session
from sqlalchemy.exc import NoResultFound

from app.model import Clerk, Ticket, History

fe_clerk = Blueprint('ClerkSystem', __name__)


## Login page
@fe_clerk.route("/login",methods=['POST','GET'])
def login(error=''):
    if request.method == "POST":
        name = request.form['name']
        password = request.form['password']

        clerk = Clerk.query.filter(Clerk.name==name, Clerk.password == password).first()
        #print(clerk)
        if clerk:
            session['name'] = clerk.name
            session['subjects'] = clerk.subjects
            session['position'] = clerk.position
            session['id'] = clerk.id

            #print(session)
            return redirect(url_for('ClerkSystem.main'))
        else:
            error="Error no Login"
            return render_template('login.html',error=error)

        #return render_template('login.html',error=Zclerk)

    elif request.method == "GET":
        return render_template('login.html',error=error)

## Clerk Page
@fe_clerk.route("/main",methods=['GET'])
def main():
    if "name" in session:
        return render_template('clerk_page.html',id=session['id'],name=session['name'],position=session['position'],subjects=session['subjects'].split('\n'))
    else:

        return redirect(url_for('ClerkSystem.login',error="Você não fez login"))

@fe_clerk.route("/main/ticket_list/<subjects>")
def make_complete_list(subjects):
    list_subject = subjects.split("/n")
    result = Ticket.query.all()
    tickets = [ticket for ticket in result if ticket.subject in list_subject]
    return render_template("ticket_list.html",tickets=tickets)

@fe_clerk.route("/main/ticket_list_by_clerk/<identificador>")
def make_complete_choosen_list(identificador):
    result = Ticket.query.all()
    clerk_history = History.query.filter(History.clerk_id == identificador).all()
    #print([x.ticket_id for x in clerk_history])
    ticket_ids = [his.ticket_id for his in clerk_history]
    tickets = [ticket for ticket in result if ticket.id in ticket_ids ]
    #print(tickets)
    return render_template("ticket_list_choosen.html", tickets=tickets)



## Cadastro page


## Clerk Page



### Clerk Page tem, pode escolher entre escolher um ticket, e ver o historico de tickets