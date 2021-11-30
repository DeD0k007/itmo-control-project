import config
import sqlite3
import telebot

API_KEY = config.API_KEY

bot = telebot.TeleBot(API_KEY)


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
        try:
            _SQL = """SELECT * FROM contacts
                                WHERE name = ?"""
            res = self.cursor.execute(_SQL, (name,)).fetchone()
            if not res:
                res = "Кажется такого человека нет в базе."
            return res["number"]
        except Exception:
            return "Такого человека нет в базе."

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


dbConnecting = PhoneBook(database)


def get_person(message):
    name = message.text
    res = dbConnecting.getContactByName(name)
    bot.send_message(message.chat.id, str(res))


def add_person(message, name):
    number = message.text
    dbConnecting.postNewContact(name, number)
    bot.send_message(message.chat.id, "Ok")


def add_person_name(message):
    name = message.text
    text = 'Введите номер человека'
    sent = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent, add_person, name)


@bot.message_handler(commands=['add_person'])
def add(message):
    text = 'Введите имя человека'
    sent = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent, add_person_name)


@bot.message_handler(commands=['get'])
def get(message):
    text = 'Введите имя человека'
    sent = bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(sent, get_person)


bot.polling(none_stop=True)
