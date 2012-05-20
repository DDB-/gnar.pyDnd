#!/usr/bin/env python

import unittest
import weapon

class TestWeapon(unittest.TestCase):
"""
    Unit Tests for the weapon class
"""
    def setUp(self):
        self.testWeapon = weapon.Weapon()
