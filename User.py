from database import Database

class User:


    def __init__(self):
       self.db = Database ()


    def add_user(self, nom, prenom, pseudo, email, mdp):
        if self.check_email(email):
            print('E-MAIL EXIST')
            return  # Stop execution if the email already exists
        elif self.check_pseudo(pseudo):
            print('PSEUDO EXIST')
            return  # Stop execution if the username already exists
        else:
            query = "INSERT INTO user (nom, prenom, pseudo, email, mdp, id_channel, admin) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (nom, prenom, pseudo, email, mdp,  1,  0)
            try:
                self.db.execute_query(query, values)
                print('USER ADD .')
            except Exception as e:
                print(f'Erreur lors de l\'ajout de l\'utilisateur: {e}')

    def delete_user(self, id):
        query = "DELETE FROM user WHERE id = %s"
        results = self.db.execute_query(query, (id,)) 
        return results

    def read_user_id(self, id):
        query = "SELECT * FROM user WHERE id = %s"
        results = self.db.fetch_all(query, (id,))  
        return results
    
    def read_user_pseudo(self, pseudo):
        query = "SELECT * FROM user WHERE pseudo = %s"
        results = self.db.fetch_all(query, (pseudo,))  
        return results


    def read_all_user(self):
        query = "SELECT * FROM USER"
        result = self.db.fetch_all(query)
        return result
    

    def check_email(self, email):
        query = "SELECT email FROM user WHERE email = %s"
        result = self.db.fetch_all(query, (email,))
        return result
            
    def check_pseudo(self, pseudo):
        query = "SELECT pseudo FROM user WHERE pseudo = %s"
        result = self.db.fetch_all(query, (pseudo,))
        return result

if __name__ == "__main__":
    test = User()
    test.add_user("lucas","lubin","testf", "dbfdfb", "pdksdicns")

    id_to_read = 2
    result = test.read_all_user()
    print(result)