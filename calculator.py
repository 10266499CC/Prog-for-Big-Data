# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:46:00 2020

@author: User1
"""
import sys
import operator
from functools import reduce

def menu():
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()
while True:
    choice = input("""
                      Welcome to the DBS 10 Functional Calculator with Map Reduce Filter
                      & Generator
                      Choose one of the following options:
                          
                      1: Add two numbers together
                      2: Multiply two numbers together
                      3: Identify the odd numbers in a given sequence 
                      4: Find the sum of a list of numbers
                      5: Convert Celcius to Fahrenheit
                      6: Find numbers greater than or equal to 3
                      7: List the first 10 square numbers 
                      8: Compute Pythagorean triples
                      9: Generate the Fibonnaci Sequence 
                      10: Find all the prime numbers
                      11: Quit

                      Please enter your choice: """)
    
    if choice == "1":
         add()
    elif choice == "2":
        sqr_num_seq()
    elif choice == "3":
        odd_nums()
    elif choice=="4":
        sum_of_nums()
    elif choice == "5":
        convert_f_to_c()
    elif choice == "6":
         find_num()
    elif choice=="7":
        first_ten_sqr_nums():
    elif choice == "8":
        pythagorean():
    elif choice == "9":
        fibonacci()
    elif choice=="10":
        find_prime()
    elif choice=="11":
        sys.exit
    else:
        print("Please try again")

menu()

class Calculator(object):
    
    def add(num1, num2):
        num1= int(input('Enter the first number'))
        num2= int(input('Enter the second number'))
        add= lambda x,y: x + y
        print(add(num1, num2))
   
    def multiply(num1, num2):
        num1= int(input('Enter the first number'))
        num2= int(input('Enter the second number'))
        multiply= lambda x,y: x * y
        print(multiply(num1, num2))
           
    def odd_nums(userlist):
        userlist = list(map(int, input("Enter the list numbers separated by space : ").strip().split()))[:n]
        print("User List: ", userlist)
        for x in userlist:
            odd_num = list(filter(lambda x: x%2!=0 , userlist))
            print(odd_num)
    
    def sum_of_nums(userlist): 
        userlist = list(map(int, input("Enter the list numbers separated by space : ").strip().split()))[:n]
        print("User List: ", userlist)
        for x in userlist:
            print ("The sum of the list elements is : ",end="")
            print (functools.reduce(operator.add,num_list))
            
    def convert_f_to_c(x):
         x = float(input("Enter the temperature you want to convert : "))
         fahrenheit = lambda x: (float(9/5)*x) + 32
         print(fahrenheit)
    
    def find_num(x):
        x = int(input("Enter first number:"))
        result = map(lambda x:x+x,filter(lambda x: (x>=3), (1,2,3,4)))
        print(result)
                   
    
    def first_ten_sqr_nums():
        squares = [ x**2 for x in range(10) ]
        print(squares)
    
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


                                

    

    
    