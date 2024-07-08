import unittest
from Soundex import generate_soundex

class TestSoundex(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(generate_soundex(""), "")

    def test_single_character(self):
        self.assertEqual(generate_soundex("A"), "A000")
        
    def test_string_with_special_characters(self):
        self.assertEqual(generate_soundex("1@!Abc3"),"1120")
        
    def test_string_with_vowels(self):
        self.assertEqual(generate_soundex("Robert"),"R163")
  
if __name__ == '__main__':
    unittest.main()

