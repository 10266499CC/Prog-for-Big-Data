# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 14:09:22 2020

@author: User1
"""
#################################################################
# 10 Functional Calculator with Map Reduce Filter & Generator
#################################################################
    
# 1) Using Lambda on its own: Add 2 numbers together

add = lambda x, y : x + y
print(add(1,2))

# 2) Using Map: Square numbers in a given sequence 

sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences) 
print(list(filtered_result))

# 3) Using Filter: Output the odd numbers in a given range

num_list = [2,3,4,5,6]
odd_num = list(filter(lambda x: x%2!=0 , num_list))
print(odd_num)

# 4) Using Reduce: Find the sum of a list of numbers

import functools 
import operator 
num_list = [ 1 , 3, 5, 6, 2, ] 
   
print ("The sum of the list elements is : ",end="") 
print (functools.reduce(operator.add,num_list)) 

# 5) Using Reduce: Find the number of elements in a list greater than 5

from functools import reduce
 
test_list = [1, 7, 5, 6, 3, 8] 
print ("The list : " + str(test_list)) 

count = reduce(lambda sum, j: sum  + (1 if j > 5 else 0), test_list, 0) 
print ("The numbers greater than 5 : " + str(count)) 

# 6) Using Map and Filter within Reduce 

d = reduce(lambda x,y: x+y,map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))) 
print(d)

# 7) List Comprehension: Square the even numbers in a given list

num_list = [2,3,4,5,6]
sq_list = [x*x for x in num_list if x%2==0]
sq_list

# 8) List Comprehension: Pythagorean triples

def pythagorean(n):
	for x in range(1,n):
		for y in range(x,n):
			for z in range(y,n):
				if x**2 + y**2 == z**2:
					yield (x,y,z)

output = pythagorean(30) 
print(output)

# 9) Generator: Fibonacci Sequence

def fibonacci(xterms):
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

fib = fibonacci(5)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

# 10) Generator: Find all the prime numbers

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
    
    