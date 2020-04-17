# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:32:02 2020

@author: User1
"""

class Calculator(object):
 
    def add(self, x, y):
        number_types = (int, float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return lambda x, y : x + y
        else:
            raise ValueError
    
    def mymap(self, aFunc, aSeq):
	    result = []
	    for x in aSeq: result.append(aFunc(x))
	    return result
    
    def is_odd(self, x):
        num_list = []
        if x % 2 != 0:
           return True
        else:
            return False
    
    odd_num = list(filter(lambda x: x%2!=0 , num_list))
    print(odd_num)

    def myreduce(self, fnc, seq):
	    tally = seq[0]
	    for next in seq[1:]:
		    tally = fnc(tally, next)
	    return tally

    def pythagorean(self, n):
	    for x in range(1,n):
		    for y in range(x,n):
			    for z in range(y,n):
				     if x**2 + y**2 == z**2:
					     yield (x,y,z)
    
    def fibonacci(self, xterms):
     # first two terms
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
    
    def find_prime(self, num):
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
    