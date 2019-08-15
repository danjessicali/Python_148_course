__author__ = 'lidan'

import unittest
from lab2 import GradeEntry
from lab2 import LetterGradeEntry
from lab2 import NumericGradeEntry

class TestLetterGradeEntry(unittest.TestCase):

    def setUp(self):
        self.lettergrade = LetterGradeEntry('CSC148','0,5','99')
        self.numricgrade = NumericGradeEntry('CSC148','0,5','99')

    def testNumeric(self):
        self.assertEqual(self.numricgrade.get_grade(),4.0)
        print(self.numricgrade.get_grade())


if __name__ == 'main':
    unittest.main

