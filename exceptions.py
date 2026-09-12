# try:
#     #code thhat may raise an exception
# except:
#     #code to handle the exception
# else:
      #code that will run if no exception occurred
# finally:
#     #code that will run regardless of whether an exception occurred or not

# try:
#     a = int(input("Enter a number: "))
#     b = int(input("Enter another number: "))
#     result = a / b
# except ValueError:
#     print("Invalid input! Please enter valid integers.")
# except ZeroDivisionError:
#     print("Error! Division by zero is not allowed.")
# else:
#     print(f"The result is: {result:.2f}")
# finally:
#     print("Execution completed.")

#Exception Handling Exercises
# Divide Two Numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")

# Write a Python program to divide two numbers. Handle ZeroDivisionError if the user enters 0.
try: 
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    division_result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
else:
    print(f"The result of division is: {division_result}")
finally:
    print("Execution completed.")

# Integer Input
try:
    user_input = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input! Please enter a valid integer.")
else: 
    print(f"You entered the integer: {user_input}")
finally:
    print("Execution completed.")

# Take an integer input from the user. Handle ValueError if the user enters a non-numeric value.
try:
    user_input = int(input("Enter an integer: "))
except ValueError:
    print("Invalid input! Please enter a valid integer.")       
else:
    print(f"You entered the integer: {user_input}")
finally:
    print("Execution completed.")

# List Index
try:
    numbers = [10, 20, 30, 40, 50]
    index = int(input("Enter an index (0-4): "))
    print(f"The number at index {index} is: {numbers[index]}")
except IndexError:
    print("Error: Index out of range. Please enter a valid index between 0 and 4.")
else:
    print(f"You accessed the number: {numbers[index]}")
finally:
    print("Execution completed.")

# Create a list of 5 numbers and ask the user to enter an index. Handle IndexError if the index is invalid.
try:
    numbers = [10, 20, 30, 40, 50]
    index = int(input("Enter an index (0-4): "))
    print(f"The number at index {index} is: {numbers[index]}")
except IndexError:
    print("Error: Index out of range. Please enter a valid index between 0 and 4.")
else:
    print(f"You accessed the number: {numbers[index]}")
finally:
    print("Execution completed.")

# Dictionary Key
try:
    student_details = {
        "name": "John Doe",
        "age": 20,
        "major": "Computer Science"
    }
    key = input("Enter a key (name, age, major): ")
    print(f"The value for '{key}' is: {student_details[key]}")
except KeyError:
    print(f"Error: The key '{key}' does not exist in the student details.")
else:
    print(f"You accessed the value: {student_details[key]}")
finally:
    print("Execution completed.")

# Create a dictionary containing student details. Ask the user to enter a key and handle KeyError if the key does not exist.
try:
    student_details = {
        "name": "John Doe",
        "age": 20,
        "major": "Computer Science"
    }
    key = input("Enter a key (name, age, major): ")
    print(f"The value for '{key}' is: {student_details[key]}")
except KeyError:
    print(f"Error: The key '{key}' does not exist in the student details.")
else:
    print(f"You accessed the value: {student_details[key]}")
finally:
    print("Execution completed.")

# Multiple Exceptions
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid input! Please enter valid integers.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")
# Take two numbers from the user and perform division. Handle both ValueError and ZeroDivisionError.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid input! Please enter valid integers.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")

# Try-Except-Else
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid input! Please enter valid integers.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
else:
    print(f"The result is: {result}")   
finally:
    print("Execution completed.")

# Write a program to take two numbers and divide them using try, except, and else.
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
except ValueError:
    print("Invalid input! Please enter valid integers.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")    
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")

# Try-Except-Finally
try:
    num = int(input("Enter a number: "))
    square = num ** 2
except ValueError:
    print("Invalid input! Please enter a valid integer.")
else:
    print(f"The square of {num} is: {square}")
finally:
    print("Execution completed.")

# Write a program that takes a number from the user and prints its square. Use try, except, and finally.
try:
    num = int(input("Enter a number: "))
    square = num ** 2
except ValueError:
    print("Invalid input! Please enter a valid integer.")
else:
    print(f"The square of {num} is: {square}")
finally:
    print("Execution completed.")
    