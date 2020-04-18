# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:26:36 2020

@author: User1
"""
#####################
# This doesn't work
#####################

def add_num(x,y):
    return lambda x,y: x + y

import unittest

class TestCalculator(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(25, add_num(20, 5))

if __name__ == '__main__':
    unittest.main()

#####################
# This works
####################
add_num(20,5)
