# # # 1. Add Two Numbers

# # # Problem:
# # # Write a function add_numbers(a, b) that returns the sum of two integers.
# def add_numbers(a,b):
#     return a+b
# a=int(input('Enter first number:'))
# b=int(input('Enter second number:'))
# print(add_numbers(a,b))
# # 2. Check Even or Odd

# # Write a function check_even_odd(n) that returns "Even" if n is even, otherwise "Odd".
# def even_odd_check(n):
#     if n%2==0:
#         return "Even"
#     return "odd"
# n=int(input())
# print(even_odd_check(n))

# # 3. Find Maximum of Three Numbers

# # Write a function maximum(a, b, c) that returns the largest number.
# def maximum(a,b,c):
#     if a>=b and a>=c:
#         return a
#     elif b>=a and b>=c:
#         return b
#     else:
#         return c
# a=int(input())
# b=int(input())
# c=int(input())
# print(maximum(a,b,c))
# 4. Calculate Factorial

# Write a function factorial(n) that returns n!.
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input())
# print(factorial(n))    
# 5. Check Prime Number

# Write a function is_prime(n) that returns True if n is prime, otherwise False.
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range (2, n):
#         if n%i==0:
#             return False
#     return True
# n=int(input())
# if is_prime(n):
#     print("Prime")
# else:
#     print("Not Prime")   



#     6. Sum of Digits

# Write a function digit_sum(n) that returns the sum of all digits. 
# def sum(n):
#     total=0
#     while n>0:
#         total = total +n%10
#         n=n//10
#     return total
# n= int(input())
# print(sum(n))


# 7. Reverse a Number

# def reverse(n):
#     rev=0
#     while n>0:
#         rev=rev*10+n%10
#         n=n//10
#         return rev
#     n=int(input())
#     print(reverse(n))


# 8. Check Palindrome

# Write a function that checks whether a string is a palindrome.
# def is_palindrome(n):
#     if int(str(n)[::-1])==n:
#         return True
#     return False
# n= int(input())
# if is_palindrome(n):
#     print("yes")
# else:
#     print("no") 



 

# 9. Count Vowels

# Write a function count_vowels(s) that returns the number of vowels. 

# def vowel_count(s):
#     count=0
#     for ch in s:
#         if ch in "aeiouAEIOU":
#             count=count+1
#     return count
# s=input()
# print (vowel_count(s))
             

# 11. Sum of List Elements

# Write a function list_sum(numbers) that returns the sum of all elements.

# def list_sum(numbers):
#     total=0
#     for num in numbers:
#         total=total+num
#     return total

# numbers=list(map(int,input().split()))
# print(list_sum(numbers)) 


# #   12. Find Largest Element Without max()

# Input

# 10 25 7 40 18

# Output

# 40


# def find_largest(numbers):
#     largest=numbers[0]
#     for num in numbers:
#         if num>largest:
#             largest=num
#     return largest
# numbers=list(map(int,input().split()))
# print(find_largest(numbers))        



# # # 13. Count Even Numbers

# # # Input

# # # 1 2 4 7 8 11 12

# # # Output

# def count_even(numbers):
#     count=0
#     for num in numbers:
#         if num%2==0:
#             count=count+1
#     return count
# numbers=list(map(int,input().split()))
# print(count_even(numbers))        

# # # 15. Remove Duplicates Using a Function

# # # Input

# # # 1 2 2 3 4 4 5 5

# # # Output

# # # 1 2 3 4 5
# def remove_duplicate(numbers):
#     result=[]
#     for num in numbers:
#         if num not in result:
#             result.append(num)
#     return result

# numbers= list(map(int,input().split()))
# print(remove_duplicate(numbers))        


# 16. Second Largest Element

# Input

# 10 5 20 8 20 15

# Output

# 15


# def second_largest(numbers):
#     unique_numbers= list(set(numbers))
#     unique_numbers.sort()
#     return unique_numbers[-2]
# numbers=list(map(int,input().split()))
# print(second_largest(numbers))



# # 18. Check Anagram

# # Two strings are anagrams if they contain the same characters with the same frequencies.

# # Input

# # listen
# # silent

# # Output

# # Anagram

# def is_anagram(s1,s2):
#     return sorted(s1)==sorted(s2)
# s1=input()
# s2=input()
# if is_anagram(s1,s2):
#     print("Anagram")
# else:
#     print("Not Anagram")    

# # Level 3 — Default Arguments, *args, **kwargs, Lambda

# 21. Default Argument

# # Create a function:

# # greet(name, message="Welcome")

# # Input

