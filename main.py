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
        return self.contactNumber.get(name)

    def postNewContact(self, name, contactNumber):
        self.contactNumber[name] = contactNumber
