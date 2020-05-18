#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:14:50 2020

@author: microp11, Manmohan

Game of Life v0.01
"""

from board import Board

class Game:
    """Game class for creating the Game of Life."""
    
    
    
    def __init__(self):
        """Creates a game object.
        
        >>> game1 = Game()
        >>> game1
        Game()
       
        
        """
        self._allowed_to_continue = False
        self._board = Board(8, 8)
        

    def __repr__(self):
        """Return string representation for repr()."""
        return f'Game()'     

    def __str__(self):
        """Return string representation for str()."""
        return f'for printing' #'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation."""
        return f'formatted' #'{str(self):{format}}'

    def initialize(self, clear=False):
        """
        Initializes the _board with a pattern or a number of random cells.
        
        Assumes the board exists and if random cells are to be created, they will be created on the board
        somewhere in the middle and grouped together.
        
        If a pattern is given, the board has to be at least the size of the pattern...

        Parameters
        ----------
        clear : TYPE, optional
            DESCRIPTION. The default is False.

        Returns
        -------
        None.

        """
        
        self._allowed_to_continue = True
        
        
    def start(self):
        """
        Starts the game by calling in a loop next() on the _board verifying for a stop condition.

        Returns
        -------
        None.

        """
        while (self._allowed_to_continue):
            self._board.next()
            
            while (True):
                answer = input('Should we continue? Type Y or N: ')
                if (answer.upper() == 'Y'):
                    break
                elif (answer.upper() == 'N'):
                    self._allowed_to_continue = False
                    break
                    
               
            
            
    def stop(self):
        """
        Stops the game by setting the stop condition.
        Currently unused or obsolete.

        Returns
        -------
        None.

        """
        
        self._allowed_to_continue = False
        
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)
    