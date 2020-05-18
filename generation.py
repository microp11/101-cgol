#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 10:14:50 2020

@author: microp11, Manmohan

Game of Life v0.01
"""

import numpy as np

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


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)