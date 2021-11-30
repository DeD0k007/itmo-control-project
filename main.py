import config
import sqlite3

database = config.PATH_TO_DATABASE


class PhoneContact:

    def __init__(self):
        self.name = "Alex"
        self.contactNumber = 915
        self.note = "note"
        self.result = str(self.name) + str(self.contactNumber) + str(self.note)


class PhoneBook:

    def __init__(self, database_file):
        self.connection = sqlite3.connect(database_file, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()

    def getContactByName(self, name):
        _SQL = """SELECT * FROM contacts
                            WHERE name = ?"""
        res = self.cursor.execute(_SQL, (name,)).fetchone()
        if not res:
            res = "Кажется такого человека нет в базе."
        return res["number"]

    def postNewContact(self, name, contactNumber, note="No"):
        _SQL = """INSERT INTO contacts
                            (name, number, note)
                            VALUES
                            (?, ?, ?)"""
        self.cursor.execute(_SQL, (name, contactNumber, note))
        self.connection.commit()

    def __del__(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
