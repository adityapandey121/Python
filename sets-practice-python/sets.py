# Check Membership
# Problem

# You are given a set of integers and then several numbers. For each number, determine whether it exists in the set.

# Input
# 5
# 10 20 30 40 50
# 3
# 20
# 25
# 50
# Output
# YES
# NO
# YES

# n=int(input())
# numbers=set(map(int,input().split()))
# q=int(input())
# for i in range(q):
#     x=int(input())
#     if x in numbers:
#         print("yes")
#     else:
#         print("no")    

# Unique Words
# Problem

# Given N words, find the number of distinct words.

# Input
# 7
# apple
# banana
# apple
# orange
# banana
# mango
# apple
# Output
# 4

# n=int(input())
# words=set()
# for i in range(n):
#     word=input()
#     words.add(word)
# print(len(words))    

# Add Country Stamps
# Problem

# A traveler collects country stamps. Duplicate stamps should be counted only once. Find the number of unique countries.

# Input
# 8
# India
# USA
# India
# Japan
# USA
# Germany
# Japan
# France
# Output
# 5

# n=int(input())
# countries=set()
# for i in range(n):
#     country=input()
#     countries.add(country)
# print(len(countries))

# 7. Add Multiple Numbers
# Problem

# Given an initial set and another list of numbers, add all numbers from the second list to the set. Print the final number of unique elements.

# Input
# 5
# 1 2 3 4 5
# 6
# 4 5 6 7 8 9
# Output
# 9

# n= int(input())
# A=set(map(int,input().split()))
# m=int(input())
# B=set(int, input().split())
# A.update(B)
# print(len(B))

