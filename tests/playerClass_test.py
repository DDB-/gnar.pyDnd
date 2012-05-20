#!/usr/bin/env python

import unittest
import playerClass

class TestPlayerClass(unittest.TestCase):
"""
    Unit Tests for the playerClass class 
"""
    def setUp(self):
        self.testClass = playerClass.PlayerClass()

    def test_saves(self):
        self.testClass
