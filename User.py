import mysql.connector
from database import Database

class user:
    def __init__(self,db):
       self.db= db

    


    def add_user ( self, nom, pseudo, email, mdp):
         query = "INSERT INTO user (nom, pseudo, email, mdp) VALUES (?,?,?,?)"
         values = (nom, pseudo, email, mdp)
         self.db.execute_query(query, values)

    def delete_user(self, nom, pseudo, email, mdp):
        
        query = "DELETE FROM category WHERE id = %s"
        self.db.execute_query(query, (nom, pseudo, email, mdp))