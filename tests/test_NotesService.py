import unittest
from unittest.mock import *
from src.sample.Note import Note
from src.sample.NotesStorage import NotesStorage
from src.sample.NotesService import NotesService


class TestNotesService(unittest.TestCase):
    def setUp(self):
        self.temp = NotesService()

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_notes_service_average(self, getAllNotesOf):
        self.temp.add(Note("Grzes", 5.0))
        self.temp.add(Note("Grzes", 4.0))
        getAllNotesOf.return_value = [Note("Grzes", 5.0), Note("Grzes", 4.0)]
        self.assertEqual(self.temp.averageOf("Grzes"), 4.5)

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_notes_service_average_wrong_type(self, getAllNotesOf):
        getAllNotesOf.side_effect = TypeError("Wrong type")
        self.assertRaises(TypeError, self.temp.averageOf, [51])

    @patch.object(NotesStorage, "getAllNotesOf")
    def test_add_note(self, getAllNotesOf):
        self.temp.add(Note("Scooby", 3.0))
        getAllNotesOf.return_value = [Note("Scooby", 3.0)]
        self.assertEqual(self.temp.averageOf("Scooby"), 3.0)

    def test_clear_notes(self):
        self.temp.add(Note("Marek", 4.5))
        self.temp.clear()
        self.temp.notes_storage.notes = []
        self.assertEqual(self.temp.notes_storage.notes, [])