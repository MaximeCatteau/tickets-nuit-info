import datetime

import mysql.connector


# Classe qui va lier l'object ticket à la base de données SQL
class TicketModel:

    # Constructeur
    def __init__(self, title, ip_address, team_name, description):
        # Connexion à la SQL Database
        host = "127.0.0.1"
        user = "rootnuitinfo"
        password = "root"
        db = "tickets"
        self.con = mysql.connector.connect(host=host, user=user, password=password, db=db,
                                           auth_plugin='mysql_native_password')
        self.cur = self.con.cursor()

        # Paramètres du formulaire
        self.title = title
        self.ip_address = ip_address
        self.team_name = team_name
        self.description = description

    # Envoi d'un ticket à la database
    def send_ticket(self):
        now = datetime.datetime.now().strftime("le %d/%m/%y à %Hh%Mmin%Ss")
        self.cur.execute("INSERT INTO tickets(team_name, ip_address, title, description, date, archived) " +
                       "VALUES(%s, %s, %s, %s, %s, %s)", (self.team_name, self.ip_address, self.title, self.description,
                                                          now, False));
        self.con.commit()
        self.cur.close()

