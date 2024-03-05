from database import Database

class Channel :
    def __init__(self) -> None:
        self.db = Database ()

    def get_channels_number (self) :
        query = "SELECT * FROM channel"
        results = self.db.fetch_all(query)
        return results [-1][0]

if __name__ == "__main__":
    test=Channel ()
    test.get_channels_number ()