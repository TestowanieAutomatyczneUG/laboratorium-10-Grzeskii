class Note:
    def __init__(self, name, note):
        if name is None:
            raise Exception("Can't be none")
        if name == "":
            raise Exception("Can't be empty")
        if note < 2 or note > 6:
            raise Exception("Must be between 2 and 6")
        if type(name) is not str or type(note) is not float:
            raise Exception("Wrong type")
        self.name = name
        self.note = note

    def get_note(self):
        return self.note

    def get_name(self):
        return self.name