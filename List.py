# #LIST
# a = [1, 2, 3, 4]
# b = []
# for i in a:
# b.append(a)
# print(b)

# a=[1,2,3,4,5]
# b=[]
# for i in a:
#   b.append(2*i)
#   print(b)

#LIST COMPRIANSATIONN
# a=[1,2,3,4,5]
# b = [i*2 for i in a]

# QUESTIONS

# Create a list of numbers from 1 to 10 using list comprehension.

# a =[]
# for i in range(1,11):
#     a.append(i)
# print(a)

# Create a list of squares of numbers from 1 to 10.

# a =[]
# for i in range(1,11):
#     a.append(i*i)
# print(a)

# Create a list of cubes of numbers from 1 to 5.

# a =[]
# for i in range(1,6):
#     a.append(i**3)
# print(a)

# Given numbers = [1, 2, 3, 4, 5], create a new list by multiplying each number by 2.

# a=[]
# for i in range(1,6):
#     a.append(i*2)
# print(a)

# Given numbers = [10, 20, 30, 40, 50], create a new list by adding 10 to each number.

# a = [10, 20, 30, 40, 50]
# b=[]
# for i in a:
#     b.append(10+i)
# print(b)


# Given names = ["ram", "sham", "raj"], create a new list containing all names in uppercase.

# names = ["ram", "sham", "raj"]
# a =[]
# for i in names:
#     a.append(i.upper())
# print(a)

# name = ["SHRAWAN", "LILAKANT", "PATIL"]
# a = []
# for i in name:
#     a.append(i.lower())
# print(a)


# Given numbers = [2, 4, 6, 8, 10], create a new list by dividing each number by 2.
# numbers = [2, 4, 6, 8, 10]
# a =[]
# for i in numbers:
#     a.append(i/2)
# print(a)

#
# 14-08-2026
#
# Create a list containing the squares of numbers from 1 to 10 using list comprehension.
# a = []
# for i in range(1,11):
#     a.append(i**2)
# print(a)

# Create a list containing only even numbers from 1 to 20 using list comprehension.
# num = [i for i in range(1,21) if i % 2 == 0 ]
# print(num)

# Create a list containing only odd numbers from 1 to 20 using list comprehension.
# num = [i for i in range(1,21) if i % 3==0]
# print(num)

# Given a list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a new list containing only numbers greater than 5.
# num = [i for i in range(1,11) if i >=5]
# print(num)

# Given a list of numbers, create a new list where even numbers are multiplied by 2 and odd numbers are multiplied by 3 using list comprehension.
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_odd = [i * 2 if i % 2 == 0 else i * 3 for i in num]
# print(even_odd)

# Given a list of names, create a new list containing only names whose length is greater than 5 using list comprehension.
# names = ["Shrawan", "Sam", "Priyanka", "Raj", "Sanika", "Ram"]
# a = [name for name in names if len(name) > 5]
# print(a)
