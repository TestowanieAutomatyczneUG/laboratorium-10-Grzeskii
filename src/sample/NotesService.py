from src.sample.NotesStorage import NotesStorage

class NotesService:
    def __init__(self):
        self.notes_storage = NotesStorage()

    def add(self, note):
        self.notes_storage.add(note)

    def averageOf(self, name):
        if type(name) is not str:
            raise TypeError("Wrong type")
        all_notes = self.notes_storage.getAllNotesOf(name)
        result = 0
        for note in all_notes:
            result += note.get_note()
        return result / len(all_notes)

    def clear(self):
        self.notes_storage.clear()