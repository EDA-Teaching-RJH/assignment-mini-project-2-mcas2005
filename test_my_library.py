import unittest
from my_library import Person

class TestPerson(unittest.TestCase):
    def test_greet(self):
        person= Person("Alice")
        self.assertEqual(person.greet(), "hello, my name is alice" )

    def test_str(self):
        person = Person("Bob")
        self.assertEqual(str(person), "bob")

if __name__=="__main__":
    unittest.main()
