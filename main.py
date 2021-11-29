class PhoneContact:

    def __init__(self):
        self.name = "Alex"
        self.contactNumber = 915
        self.note = "note"
        self.result = str(self.name) + str(self.contactNumber) + str(self.note)


class PhoneBook:

    def __init__(self):
        self.contactNumber = {"Alex": 915}

    def getContactByName(self, name):
        res = self.contactNumber.get(name)
        if not res:
            res = "Кажется такого человека нет в базе."
        return res

    def postNewContact(self, name, contactNumber):
        try:
            self.contactNumber[str(name)] = int(contactNumber)
        except ValueError:
            self.contactNumber[str(name)] = 123
