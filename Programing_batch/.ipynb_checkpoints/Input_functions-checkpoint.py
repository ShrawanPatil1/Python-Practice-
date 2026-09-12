#reverse a 3 digit number

#inp = 123
#out = 321
"""
number = int(input("Enter a 3 digit number : "))
digit_3 = number % 10
digit_2 = (number // 10) % 10
digit_1 = number // 100
reverse = digit_3 * 100 + digit_2 * 10 + digit_1
print(f"The reverse of {number} is {reverse}")
"""
#wap to reverse a 4 digit number
#for output of
#out = 1234
#inp = 4321
'''
number = int(input("Enter a 4 digit number : "))
digit_4 = number % 10
digit_3 = (number // 10) % 10
digit_2 = (number // 100) % 10
digit_1 = number // 1000
reverse = digit_4 * 1000 + digit_3 * 100 + digit_2 * 10 + digit_1
print(f"The reverse of {number} is {reverse}")
'''
# WAP to find the sum of digits of a 5 digit number without using loops or string operations.
#inp = 58321
#out = 19
'''
number = int(input("Enter a 5 digit number : "))
digit_5 = number % 10
digit_4 = number % 1000
digit_3 = number % 1000
digit_2 = number % 10000
digit_1 = number % 10000
values = digit_5 + digit_4 + digit_3 + digit_2 + digit_1
print(f"the sum of 5 digit {number} is : {values}")
'''

#4. WAP to find the product of all digits of a 4 digit number.
#inp = 2345
#out = 120
'''
number = (input("Enter a 4 digit number : "))
num_1 = number[0]
num_2 = number[1]
num_3 = number[2]
num_4 = number[3]
product = num_1 * num_2 * num_3 * num_4
print(" The Product of 4 digit {number} is : {product}")
'''

#5. WAP to extract the first digit of a 5 digit number using only // and % operators.
#inp = 58321
#out = 5
'''
number = int(input("Enter a 5 digit number : "))
digit_1 = number // 10000
value = digit_1 * 1000
print(f"the first value is of {number}: id : {value}")
'''
#6. WAP to extract the last digit of a number without using the modulus (%) operator.
#inp = 58327
#out = 7
'''
number = int(input("Enter a 5 digit number : "))
digit_1 = number % 10
value = digit_1 * 1000
print(f"the first value is of {number}: id : {value}")
'''
#7. WAP to remove the first digit from a 5 digit number.
#inp = 58321
#out = 8321
'''
number = int(input("Enter a 5 digit number : "))
digit_4 = number % 10000
print(f"The first digit froma 5 digti is : {digit_4}")
'''

#8. WAP to remove the last digit from a number.
#inp = 58321
#out = 5832
'''
number = 2567
digit_1 = number // 10
print(f"The first digit froma  digti is : {digit_1}")
'''
#9. WAP to interchange the first and last digit of a 4 digit number.
#inp = 1234
#out = 4231
'''
number = int(input("Enter a 4 digit number : "))

digit_4 = number % 10
digit_2 = (number % 1000) % 10
digit_1 = number // 10000
value = digit_4 + digit_2 + digit_1
print(f"the interchange the {number} first and last dibit is : ", digit_4 , digit_2, digit_1)
'''
#10. WAP to interchange the middle two digits of a 4 digit number.
#inp = 1234
#out = 1324
'''
number = int(input("Enter a 4 digit numbers : "))
d_1 = number // 1000
d_2 = (number // 10) % 10
d_3 = (number // 100) % 10
d_4 = number % 10
print(f"numbers: ", d_1, d_2, d_3, d_4)
'''
#11. WAP to move the last digit of a 4 digit number to the first position.
#inp = 1234
#out = 4123
'''
number = int(input("Enter a 4 digit numbers : "))
d_4 = number % 10
d_1 = number // 1000
d_2 = (number // 100) % 10
d_3 = (number // 10) % 10
value = d_4 * 1000 + d_1 * 100 + d_2 * 10 + d_3
print(f"The last digit of a {number} number to the first position : {value}")
'''
#12. WAP to move the first digit of a 4 digit number to the last.
#inp = 1234
#out = 2341
'''
number = int(input("Enter a 4 digit numbers : "))
d_1 = (number // 100) % 10
d_2 = (number // 10) % 10
d_3 = number % 10
d_4 = number // 1000
value = d_1 * 1000 + d_2 * 100 + d_3 * 10 + d_4
print(f" The first digit of a {number} number to the last : {value} ")
'''
#13. WAP to find the difference between the first and last digit of a 5 digit number.
#inp = 58321
#out = 4
'''
num = int(input("Enter a 5-digit number: "))

first_digit = num // 10000
last_digit = num % 10
difference = first_digit - last_digit

print("Difference:", difference)

'''
#14. WAP to find the sum of the first and last digit of a 6 digit number.
#inp = 583217
#out = 12
'''
num = int(input("Enter a 6-digit number: "))

first_digit = num // 100000
last_digit = num % 10
total_sum = first_digit + last_digit

print("Sum:", total_sum)
'''
#15. WAP to extract the middle digit of a 5 digit number.
#inp = 58321
#out = 3
'''
num = int(input("Enter a 5-digit number: "))

middle_digit = (num // 100) % 10

print("Middle digit:", middle_digit)
'''

#16. WAP to calculate:
#(a² + b²) / (a + b)
#inp = 3, 5
#out = 4.25

a = [3, 5]

a_1 = a // 10
a_2 = a % 10

print(a_1, a_2)


#17. WAP to calculate:
#(a + b)² - (a - b)²
#inp = 7, 3
#out = 84


#18. WAP to calculate:
#a³ - b³
#inp = 5, 2
#out = 117


#19. WAP to calculate the average of 5 numbers without using sum(), loops or any other function.
#inp = 10, 20, 30, 40, 50
#out = 30.0


#20. WAP to calculate:
#(a*2 + b*3 + c*5) / 10
#inp = 10, 20, 30
#out = 23.0


#21. WAP to reverse a 4 digit number and then add the original number to its reverse.
#inp = 1234
#out = 5555


#22. WAP to reverse a 3 digit number and multiply it by the original number.
#inp = 123
#out = 15129


#23. WAP to calculate the sum of squares of all digits of a 4 digit number.
#inp = 1234
#out = 30


#24. WAP to calculate the sum of cubes of all digits of a 3 digit number.
#inp = 153
#out = 153


#25. WAP to calculate the square of a number.
#inp = 25
#out = 625


#26. WAP to calculate the cube of a number without using operator.
#inp = 7
#out = 343


#27. WAP to exchange the values of two numbers without using a third variable.
#inp:
#a = 10
#b = 20
#out:
#a = 20
#b = 10


#28. WAP to accept total seconds and convert them into:
#hours, minutes and seconds
#inp = 7384
#out = 2 hours 3 minutes 4 seconds
#Use only // and % for extraction.


#29. WAP to accept a 5 digit number and rearrange its digits as:
#5th digit + 3rd digit + 1st digit + 4th digit + 2nd digit
#inp = 12345
#out = 53142
#Use only arithmetic operators.
#No strings, loops or conditions.



#30.
#WAP to accept a 5 digit number and create the following output using ONLY arithmetic operators:
#1. Reverse of the number
#2. Sum of all digits
#3. Product of all digits
#4. Sum of squares of all digits
#5. Difference between the original number and reverse
#inp = 12345
#out =
#Reverse = 54321
#Digit Sum = 15
#Digit Product = 120
#Square Sum = 55
#Difference = -41976





























