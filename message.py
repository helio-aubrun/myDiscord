from database import Database
from datetime import datetime

class Message:

    def __init__(self, db):
        self.db = db


    def add_message (self, id_channel, content, id_user):

        #give the time when the fonction is called
        current_time = datetime.now()

        query = "INSERT INTO message (id_channel, content, id_user, time) VALUES (?,?,?,?)"
        values = (id_channel, content, id_user, current_time)
        self.db.execute_query(query, values)


    def delete_message(self, id_message):
        
        query = "DELETE FROM category WHERE id = %s"
        self.db.execute_query(query, (id_message,))