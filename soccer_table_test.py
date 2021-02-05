import unittest

import self as self

import soccer_table

class SoccerTableTestCase(unittest.TestCase):
    def test_team_point(self):
        expected_output = [
            ('Tarantulas', 6),
            ('Lions', 5),
            ('FC Awesome', 1),
            ('Snakes', 1),
            ('Grouches', 0)
        ]
        team_point_table = soccer_table.team_point('soccer_input.txt')
        self.assertEqual(team_point_table, expected_output)

if __name__ == '__main__':
    unittest.main()