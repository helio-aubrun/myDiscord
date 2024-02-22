from database import Database



class user:
    def __init__(self,db):
       self.db= db


    def add_user(self, nom, prenom, pseudo, email, mdp):
        query = "INSERT INTO user (nom, prenom, pseudo, email, mdp, id_channel, admin) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (nom, prenom, pseudo, email, mdp,   1,   0)  # Changé [1] en   1
        self.db.execute_query(query, values)

    def delete_user(self, nom, pseudo, email, mdp):
        query = "DELETE FROM user WHERE nom = %s AND pseudo = %s AND email = %s AND mdp = %s"
        self.db.execute_query(query, (nom, pseudo, email, mdp))

    def read_user(self, nom, prenom, pseudo, email, mdp, admin, id_channel):
        query = "SELECT * FROM user WHERE nom = %s AND prenom = %s AND pseudo = %s AND email = %s AND mdp = %s AND admin = %s AND id_channel = %s"
        values = (nom, prenom, pseudo, email, mdp, admin, id_channel)
        results = self.db.execute_query(query, values)
        return results

   
if __name__ == "__main__":
    db = Database(host="localhost", user="root", password="AstaxYuno972.", database="ma_base")
    test = user(db)
    test.delete_user("nom","pseudo", "email@example.com", "password")
