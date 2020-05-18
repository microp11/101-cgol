#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:14:50 2020

@author: microp11, Manmohan

Game of Life v0.01
"""

from generation import Generation

class Board:

    def __init__(self, rows, cols):
        """Creates a game object."""
        #self._board = Board(8, 8)
        
        self._rows = rows
        self._cols = cols
        self._current_generation = Generation(rows, cols)
        

    def __repr__(self):
        """Returns the “official” string representation of an object (a representation that has all information about the object)."""
        return f'Board()'     

    def __str__(self):
        """Returns the “informal” string representation of an object (a representation that is useful for printing the object)."""
        return f'Board {self._rows} by {self._cols}'

    def __format__(self, format):
        """Returns a formatted string that holds a printable representation of an object."""
        return f''
    
    def next(self):
        """
        Advances the board to the next generation.
        
        Returns
        -------
        None.

        """
        self.render()
        self._past_generation = self._current_generation
        
        # we iterate through all the spaces in the board and we compute the _current_generation
        
        
        


    def render(self):
        """
        Prints the current board as a matrix of spaces and Xs.
        
        ........
        ........
        .....X..               
        ....XX..               
        ....XX..               
        ........
        ........
        ........

        Returns
        -------
        None.

        """
        return print(f'{self._current_generation}')


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)