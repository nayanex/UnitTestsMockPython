import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):
    def SetUp(self):
        self.phonebook = Phonebook()

    @unittest.skip("WIP")
    def test_lookup_entry_by_name(self):
        self.phonebook.add("Bob", "12345")
        self.assertEqual("12345", self.phonebook.lookup("Bob"))
    
    @unittest.skip("WIP")
    def test_missing_entry_raises_KeyError(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup("missing")
    
    @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("WIP")
    def test_phonebook_with_normal_entries_is_consistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "012345")
        self.assertTrue(self.phonebook.is_consistent())

    @unittest.skip("WIP")
    def test_phonebook_with_duplicate_entries_is_inconsistent(self):
        self.phonebook.add("Bob", "12345")
        self.phonebook.add("Mary", "12345")
        self.assertFalse(self.phonebook.is_consistent())

    @unittest.skip("WIP")
    def test_phonebook_with_numbers_that_prefix_one_another_is_inconsistent(self):
        self.phonebook.add("Bob","12345")
        self.phonebook.add("Mary", "123")
        self.assertFalse(self.phonebook.is_consistent())

    @unittest.skip("WIP")
    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Sue", "12345")
        self.assertIn("Sue", phonebook.get_names())
        self.assertIn("12345", phonebook.get_numbers())