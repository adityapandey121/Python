# # class student:
# #     def __init__(self, age, name, marks):
# #         self.name= name()
# #         self.age=age()
# #         self.marks=marks()
# #     def display(self):
# #         print(self.name)
# #         print(self.marks)

# # s1 = student("Aditya", 85)

# # s1.display()

# class student:
#     def __init__(self, name, m1, m2, m3):
#         self.name=name
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def   average(self):
#         return(self.m1+self.m2+self.m3)/3 
# s = student("Aditya", 80, 90, 70)

# print(s.average())    

# #Question 1 — Student Information
# # Problem Statement

# # You are given the details of a student. Your task is to create a Student class that stores the student's name, age, and marks.

# # The class should contain a method display() that prints the student's information in the required format.

# # Create an object of the Student class using the given input and call the display() method.

# # Input Format

# # The first line contains a string representing the student's name.

# # The second line contains an integer representing the student's age.

# # The third line contains an integer representing the student's marks.

# # Output Format

# # Print the student's information in the following format:

# # Name: <name>
# # Age: <age>
# # Marks: <marks>
# # Constraints
# # 1 ≤ age ≤ 100
# # 0 ≤ marks ≤ 100

# # The name contains only alphabetic characters.

# # Sample Input
# # Aditya
# # 25
# # 85
# # Sample Output
# # Name: Aditya
# # Age: 25
# # Marks: 85

# class students:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks


#     def display(self):
#         print("name:",self.name)
#         print("age:",self.age)
#         print("marks:",self.marks)


# name=input()
# age=int(input())
# marks=int(input())
# students=students(name,age,marks)
# students.display()            

# # Question 2 — Bank Account
# # Problem Statement

# # A bank wants to create a simple account management system.

# # Create a class called BankAccount that stores the account holder's name and current balance.

# # The class must provide the following methods:

# # deposit(amount) — adds the given amount to the balance.
# # withdraw(amount) — subtracts the given amount if sufficient balance is available.
# # display_balance() — displays the current balance.

# # If the withdrawal amount is greater than the available balance, the withdrawal should not be performed and the program should print:

# # Insufficient Balance
# # Input Format

# # The first line contains the account holder's name.

# # The second line contains the initial balance.

# # The third line contains the amount to deposit.

# # The fourth line contains the amount to withdraw.

# # Output Format

# # After the deposit and withdrawal operations, print:

# # Balance: <balance>

# # If the withdrawal cannot be performed, print:

# # Insufficient Balance

# # followed by the current balance.

# # Sample Input
# # Aditya
# # 10000
# # 5000
# # 3000
# # Sample Output
# # Balance: 12000

# class BankAccount:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount

#     def withdraw(self,amount):
#         if amount> self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance-=amount

#     def display_balance(self):
#         print("Banlance:",self.balance)


# name=input()
# balance=int(input())
# deposit_amount=int(input())
# withdraw_amount=int(input())
# account=BankAccount(name,balance)
# account.deposit(deposit_amount)
# account.withdraw(withdraw_amount)
# account.display_balance() 
# # 
# # 
# # 
                       
# # Question 3 — Employee Salary Calculator
# # Problem Statement

# # Create an Employee class that stores the employee's name and basic salary.

# # The company provides the following benefits:

# # HRA = 20% of basic salary
# # DA = 10% of basic salary
# # Bonus = 5% of basic salary

# # Create a method calculate_salary() that calculates the employee's final salary:

# # Final Salary = Basic Salary + HRA + DA + Bonus

# # Create another method display() that prints the employee's name and final salary.

# # Input Format

# # The first line contains the employee's name.

# # The second line contains the basic salary as a floating-point number.

# # Output Format

# # Print:

# # Employee: <name>
# # Final Salary: <salary>

# # Display the salary rounded to 2 decimal places.

# # Sample Input
# # Aditya
# # 60000
# # Sample Output
# # Employee: Aditya
# # Final Salary: 81000.00

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary

#     def calculate_salary(self):
#         hra=self.salary*0.2
#         da=self.salary*10
#         bonus=self.salary*0.05
#         return self.salary+hra+da+bonus
#     def display(self):
#         final_salary=self.calculate_salary()
#         print("employee:", self.name)
#         print(f"final salary: {final_salary:,2f}")

# name=input()
# salary=float(input())
# employee=Employee(name,salary)
# employee.display()  

# # Question 4 — School Information
# # Problem Statement

# # A school wants to store the name of the school for every student.

# # Create a Student class with:

# # name
# # age

# # The school name should be common to all students.

# # Initially, the school name is:

# # VCTI

# # Create a class method change_school() that changes the school name.

# # The program will create two students, display their information, change the school name, and display their information again.

