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

    def get_all_messages(self):
        query = "SELECT * FROM messsage"
        results = self.db.execute_query(query)
        return results
    
    def get_messages_user(self, user):
        query = "SELECT * FROM messsage WHERE id_user = %s"
        values = (user)
        results = self.db.execute_query(query, values)
        return results
    
    def get_messages_channel(self, channel):
        query = "SELECT * FROM messsage WHERE id_channel = %s"
        values = (channel)
        results = self.db.execute_query(query, values)
        return results