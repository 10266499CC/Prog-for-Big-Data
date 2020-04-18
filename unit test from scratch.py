# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:12:18 2020

@author: User1
"""
import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)

