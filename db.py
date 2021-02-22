import sqlite3


class Database:
    # intialize db
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        # create passwords table ONLY IF it does not exist (creates one time)
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, website text, password_ text)")
        self.connection.commit()

    # insert website and password

    def insert_data(self, website, password):
        self.cursor.execute("INSERT INTO passwords VALUES(NULL, ?, ?)",
                            (website, password))
        self.connection.commit()

    # get the websites and passwords

    def get_data(self):
        self.cursor.execute("SELECT * FROM passwords")
        rows = self.cursor.fetchall()  # get all data from passwords table
        return rows  # return id, website, password_

    # remove specific data i.e website AND password in database (grab using id)

    def delete_data(self, id):
        # grab id and it will delete BOTH website and password associated with it
        # one item tuple requires comma
        self.cursor.execute("DELETE FROM passwords WHERE id=?", (id,))
        self.connection.commit()

    # update with new website and password
    def update_data(self, id, new_website, new_password):
        # update data
        self.cursor.execute(
            "UPDATE passwords SET website=?, password_=? WHERE id=?",
            (new_website, new_password, id))
        self.connection.commit()  # ALWAYS COMMIT CHANGES when making changes to db

    def __del__(self):
        self.connection.close()


db = Database("passwords")
print(db.get_data())
