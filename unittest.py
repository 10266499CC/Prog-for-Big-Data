# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:26:36 2020

@author: User1
"""
########################
# Calculator Functions

# In the original code, 'userlist' is a user defined list of numbers.

# For test purposes,the user defined list will be 
# replaced by the following list: [1,2,3,4]

#################################
# Functions for non-list inputs
################################

add =lambda x,y: x + y

multiply =lambda x,y: x * y

convert_f_to_c = lambda x: (float(9/5)*x) + 32
       

###################################
# Unit testing for non-list inputs
###################################

import unittest

class TestCalculator(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(25, add(20, 5))
        
    def testMultiply(self):
        self.assertEqual(10, multiply(5,2))
    
    def testConvert_f_to_c(self):
        self.assertEqual(194.0, convert_f_to_c(90))
        
if __name__ == '__main__':
    unittest.main()

##################################
# Functions involving lists
##################################

odd_nums= list(filter(lambda x: x%2!=0 , [2,5,8,13,16]))
print(odd_nums)

from functools import reduce
import operator
sum_of_nums= reduce(operator.add, [1,2,3,4,5])
print(sum_of_nums)

result = map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))
print(list(result))    

squares = [ x**2 for x in range(10) ]
print(squares) 

##################################
# Unit tests for lists
#################################
import unittest

class TestCalculator(unittest.TestCase):

    def testOddnums(self):
        self.assertListEqual([5,3], odd_nums[2,5,8,13,16])
        
    def testSumofnums(self):
        self.assertListEqual([15], sum_of_nums[1,2,3,4,5])
    
    def testFind_num(self):
        self.assertListEqual([6,8], result([1,2,3,4])

    def testFindSquares(self):
        self.assertListEquaL([0,1,4,9,16,25,36,49,64,81], squares())
        
        
if __name__ == '__main__':
    unittest.main()
    

###################################
# Functions involving generators
##################################

    def pythagorean(n):
        n = int(input("Enter the range : "))
        for x in range(1,n):
            for y in range(x,n):
            for z in range(y,n):
                if x**2 + y**2 == z**2:
                    yield (x,y,z)
                    output = pythagorean(n)
                    print(output)
    
    def fibonacci(xterms):
        n = int(input("Enter your choice : "))
        x1 = 0
        x2 = 1
        count = 0
        
        if xterms <= 0:
            print("Please provide a +ve integer")
            elif xterms == 1:
                print("Fibonacci seq upto",xterms,":")
                print(x1)
                else:
                    while count < xterms:
                        xth = x1 + x2
                        x1 = x2
                        x2 = xth
                        count += 1
                        yield xth
                        fib = fibonacci(n)
                        print(next(fib))
     
        def find_prime():
            num = 1
            while True:
                if num > 1:
                    for i in range(2, num):
                        if (num % i) == 0:
                            break
                        else:
                            yield num
                            num += 1
                            for ele in find_prime():
                                print(ele)
                                
#########################################
# Generator Tester
#########################################

def generator_tester(generator, expected_values):   
    range_index = 0
    for actual in generator_iterator_to_test:
        assert range_index + 1 <= len(expected_values), 'Too many values returned from range'
        assert expected_values[range_index] == actual
        range_index += 1

    assert range_index == len(expected_values, 'Too few values returned from range'