# # Aditya

# # Output

# # Hello Aditya, Welcome


# def greet(name, message="Welcome"):
#     return f"Hello {name}, {message}"


# name = input()

# print(greet(name))

# # 22. Variable Number of Arguments — *args

# # Write a function that accepts any number of integers and returns their sum.

# # Input

# # 10 20 30 40 50

# # Output

# # 150

# def calculate_sum(*args):
#     total = 0

#     for num in args:
#         total += num

#     return total


# numbers = list(map(int, input().split()))

# print(calculate_sum(*numbers))

# # 23. **kwargs — Student Information

# # Create a function that accepts student information using keyword arguments.

# # Input

# # Aditya 26 8.5

# # Output

# # Name: Aditya
# # Age: 26
# # CGPA: 8.5


# def student_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# name, age, cgpa = input().split()

# student_info(
#     Name=name,
#     Age=age,
#     CGPA=cgpa
# )


# # 24. Lambda — Square Numbers

# # Write a function that uses a lambda to square every number.

# # Input

# # 1 2 3 4 5

# # Output

# # 1 4 9 16 25


# def square_numbers(numbers):
#     square = lambda x: x * x

#     return [square(num) for num in numbers]


# numbers = list(map(int, input().split()))

# print(*square_numbers(numbers))


# # 25. Use map() with a Function

# # Convert a list of Celsius temperatures into Fahrenheit.

# # Formula:

# # F = (C × 9/5) + 32

# # Input

# # 0 10 20 30

# # Output

# # 32.0 50.0 68.0 86.0

# def celsius_to_fahrenheit(c):
#     return (c * 9 / 5) + 32


# temperatures = list(map(float, input().split()))

# result = list(map(celsius_to_fahrenheit, temperatures))

# print(*result)


# # 26. Use filter() with a Function

# # Return only numbers greater than 50.

# # Input

# # 10 55 20 80 90 45

# # Output

# # 55 80 90

# def greater_than_50(n):
#     return n > 50


# numbers = list(map(int, input().split()))

# result = list(filter(greater_than_50, numbers))

# print(*result)

# # 27. Use reduce()

# # Find the product of all numbers.

# # Input

# # 1 2 3 4 5

# # Output

# # 120

# # from functools import reduce


# def multiply(a, b):
#     return a * b


# numbers = list(map(int, input().split()))

# result = reduce(multiply, numbers)

# print(result)

# # Level 4 — Recursion & Nested Functions
# # 28. Recursive Factorial

# # Write a recursive function to calculate factorial.

# # Input

# # 5

# # Output

# # 120


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1

#     return n * factorial(n - 1)


# n = int(input())

# print(factorial(n))

# # 29. Recursive Fibonacci

# # Write a recursive function to find the nth Fibonacci number.

# # Input

# # 7

# # Output

# # 13


# def fibonacci(n):
#     if n == 0:
#         return 0

#     if n == 1:
#         return 1

#     return fibonacci(n - 1) + fibonacci(n - 2)


# n = int(input())

# print(fibonacci(n))

# ##Nested Function

# # Problem Statement

# # Write a function calculate() that contains a nested function square(). The nested function should calculate the square of a number.

# # For input 5, the output should be: 25

# def calculate(n):
#     def square(x):
#         return x*x
#     return square(n)
# print(calculate(5))

# Problem 2 — Nested Function for Even/Odd
# Problem Statement

# Create a function check_number(n).

# Inside it, create a nested function is_even(n) that returns True if the number is even and False otherwise.

# def check_number(n):
#     def is_even(x):
#         return x%2==0
#     if is_even(n):
#         return "Even"
#     else:
#         return "odd"
    
# print(check_number(10))
# print(check_number(7))

# Problem 3 — Nested Function With Two Calculations
# Problem Statement

# Create a function calculate(a, b).

# Inside it:

# Create a nested function add()
# Create another nested function multiply()
# Return both results.

# def calculate(a,b):
#     def add():
#         return a+b
#     def multiply():
#         return a*b
#     return add(), multiply()
# x,y=calculate(5,4)
# print(x)
# print(y)

# Problem 4 — Nested Function With a List
# Problem Statement

# Given a list of numbers, create a function process_numbers().

# Inside it, create a nested function is_positive() that checks whether a number is positive.

# Return a list containing only positive numbers.

def process_numbers(numbers):
    def is_positive(n):
        return n>0
    result=[]
    for n in numbers:
         if is_positive(n):
            result.append(n)
    return result


numbers = [-5, 10, -2, 7, 0, 8]

print(process_numbers(numbers))

