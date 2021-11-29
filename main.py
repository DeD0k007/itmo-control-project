class PhoneContact:
    name = "Alex"
    contactNumber = 915
    note = "note"

    def __init__(self):
        self.result = str(self.name) + str(self.contactNumber) + str(self.note)