# # Sample Input
# # Aditya
# # 25
# # Rahul
# # 23
# # ABC School
# # Sample Output
# # Aditya 25 VCTI
# # Rahul 23 VCTI
# # Aditya 25 ABC School
# # Rahul 23 ABC School



# class Student:

#     school = "VCTI"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def change_school(cls, new_school):
#         cls.school = new_school

#     def display(self):
#         print(self.name, self.age, self.school)


# name1 = input()
# age1 = int(input())

# name2 = input()
# age2 = int(input())

# new_school = input()

# student1 = Student(name1, age1)
# student2 = Student(name2, age2)

# student1.display()
# student2.display()

# Student.change_school(new_school)

# student1.display()
# student2.display()


# # Question 5 — Secure Bank Account
# # Problem Statement

# # A bank wants to protect the account balance from direct modification.

# # Create a BankAccount class with:

# # account holder name
# # private balance

# # The class should provide:

# # deposit(amount)
# # withdraw(amount)
# # get_balance()

# # The balance must not be directly accessible outside the class.

# # A withdrawal should only happen if enough balance exists.

# # Sample Input
# # Aditya
# # 10000
# # 5000
# # 3000
# # Sample Output
# # Balance: 12000

# class BankAccount:

#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient Balance")

#     def get_balance(self):
#         return self.__balance


# name = input()
# balance = int(input())
# deposit_amount = int(input())
# withdraw_amount = int(input())

# account = BankAccount(name, balance)

# account.deposit(deposit_amount)
# account.withdraw(withdraw_amount)

# print("Balance:", account.get_balance())


# # Question 6 — Vehicle Inheritance
# # Problem Statement

# # Create a base class Vehicle containing:

# # brand
# # speed

# # Create a child class Car that inherits from Vehicle.

# # The Car class should contain an additional attribute:

# # doors

# # Create a method display() in Car that displays all information.

# # Sample Input
# # Toyota
# # 180
# # 4
# # Sample Output
# # Brand: Toyota
# # Speed: 180
# # Doors: 4


# class vehicle:
#     def __init__(self,brand,speed):
#         self.brand=brand
#         self.speed=speed
# class car(vehicle):
#     def __init__(self,brand,speed,doors):
#         super().__init__(brand,speed)
#         self.doors=doors

#     def display(self):
#         print("Brand:",self.brand)
#         print("speed:",self.speed)
#         print("doors:",self.doors)

# brand=input()
# speed=int(input())
# doors=int(input())
# car=car(brand,speed,doors)
# car.dosplay()            




# # Question 7 — Method Overriding
# # Problem Statement

# # Create a base class Animal with a method sound() that prints:

# # Animal makes a sound

# # Create two child classes:

# # Dog
# # Cat

# # Both classes should override the sound() method.

# # Dog should print:

# # Dog says Bark

# # Cat should print:

# # Cat says Meow
# # Sample Input
# # Dog
# # Sample Output
# # Dog says Bark


# class Animal:

#     def sound(self):
#         print("Animal makes a sound")


# class Dog(Animal):

#     def sound(self):
#         print("Dog says Bark")


# class Cat(Animal):

#     def sound(self):
#         print("Cat says Meow")


# animal_type = input()

# if animal_type == "Dog":
#     animal = Dog()
# else:
#     animal = Cat()

# animal.sound()



# # Question 8 — Employee Roles
# # Problem Statement

# # A company has different types of employees.

# # Create a base class Employee containing a method:

# # work()

# # Create two child classes:

# # Developer
# # Tester

# # The developer should print:

# # Developer writes code

# # The tester should print:

# # Tester tests software

# # The program should create a list containing different employee objects and call work() for every employee.

# # Sample Input
# # Developer
# # Tester
# # Developer
# # Tester
# # Sample Output
# # Developer writes code
# # Tester tests software
# # Developer writes code
# # Tester tests software



# class Employee:

#     def work(self):
#         print("Employee works")


# class Developer(Employee):

#     def work(self):
#         print("Developer writes code")


# class Tester(Employee):

#     def work(self):
#         print("Tester tests software")


# employees = []

# for _ in range(4):
#     role = input()

#     if role == "Developer":
#         employees.append(Developer())
#     else:
#         employees.append(Tester())


# for employee in employees:
#     employee.work()


# #     Question 9 — Payment System
# # Problem Statement

# # Create an abstract class Payment.

# # It must contain an abstract method:

# # pay(amount)

# # Create two classes:

# # UPIPayment
# # CardPayment

# # UPIPayment should print:

# # Paid <amount> using UPI

# # CardPayment should print:

# # Paid <amount> using Card

# # The program should create the appropriate object based on the payment method and call pay().

