#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:14:55 2020

@author: microp11, Manmohan

Game of Life v0.01
"""

from game import Game
from board import Board

import unittest

class TestGame(unittest.TestCase):
    """Unit tests for the Game class."""    
    
    def setUp(self):
        self.game1 = Game()
    
    def test___init__(self):
        self.assertIsInstance(self.game1._board, Board)
        self.assertFalse(self.game1._allowed_to_continue)
        
    def test_initialize(self):
        # print('a:', self.game1._allowed_to_continue)
        self.game1.initialize(clear=True)
        self.assertTrue(self.game1._allowed_to_continue, '_allowed_to_continue should be True!')
    
    def test_stop(self):
        self.game1.stop()
        self.assertFalse(self.game1._allowed_to_continue)
        
if __name__ == '__main__':
    unittest.main()