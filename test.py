# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 18:55:30 2020

@author: User1
"""
import unittest

#################################
Functions to be tested
#################################

    def add(x, y):
        print(lambda x, y : x + y)
   
    def sqr_num_seq():
        n = int(input("Enter the size of list : "))
        userlist = list(map(int, input("Enter the list numbers separated by space : ").strip().split()))[:n]
        print("User List: ", userlist)
        for x in userlist:
            filtered_result = map (lambda x: x*x, userlist) 
            print(list(filtered_result))
           
    def odd_nums():
        n = int(input("Enter the size of list : "))
        userlist = list(map(int, input("Enter the list numbers separated by space : ").strip().split()))[:n]
        print("User List: ", userlist)
        for x in userlist:
            odd_num = list(filter(lambda x: x%2!=0 , userlist))
            print(odd_num)
    
    def sum_of_nums():
        n = int(input("Enter the size of list : "))
        userlist = list(map(int, input("Enter the list numbers separated by space : ").strip().split()))[:n]
        print("User List: ", userlist)
        for x in userlist:
            print ("The sum of the list elements is : ",end="")
            print (functools.reduce(operator.add,num_list))
            
    def convert_f_to_c():
         x = float(input("Enter the temperature you want to convert : "))
         fahrenheit = map(lambda x: (float(9)/5)*x + 32)
         print(fahrenheit)
    
    def find_num():
        x = int(input("Enter first number:"))
        y = int(input("Enter first number:"))
        d = reduce(lambda x,y: x+y,map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))
        print(d)
    
    def sqr_even_num():
        n = int(input("Enter the size of list : "))
        userlist = list(map(int, input("Enter the list numbers separated by space : ").strip().split()))[:n]
        print("User List: ", userlist)
        for x in userList:
            sq_list = [x*x for x in userlist if x%2==0]
            print(sq_list)
    
    def sqr_even_num():
        n = int(input("Enter the size of list : "))
        userlist = list(map(int, input("Enter the list numbers separated by space : ").strip().split()))[:n]
        print("User List: ", userlist)
        for x in userList:
            sq_list = [x*x for x in userlist if x%2==0]
            print(sq_list)
    
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

###########################################
# Unit test
##########################################

class TestCalculator(unittest.TestCase):

    def testadd(self):
        self.assertEqual(4, add(2,2))
        self.assertEqual(10, add(5, 5))
    
    def testadd(self):
        self.assertEqual(4, add(2,2))
        self.assertEqual(10, add(5, 5))
    
    

    def testCube(self):
        self.assertEqual(125, cube(5))
        self.assertEqual(1, cube(1))
        self.assertEqual(-8, cube(-2))

if __name__ == '__main__':
    unittest.main()