# # Sample Input
# # UPI
# # 5000
# # Sample Output
# # Paid 5000 using UPI


# from abc import ABC, abstractmethod


# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass


# class UPIPayment(Payment):

#     def pay(self, amount):
#         print(f"Paid {amount} using UPI")


# class CardPayment(Payment):

#     def pay(self, amount):
#         print(f"Paid {amount} using Card")


# method = input()
# amount = int(input())

# if method == "UPI":
#     payment = UPIPayment()
# else:
#     payment = CardPayment()

# payment.pay(amount)


# # Question 10 — Multiple Inheritance
# # Problem Statement

# # A SmartPhone has two capabilities:

# # Camera
# # MusicPlayer

# # Create two classes:

# # Camera
# # MusicPlayer

# # Each class should have one method.

# # Create a SmartPhone class that inherits from both classes.

# # Sample Input
# # Sample Output
# # Taking Photo
# # Playing Music



# class Camera:

#     def take_photo(self):
#         print("Taking Photo")


# class MusicPlayer:

#     def play_music(self):
#         print("Playing Music")


# class SmartPhone(Camera, MusicPlayer):
#     pass


# phone = SmartPhone()

# phone.take_photo()
# phone.play_music()


# # Question 11 — Duck Typing
# # Problem Statement

# # In Python, different objects can be treated in the same way if they provide the required method. This concept is known as duck typing.

# # Create two classes:

# # Dog
# # Person

# # Both classes must have a method called speak().

# # The Dog class should print:

# # Dog says: Woof

# # The Person class should print:

# # Person says: Hello

# # Create a function make_speak(obj) that calls the speak() method of the object passed to it.

# # The function should work with both Dog and Person objects without checking their class.

# # Input Format

# # The first line contains either:

# # Dog

# # or

# # Person

# # The second line contains another choice.

# # Sample Input
# # Dog
# # Person
# # Sample Output
# # Dog says: Woof
# # Person says: Hello


# class Engine:

#     def start(self):
#         print("Engine Started")


# class Car:

#     def __init__(self, brand):
#         self.brand = brand
#         self.engine = Engine()

#     def start_car(self):
#         print("Brand:", self.brand)
#         self.engine.start()
#         print("Car Started")


# brand = input()

# car = Car(brand)

# car.start_car()


# # Question 13 — Magic Method __str__()
# # Problem Statement

# # Create a Book class that stores:

# # title
# # author
# # price

# # Normally, printing an object gives a default object representation.

# # Override the __str__() magic method so that printing the object produces:

# # Title: <title>, Author: <author>, Price: <price>
# # Input Format

# # The first line contains the book title.

# # The second line contains the author's name.

# # The third line contains the price.

# # Sample Input
# # Python Basics
# # Aditya
# # 499
# # Sample Output
# # Title: Python Basics, Author: Aditya, Price: 499


# class Book:

#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"


# title = input()
# author = input()
# price = int(input())

# book = Book(title, author, price)

# print(book)


# # Question 15 — Static Method: Temperature Converter
# # Problem Statement

# # Create a class Temperature containing two static methods:

# # celsius_to_fahrenheit(celsius)
# # fahrenheit_to_celsius(fahrenheit)

# # Use the following formulas:

# # F = (C × 9/5) + 32

# # and

# # C = (F - 32) × 5/9

# # Since these methods don't require any object-specific or class-specific data, implement them as @staticmethod.

# # Input Format

# # The first line contains a temperature in Celsius.

# # The second line contains a temperature in Fahrenheit.

# # Output Format

# # Print:

# # Fahrenheit: <value>
# # Celsius: <value>

# # Round both results to 2 decimal places.

# # Sample Input
# # 100
# # 212
# # Sample Output
# # Fahrenheit: 212.00
# # Celsius: 100.00


# class Temperature:

#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return (celsius * 9 / 5) + 32

#     @staticmethod
#     def fahrenheit_to_celsius(fahrenheit):
#         return (fahrenheit - 32) * 5 / 9


# celsius = float(input())
# fahrenheit = float(input())

# f_result = Temperature.celsius_to_fahrenheit(celsius)
# c_result = Temperature.fahrenheit_to_celsius(fahrenheit)

# print(f"Fahrenheit: {f_result:.2f}")
# print(f"Celsius: {c_result:.2f}")


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        hra = self.salary * 0.20
        da = self.salary * 0.10
        bonus = self.salary * 0.05

        return self.salary + hra + da + bonus

    def display(self):
        final_salary = self.calculate_salary()

        print("Employee:", self.name)
        print(f"Final Salary: {final_salary:.2f}")


name = input()
salary = float(input())

employee = Employee(name, salary)

employee.display()