__author__ = 'lidan'

import unittest

from csc148.lab.lab1.lab01 import RaceRegistry


class TestRegistry(unittest.TestCase):

    def setUp(self):
        self.registry = RaceRegistry()
        self.registry.register('Gerhard','under 40')
        self.registry.register('Tom', 'under 30')
        self.registry.register('Toni','under 20')
        self.registry.register('Margot','under 30')
        self.registry.register('Gerhard','under 30')

    def test_nameunder30(self):
        self.assertEqual(self.registry.get_runner_list('under 30'),['Tom','Margot','Gerhard'])




if __name__ == 'main':
    unittest.main






