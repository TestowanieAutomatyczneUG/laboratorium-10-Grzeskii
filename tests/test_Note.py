import unittest
from src.sample.Note import Note


class TestNote(unittest.TestCase):

    def test_init(self):
        Note("ktos", 4.5)

    def test_get_name(self):
        example = Note("Grzes", 5.0)
        self.assertEqual(example.get_name(), "Grzes")

    def test_get_note(self):
        example = Note("Grzes", 4.5)
        self.assertEqual(example.get_note(), 4.5)

    def test_exception_empty_string(self):
        self.assertRaises(Exception, Note, "", 3.0)

    def test_exception_wrong_type_name(self):
        self.assertRaises(Exception, Note, 11, 4.5)

    def test_exception_none_name(self):
        self.assertRaises(Exception, Note, None, 5.0)

    def test_exception_wrong_type_note(self):
        self.assertRaises(Exception, Note, "Ktos", "Cos")

    def test_exception_note_small(self):
        self.assertRaises(Exception, Note, "Haha", 1.5)

    def test_exception_note_big(self):
        self.assertRaises(Exception, Note, "JHanek", 7.5)


if __name__ == "__main__":
    unittest.main()
