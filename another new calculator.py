# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:46:00 2020

@author: User1
"""
import sys
import operator
from functools import reduce

def main():
    print("************MAIN MENU**************")
    #time.sleep(1)
    print()

    choice = input("""
                      Welcome to the DBS 10 Functional Calculator with Map Reduce Filter
                      & Generator
                      Choose one of the following options:
                          
                      1: Add two numbers together
                      2: Square numbers in a given sequence
                      3: Identify the odd numbers in a given sequence 
                      4: Find the sum of a list of numbers
                      5: Convert Celcius to Fahrenheit
                      6: Find numbers less than or equal to 3
                      7: Square the even numbers in a given list
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
        sqr_even_num()
    elif choice == "8":
        viewstudentdetails()
    elif choice == "9":
        fibonacci()
    elif choice=="10":
        find_prime()
    elif choice=="11":
        sys.exit
    else:
        print("Please try again")

main()

class Calculator(object):
    
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


    
    