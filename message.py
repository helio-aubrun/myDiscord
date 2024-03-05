from database import Database
from datetime import datetime

class Message:

    def __init__(self, ):
        self.db = Database ()


    def add_message (self, id_channel, content, id_user):

        #give the time when the fonction is called
        current_time = datetime.now()

        query = "INSERT INTO message (id_channel, content, id_user, time) VALUES (%s,%s,%s,%s)"
        values = (id_channel, content, id_user, current_time)
        self.db.execute_query(query, values)


    def delete_message(self, id_message):
        
        query = "DELETE FROM message WHERE id = %s"
        self.db.execute_query(query, (id_message,))

    def get_all_messages(self):
        query = "SELECT * FROM message"
        results = self.db.fetch_all(query)
        return results
    
    def get_messages_user(self, user):
        query = "SELECT * FROM message WHERE id_user = %s"
        values = (user,)
        results = self.db.fetch_all(query,values)
        return results
    
    def get_messages_channel(self, channel):
        query = "SELECT * FROM message WHERE id_channel = %s"
        values = (channel,)
        results = self.db.fetch_all(query,values)
        return results
    
if __name__ == "__main__":
    test = Message()
    test.add_message(1,"wewewe",1)
    test.add_message(1,"delete",2)
    test.add_message(1,"channel2 et user2",2)
    test.delete_message(37)
    print(test.get_all_messages())
    print(test.get_messages_channel(1))
    print(test.get_messages_channel(2))
    print(test.get_messages_user(1))
    print(test.get_messages_user(2))
    