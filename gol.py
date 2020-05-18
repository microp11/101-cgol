#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:14:50 2020

@author: microp11, Manmohan

Game of Life v0.01
"""

import numpy as np

class Game:
    """Game class for creating the Game of Life."""
    
    
    
    def __init__(self):
        """Creates a game object."""
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
        Starts the game by calling in a loop Next() on the _board verifying for a stop condition.

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
     
        
     
    
class Board:

    def __init__(self, rows, cols):
        """Creates a game object."""
        #self._board = Board(8, 8)
        
        self._rows = rows
        self._cols = cols
        self._current_generation = Generation(rows, cols)
        

    def __repr__(self):
        """Return string representation for repr()."""
        return f'Board()'     

    def __str__(self):
        """Return string representation for str()."""
        return f'' #'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation."""
        return f'' #'{str(self):{format}}'
    
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

    
class Generation:

    def __init__(self, rows, cols):
        """Creates a generation object."""
        #self._board = Board(8, 8)
        
        #first we create a list of cells
        count = 0
        list_of_cells = []
        for r in range(rows):
            for c in range(cols):
                list_of_cells.append((r, c, False))
                count += 1
        
        #then we create a np matrix from the list with the given shape
        self._cells = np.array(list_of_cells).reshape(rows, cols, 3)
       

    def __repr__(self):
        """Return string representation for repr()."""
        return f'Generation()'     

    def __str__(self):
        """Return string representation for str()."""
        return f'{self._cells}' #'{self.face} of {self.suit}'

    def __format__(self, format):
        """Return formatted string representation."""


        # just for test
        #self._cells[1][1][2] = 1

        s = ''
        
        rows = self._cells.shape[0]
        cols = self._cells.shape[1]
        for r in range(rows):
            for c in range(cols):
                if (self._cells[r][c][2]):
                    s = s + 'X'
                else:
                    s = s + '.'
            s = s + '\n'
        
        return s
    
    
# below code is not part of the module, it is used solely for testing

game1 = Game()
game1.initialize()
game1.start()

    