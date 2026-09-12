#wap to find the product of digits of a number
'''
number = int(input("Enter a number : "))
product_of_digits = 1

while number != 0:
    digit = number % 10
    product_of_digits *= digit
    number //= 10
print(product_of_digits)
'''
#number programs

#wap to check wherther the number is prime or not
'''
number = int(input("Enter a number : "))
number_of_factors, i = 0, 1

while i <= number:
    if number % i == 0:
        number_of_factors += 1
    i += 1
if number_of_factors == 2:

    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
'''

#wap to check whether the number is palindrome or not
'''
number = int(input("Enter a number: "))
t_number = number
reverse = 0

while t_number != 0:
    digit = t_number % 10
    reverse = reverse * 10 + digit
    t_number //= 10

if reverse == number:
    print(f"{number} is palindrome number")
else:
    print(f"{number} is not palindrome number")
'''

#wap to check whether the number is armstring number
'''
number = int(input("Enter the number:"))
number_of_digits = 0
temp_number = number

while temp_number != 0:
    number_of_digits += 1
    temp_number //= 10

temp_number_1 = number
sum_of_powers = 0

while temp_number_1 != 0:
    digit = temp_number_1 % 10
    sum_of_powers += digit ** number_of_digits
    temp_number_1 //= 10

if sum_of_powers == number:
    print(f"{number} is a armstrong number")
else:
    print(f"{number} is not an armstrong number")
'''

#wap to check whether the number is perfect or not

#inp = 6                  |   inp = 28
#out = "perfect number"   |   out = "perfect number"

number = int(input("Enter a number : "))
sum_of_factors = 0
i = 1

while i < number:
    if number % i == 0:
        sum_of_factors + = i
    i += 1

if sum_of_factors == number:
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")

'''
num = int(input("Enter a number: "))

if num <= 0:
  print("Not a perfect number")
else:
  divisor_sum = 0
  i = 1

  while i <= num // 2:
    if num % i == 0:
      divisor_sum += i
    i += 1

  if divisor_sum == num:
    print("perfect number")
  else:
    print("Not a perfect number")
'''
