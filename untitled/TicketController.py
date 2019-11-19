from flask import render_template
from TicketModel import TicketModel


class TicketController:
    def __init__(self, form=None):
        if form:
            self.title = form["title"]
            self.ip_address = form["ip_address"]
            self.description = form["description"]
            self.team_name = form["team_name"]
            self.ticket = TicketModel(self.title, self.ip_address, self.team_name, self.description)

    def send_ticket(self):
        self.ticket.send_ticket()
        return render_template("tickets.html")