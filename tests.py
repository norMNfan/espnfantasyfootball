from main import League

import unittest

class TestLeagueApi(unittest.TestCase):

    def test_leagueCreationEmpty(self):
        self.league = League()

    def test_leagueCreationWithId(self):
        self.league = League(1360211)

    def test_leagueCreationWithIdAndYear(self):
        self.league = League(1360211, 2018)
"""
    def test_leagueAPICall(self):
        leagueId = 1360211
        league2 = League(leagueId);
        self.assertEqual(self.league, league2)
        """

if __name__ == '__main__':
    unittest.main()