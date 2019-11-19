from flask import Flask, render_template, request

from TicketController import TicketController
from Database import Database

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def tickets():
    if request.method == "POST":
        db = Database()
        id = request.form["archive"]
        db.archive_ticket(id)
        return render_template("tickets.html")

    def db_query():
        db = Database()
        tickets = db.list_tickets()
        return tickets
    res = db_query()
    return render_template('tickets.html', result=res, content_type='application/json')


@app.route('/sendticket', methods=["GET", "POST"])
def send_ticket():
    if request.method == "POST":
        new_ticket = TicketController(request.form)
        return new_ticket.send_ticket()
    return render_template('ticket_form.html', content_type='application/json')


if __name__ == '__main__':
    app.run()
