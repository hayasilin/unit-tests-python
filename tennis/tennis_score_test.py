import unittest
from tennis_score import TennisScore

class TennisScoreTest(unittest.TestCase):
    def setUp(self):
        self.sut = TennisScore()

    def test_love_all(self):
        self.assertEqual("Love All", self.sut.get_score())

    def test_fifteen_love(self):
        self.sut.add_score(1, 1)
        self.assertEqual("Fifteen Love", self.sut.get_score())

    def test_thirty_love(self):
       self.sut.add_score(1,2)
       self.assertEqual("Thirty Love", self.sut.get_score())

    def test_forty_love(self):
       self.sut.add_score(1, 3)
       self.assertEqual("Forty Love", self.sut.get_score())

    def test_love_fifteen(self):
       self.sut.add_score(2, 1)
       self.assertEqual("Love Fifteen", self.sut.get_score())

    def test_love_thirty(self):
       self.sut.add_score(2, 2)
       self.assertEqual("Love Thirty", self.sut.get_score())

    def test_love_forty(self):
       self.sut.add_score(2, 3)
       self.assertEqual("Love Forty", self.sut.get_score())

    def test_fifteen_all(self):
       self.sut.add_score(1, 1)
       self.sut.add_score(2, 1)
       self.assertEqual("Fifteen All", self.sut.get_score())

    def test_thirty_all(self):
       self.sut.add_score(1, 2)
       self.sut.add_score(2, 2)
       self.assertEqual("Thirty All", self.sut.get_score())

