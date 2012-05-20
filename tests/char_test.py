#!/usr/bin/env python

import unittest
import char

class TestChar(unittest.TestCase):
"""
    Unit Test for the player class
"""
    def setUp(self):
        self.testPlayer = char.Player(s = 15, d = 18, c = 20,\
                                      i = 10, w = 12, C = 8 )

    def test___init__(self):
        self.assertEqual( self.testPlayer.stats['str'], 15 )
        self.assertEqual( self.testPlayer.stats['dex'], 18 )
        self.assertEqual( self.testPlayer.stats['con'], 20 )
        self.assertEqual( self.testPlayer.stats['int'], 10 )
        self.assertEqual( self.testPlayer.stats['wis'], 12 )
        self.assertEqual( self.testPlayer.stats['cha'], 8 )
        self.assertEqual( self.testPlayer.stats['bab'], 4 )

        self.assertIsInstance( self.testPlayer.stats, dict )
        self.assertIsInstance( self.testPlayer.saves, dict )
        self.assertIsInstance( self.testPlayer.weapons, list )

        self.assertEqual( self.testPlayer.level, 1 )

    def test_calcBonus(self):
        self.assertEqual( self.testPlayer.calcBonus(19), 4 )
        self.assertEqual( self.testPlayer.calcBonus(12), 1 )
        self.assertEqual( self.testPlayer.calcBonus(11), 0 )
        self.assertEqual( self.testPlayer.calcBonus(10), 0 )
        self.assertEqual( self.testPlayer.calcBonus(9), -1 )
        self.assertEqual( self.testPlayer.calcBonus(8), -1 )
        self.assertEqual( self.testPlayer.calcBonus(7), -2 )

    def test_melee(self):
        self.assertEqual( self.testPlayer.melee(), (4 + 2) )

    def test_ranged(self):
        self.assertEqual( self.testPlayer.ranged(), (4 + 4) )

if __name__ == '__main__':
    unittest.main()
