import mysql.connector


class Database:
    def __init__(self):
        host = "127.0.0.1"
        user = "rootnuitinfo"
        password = "root"
        db = "tickets"
        self.con = mysql.connector.connect(host=host, user=user, password=password, db=db,
                                           auth_plugin='mysql_native_password')
        self.cur = self.con.cursor()

    # Liste tous les tickets non archivés dans l'ordre
    def list_tickets(self):
        self.cur.execute("SELECT * FROM tickets WHERE archived=false ORDER BY date ASC")
        result = self.cur.fetchall()
        return result

    # Archive un ticket selon son ID
    def archive_ticket(self, ticket_id):
        self.cur.execute("UPDATE tickets SET archived=True WHERE id=%s", (ticket_id, ))
        self.con.commit()
        self.cur.close()