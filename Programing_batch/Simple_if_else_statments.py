#Simple if else statements


#1. ATM Withdrawal with Balance Check
#An ATM has a customer's balance. Accept the balance and withdrawal amount.
#• If the withdrawal amount is less than or equal to the balance, deduct it.
#• If the remaining balance is below ₹2,000, display "Low Balance".
#• Otherwise, display "Withdrawal Successful".
'''
balance = 10000
a = int(input("Ente the Withdrawal amount: "))
if a <= balance:
    balance -= a
    print(f"The amount is less than or equal to the balance : {balance}")
if balance <= 2000:
    print("Low Balance")
else:
    print("Withdrawal Successful")
'''
#2. Electricity Bill Warning
#Accept the current electricity bill amount.
#• If the bill is greater than ₹5,000, add a ₹500 late/surcharge amount.
#• Display the final bill.
#• If the final bill is greater than ₹5,000, display "High Bill".
#• Otherwise, display "Normal Bill".
'''
bill = int(input("Enter the Current Electricity bill amount: "))

if bill >= 5000 :
    bill += 500
    print(f"Add the  ₹500 late/surcharge Total amount: {bill}")
if bill >= 5000:
    print("High Bill")
else:
    print("Normal Bill")
'''
#3. Student Marks Adjustment
#Accept marks obtained by a student.
#• If marks are below 40, add 5 grace marks.
#• Display the final marks.
#• If final marks are 40 or more, display "Pass".
#• Otherwise, display "Fail".
'''
marks = int(input("Enter the Student Total Obtained marks: "))

if marks <=40:
    marks += 5
    print(f"Added Grace marks , total marks: {marks}")
if marks >= 40:
    print("Pass")
else:
    print("Fail")
'''
#4. Shopping Wallet
#A customer has ₹5,000 in their wallet. Accept the purchase amount.
#• If the customer can afford the purchase, deduct it.
#• If the remaining balance is exactly ₹1,000, display "Exactly One Thousand Left".
#• Otherwise, display "Purchase Completed".
#If the customer cannot afford it, display "Insufficient Balance".
'''
wallet = 5000
amount = int(input("Enter the purchase total amount: "))

if amount <= 5000:
    wallet -= amount
    print("Accept the purchase")
    if wallet == 1000:
        print("Exactly One Thousand Left")
    else:
        print("Purchase Completed")
if amount >= wallet :
    print("Insufficient Balance")
'''

#5. Mobile Data Usage
#Accept a user's available mobile data in GB.
#• If available data is less than 2 GB, add 5 GB bonus data.
#• Display the updated data.
#• If the updated data is at least 5 GB, display "Data Sufficient".
#• Otherwise, display "Data Still Low".
'''
data = int (input("Enter the Your Available mobile Data in GB: "))

if data <= 2:
    data += 5
    print(f"5GB data is add, your data is : {data}")
if data >= 5:
    print("Data Sufficient")
else:
    print("Data Still Low")
'''
#6. Salary Deduction
#An employee earns ₹60,000.
#Accept the amount of deduction.
#• If the deduction is less than ₹10,000, deduct it.
#• Otherwise, deduct ₹10,000 only.
#• Display the final salary.
#• If final salary is exactly ₹50,000, display "Salary At Limit".
'''
salary = 60000
deduct = int(input("Enter the Amount of Deduction: "))

if deduct <= 10000:
    salary_f = salary - deduct
    #print(f"Salary Dedected by 10000, Total Salary: {salary_f}")
else:
    salary_f = salary - 10000


print(f"Salary Dedected by 10000, Total Salary: {salary_f}")
if salary_f == 50000:
    print("Salary At Limit")
'''
#7. Online Order Discount
#Accept the shopping cart value.
#• If the cart value is ₹10,000 or more, give a 10% discount.
#• Otherwise, give no discount.
#• Display the final payable amount.
#• If the final amount is below ₹9,000, display "Major Saving".
'''
amount = int(input("Enter the Shoping cart value: "))

if amount >= 10000:
    a = amount * 0.10
    print(f"You got 10% discount ")
else:
    print("no discount")

print(f"total amount to Pay: {a}")
if a < 9000:
    print("Major Saving")
'''
#8. Exam Marks and Grace
#Accept a student's marks.
#• If marks are between 35 and 39, add 5 grace marks.
#• Otherwise, leave the marks unchanged.
#• Display the final marks.
#• If final marks are 40 or more, display "Pass".
#• Otherwise, display "Fail".
'''
marks = int(input("Enter the student marks: "))

if marks >=35 and marks <= 39:
    total = marks + 5
    print(" add the grace marks")
else:
    total = marks
    print("marks are not change")
print(f"The final Marks: {total}")
if total >= 40:
    print("Pass")
else:
    print("Fail")
'''

#9. Fuel Tank Calculation
#A car has 60 litres of fuel.
#Accept fuel consumed.
#• If fuel consumed is less than or equal to the available fuel, deduct it.
#• If remaining fuel is below 15 litres, display "Refuel Soon".
#• Otherwise, display "Fuel Sufficient".
'''
fuel = 60
consumed = int(input("Enter the car fuel Consumed in Liters: "))

if consumed <= 60:
    fuel -= consumed
    #print("fuel is Dedeucted")
if fuel <= 15:
    print("Refuel Soon")
else:
    print("Fuel Sufficient")
'''
#10. Restaurant Bill
#Accept the restaurant bill.
#• If the bill is above ₹2,000, give a ₹300 discount.
#• Otherwise, give no discount.
#• Display the final bill.
#• If the final bill is exactly ₹1,700, display "Special Saving".
'''
bill = int(input("Enter the Total Restaurant Bill:₹"))

if bill >= 2000:
    bill -= 300
    print("You got a ₹300 discount")
else:
    print("Ther is no Discount")
print(f"The final bill is : ₹{bill}")
if bill == 1700 :
    print("Special Saving")
'''
#11. Employee Attendance
#Accept attendance percentage.
#• If attendance is below 75%, add 5 attendance points as an approved adjustment.
#• Display the adjusted attendance.
#• If adjusted attendance is at least 75%, display "Exam Eligible".
#• Otherwise, display "Exam Not Allowed".
'''
a = int(input("Enter the Attendence Percentage: "))

if a <= 75:
    a += 5
print(f"The Adjusted Attendance is: {a}")

if a >= 75:
    print("Exam Eligible")
else:
    print("Exam Not Allowed")
'''
#12. Bank Minimum Balance
#Accept account balance.
#• If balance is below ₹5,000, deduct ₹200 as a maintenance charge.
#• Otherwise, make no deduction.
#• Display the final balance.
#• If final balance is below ₹1,000, display "Critical Balance".
'''
balance = int(input("Enter the Account Balance: "))

if balance <= 5000:
    b = balance - 200
else:
    b = balance
print(f"The final Balance is:{b} ")
if b < 1000:
    print("Critical Balance")
'''
#13. Movie Ticket Pricing
#Accept customer's age and ticket price.
#• If the customer is 60 or older, give a 20% discount.
#• Otherwise, no discount.
#• Display the final ticket price.
#• If the final price is exactly ₹240, display "Discounted Ticket".
'''
age = int(input("Enter the AGE :"))
p = int(input("Enter the Ticket Price: "))

if age >=60:
    price = p * 0.20
    price = p - price 
    #print("You got 20% Discount")
else:
    price = price
print(f"The final ticket price is: {price}")
if price == 240:
    print("Discounted Ticket")
'''
#14. Salary Bonus Trap
#Accept employee salary.
#• If salary is greater than ₹50,000, add a 10% bonus.
#• Otherwise, add ₹2,000.
#• Display the final salary.
#• If final salary exceeds ₹60,000, display "High Earnings".
'''
salary = int (input("Enter the Employee Salary: "))

if salary > 50000:
    total_salary = salary +(salary * 0.10)
else:
    total_salary = salary + 2000
print(f"The final Salary is : {total_salary}")
if total_salary > 60000:
      print("High Earnings")
'''
#15. ATM PIN and Withdrawal
#Accept PIN and withdrawal amount.
#• If PIN is 4321, continue checking the withdrawal.
#• If withdrawal is ₹20,000 or less, display "Transaction Approved".
#• Otherwise, display "Withdrawal Limit Exceeded".
#• If PIN is incorrect, display "Wrong PIN".
#1
'''
pin = int(input("Enter the 4 digit PIN: "))

if pin == 4321:
    w = (int(input("Enter the Withdrawanl Amount:")))
    if w <= 20000:
        print("Transaction Approved")
    else:
        print("Withdrawal Limit Exceeded")
else:
    print("Wrong PIN")
'''
#2
'''
pin = int(input("Enter the 4 digit PIN: "))
w = (int(input("Enter the Withdrawanl Amount:")))

if pin == 4321 and w <= 20000:
    print("Transaction Approved")
else:
    print("Withdrawal Limit Exceeded and chek pin")
'''

#16. Package Delivery
#Accept package weight.
#• If weight is greater than 10 kg, add ₹500 delivery charge.
#• Otherwise, add ₹200.
#• Display the delivery charge.
#• If the charge is ₹500, display "Heavy Package".
'''
weight = int(input("Enter the Package Weight: "))

if weight > 10:
    a = 500
    weight += a
else:
    a = 200
    weight += a
print(f"The Delivey Charge is : {a}")
if a == 500:
    print("Heavy Package")
'''

#17. Gaming Health
#A player has 100 health points.
#Accept damage caused by an enemy.
#• If damage is greater than 30, subtract 40 health.
#• Otherwise, subtract 20 health.
#• Display remaining health.
#• If health falls below 50, display "Danger".
#• Otherwise, display "Safe".
'''
health = 100
damage = int(input("Enter the Damage coude by an enemy persent: "))

if damage > 30 :
    health -= 40
else:
    health -= 20
print(f"The Remaining Health: {health}")
if health < 50:
    print("Danger")
else:
    print("Safe")
'''

#18. Relationship Points
#A person starts with 100 relationship points.
#Accept whether the person replied late using 1 for Yes and 0 for No.
#• If the reply was late, deduct 30 points.
#• Otherwise, deduct 5 points.
#• Display remaining points.
#• If points are exactly 70, display "Still Safe".
'''
points = 100
a = int(input("Enter the person replied late status by using 1 for Yes and 0 for No:"))

if a ==1 :
    points -= 30
else :
    points -= 5
print(f"The remining Points Are: {points}")
if points == 70:
    print("Still Safe")
'''

#19. School Pocket Money
#A student has ₹1,000.
#Accept the amount spent.
#• If spending is greater than ₹700, add a warning message.
#• Deduct the amount only if it can be afforded.
#• Display the remaining money.
#• If exactly ₹300 remains, display "Budget Limit Reached".
'''
student = 1000
amount = int(input("Enter the Spent Total Amount:"))

if amount > 700:
    print("Warning: Your are spending more than 700rupe")

if amount <= student:
    student -= amount
print(f"The Remaining Mony is : {student}")
if student == 300:
    print("Budget Limit Reached")
'''
#20. Internet Recharge
#Accept recharge amount.
#• If recharge is ₹500 or more, add ₹100 bonus.
#• Otherwise, add ₹20 bonus.
#• Display total credited amount.
#• If total credited amount is exactly ₹600, display "Premium Recharge".
'''
amount = int(input("Enter the Recharge amount:"))

if amount >= 500:
    amount +=  100
else:
    amount += 20
print(f"The total Credited amount Is: {amount}")
if amount == 600:
    print("Premium Recharge")
'''
#21. Temperature Warning
#Accept room temperature.
#• If temperature is above 35°C, increase the cooling level by 2.
#• Otherwise, increase it by 1.
#• Display the cooling level.
#• If cooling level becomes 3 or more, display "Strong Cooling Required".
'''
temp = int(input("Enter the room Temperature in °C:"))
level = 1

if temp >35:
    level += 2
else:
    level += 1
print(f"The cooling level is : {level}")
if level >= 3:
    print("Strong Cooling Required")
'''
#22. Library Book Return
#Accept number of late days.
#• If late days are greater than 7, calculate a fine of ₹10 per day.
#• Otherwise, fine is ₹0.
#• Display the fine.
#• If fine is exactly ₹100, display "Moderate Fine".
'''
number = int(input("Enter the Library Book Taken days: "))
fine = 0

if number > 7:
    fine = number * 10

print(f"The fine is: {fine}")
if fine == 100:
    print("Moderate Fine")
'''
#23. Credit Card Limit
#A customer has a credit limit of ₹50,000.
#Accept purchase amount.
#• If purchase is affordable, deduct it from available credit.
#• Otherwise, display "Transaction Declined".
#• If remaining credit is below ₹10,000, display "Credit Almost Exhausted".
#• Otherwise, display "Credit Available".
'''
credit = 50000
amount = int(input("Enter the Purchase Amount:"))

if amount <= credit:
    credit -= amount
    pritn(f"Remining Credit: {credit}")
    
    if credit < 10000:
        print("Credit Almost Exhausted")
    else:
        print("Credit Available")
else:
    print("Transaction Declined")
'''
#24. Salary and Loan Eligibility
#Accept salary and existing EMI.
#• If salary is greater than ₹50,000, calculate remaining income after EMI.
#• Otherwise, display "Salary Too Low".
#• If remaining income is ₹30,000 or more, display "Loan Condition Satisfied".
#• Otherwise, display "Loan Risky".
'''
salary = int(input("Enter the Salary amount:"))
emi = int(input("Enter the EMI amount: "))
income = 0

if salary > 50000:
    income = salary - emi
    print(f"The Remining income after Emi : {income}")
else:
    print("Salary Too Low")

if income >= 30000:
    print("Lone condition Satisfied")
else:
    print("Lone Risky")
'''
#25. Shopping Cart Quantity
#Accept number of items and total cart value.
#• If quantity is at least 5, give ₹500 discount.
#• Otherwise, give ₹100 discount.
#• Display final amount.
#• If final amount becomes exactly ₹4,500, display "Special Cart".
'''
items = int(input("Enter the Numbers of Items: "))
cart = int(input("Enter the total cart value:"))

if items >= 5:
    cart -= 500
    print("You got 500 discount")
else:
    cart -= 100
    print("You got 100 discount")
    
print(f"The final amount is : {cart}")

if cart == 4500:
    print("Special Cart")
'''
#26. Mobile Battery Charging
#Accept current battery percentage.
#• If battery is below 30%, add 20% charging.
#• Otherwise, add 10%.
#• Battery cannot exceed 100%.
#• Display final battery percentage.
#• If battery reaches exactly 100%, display "Fully Charged".
'''
percent = int(input("Enter the current Battety Percentage: "))

if percent < 30:
    percent += 20
else:
    percent += 10
if percent > 100:
    percent = 100
print(f"The final Battery Percentage: {percent}")

if percent == 100:
    print("Fully Charge")
'''
#27. Exam Result with Grace
#Accept marks.
#• If marks are between 33 and 39, add 5 grace marks.
#• Otherwise, do not add grace.
#• Display final marks.
#• If final marks are exactly 40, display "Just Passed".
#• Otherwise, display "Result Processed".
'''
marks = int(input("Enter the Marks: "))

if marks > 33 and marks < 39:
    marks += 5
    print("Grace marks added")
print(f"The final marks is: {marks}")

if marks == 40:
    print("Just Padded")
else:
    print("Result Processed")
'''
#28. Bus Pass Renewal
#Accept current balance and renewal fee.
#• If balance is enough, deduct the fee.
#• If remaining balance is below ₹100, display "Recharge Required".
#• Otherwise, display "Pass Renewed".
#• If balance is insufficient, display "Renewal Failed".
'''
balance = int(input("Enter the Current Balance:"))
fee = int(input("Enter the Renewal Fee:"))

if balance >= fee:
    balance -= fee
    print("Fee Deducted")
    
    if balance < 100:
        print("Rechanrge Required")
    else:
        print("Pass Renewed")
if balance < fee:
    print("Renewal Failed")
'''
#29. Food Delivery
#Accept order amount and delivery distance.
#• If order amount is at least ₹1,000, delivery is free.
#• Otherwise, charge ₹50.
#• Display final payable amount.
#• If delivery distance is greater than 10 km, add another ₹100.
#• Display the final amount again.



#30. Employee Performance Bonus
#Accept performance score out of 100.
#• If score is at least 80, give ₹10,000 bonus.
#• Otherwise, give ₹3,000.
#• Display the bonus.
#• If bonus is ₹10,000, display "Excellent Performance".
'''
score = int(input("Enter the Performance Score:"))
bonus = 0

if score >= 80:
    bonus = 10000
else:
    bonus = 3000
print(f"The Bonus is : {bonus}")

if bonus == 10000:
    print("Excellent Performance")
'''

#31. ATM Daily Limit
#Accept today's withdrawal amount and amount already withdrawn today.
#The daily limit is ₹40,000.
#• If the new withdrawal keeps the total within ₹40,000, approve it.
#• Otherwise, reject it.
#• If exactly ₹40,000 has been withdrawn after the transaction, display "Daily Limit Reached".
'''
w_1 = int(input("Enter the withdrawal amount:"))
w_2 = int(input("Enter the Privious Withdrawal amount:"))
limit = 40000

if w_2 + w_1 <= 40000:
    print("Approve the Transaction")
else:
    print("Rejected")
if w_2 + w_1 == 40000:
    print("Daily Limit Reached")
'''
#32. Hotel Room Booking
#Accept room price and customer membership status.
#• If the customer is "Premium", give a 20% discount.
#• Otherwise, give a 5% discount.
#• Display final room price.
#• If final price is below ₹4,000, display "Budget Booking".
'''
room = int(input("Enter the room Price:"))
membership = str(input("Enter the Membership Status 'Premium' or 'Not': "))

if membership == "Premium":
    discount = room * 0.20
else:
    discount = room * 0.05

final = room - discount
print(f"The final room price is : {final}")

if discount < 4000:
    print("Budget Booking")
'''
#33. Cricket Score Challenge
#Accept runs scored and wickets lost.
#• If runs are at least 100, add 10 bonus runs.
#• Otherwise, add 5 bonus runs.
#• Display final score.
#• If wickets lost are 8 or more, display "Dangerous Position".
'''
run = int(input("Enter the runs Scored: "))
wickets = int(input("Enter the Wickets lost count: "))

if run >= 100:
    run += 10
else:
    run += 5
print(f"The final score is: {run}")

if wickets >= 8:
    print("Dangerous Position")
'''
#34. Student Scholarship
#Accept marks and family income.
#• If marks are at least 85, check family income.
#• If income is ₹3,00,000 or less, display "Scholarship Approved".
#• Otherwise, display "Income Too High".
#• If marks are below 85, display "Marks Requirement Not Met".
'''
marks = int(input("Enter the marks: "))
income = int(input("Enter the Income: "))

if marks >= 85:
    print("Check the income")
if income <= 300000:
    print("Scholarship Approved")
else:
    print("Income Too High")
if marks < 85:
    print("Marks Requirement Not Met")
'''
#35. Courier Insurance
#Accept package value.
#• If package value is above ₹50,000, insurance is compulsory.
#• Otherwise, insurance is optional.
#• If insurance is compulsory, add ₹1,000 insurance fee.
#• Display total amount.
'''
value = int(input("Enter the package value:"))

if value > 50000:
    print("Insurance is compulsory")
else:
    print("Insurance is Optional")

if value > 50000:
    value += 1000
print(f"The total amount is : {value}")
'''
#36. Electricity Consumption
#Accept previous meter reading and current meter reading.
#• Calculate units consumed.
#• If units consumed are above 500, add a ₹1,000 surcharge.
#• Otherwise, no surcharge.
#• Display units consumed and final surcharge.
#• If units consumed are exactly 500, display "Usage At Limit".
'''
previous = int(input("Enter the Previous meter Reading: "))
current = int(input("Enter the current meter Reading: "))

units = current - previous
if units > 500:
    sur = 1000
else:
    sur = 0
print(f"The units consumed is : {units} and Final Surcharge is {sur}")
if units == 500 :
    print("Usage At Limit")
'''
#37. Restaurant Table Bill
#Accept number of people and total bill.
#• If there are at least 5 people, give 10% discount.
#• Otherwise, give 5% discount.
#• Display final bill.
#• If final bill is below ₹2,000, display "Affordable Dinner".
'''
people = int(input("Enter the Total numbe of peoples:"))
bill = int(input("Enter the Total bill:"))

if people >= 5:
    total = bill * 0.10
    bill -= total
    print("You got 10% Discount")
else:
    total = bill * 0.05
    bill -= total
    print("You got 5% Discount")
print(f"The final bill is : {bill}")

if bill < 2000:
    print("Affordable Dinner")
'''
#38. Online Exam Login
#Accept username and password.
#• If username is "admin", check the password.
#• If password is "python123", display "Login Successful".
#• Otherwise, display "Wrong Password".
#• If username is incorrect, display "Invalid Username".
'''
username = str(input("Enter the Your Username:"))
password = str(input("Enter the Password:"))

if username == "admin":
    print("Password is checking")

    if password == "python123":
        print("Login Successful")
    else:
        print("Wrong Password")

else:
    print("Invalid Username")
'''             
#39. Driving Eligibility
#Accept age and whether the person has a license.
#• If age is at least 18, check license status.
#• If license is "Yes", display "Allowed to Drive".
#• Otherwise, display "License Required".
#• If age is below 18, display "Underage".
'''
age = int(input("Enter the AGE: "))
licensee = str(input("Enter Yes or no your License Status:"))

if age >= 18:
    print("-")
    
if licensee == "Yes":
    print("Allowed to drive")
else:

    print("License Required")

if age < 18:
    print("Underage")
'''
#40. Shopping Membership
#Accept purchase amount and membership type.
#• If purchase is above ₹5,000, check membership.
#• If membership is "Gold", give 20% discount.
#• Otherwise, give 10% discount.
#• If purchase is ₹5,000 or less, give no discount.
#• Display final amount.
'''
amount = int(input("Enter the Purchase Amount:"))
membership = str(input("Enter the Membership Status 'Gold' or 'Not': "))

if amount > 5000:
    if membership == "Gold":
        a = amount * 0.20
        amount -= a
        print("You got 20% Discount")
    else:
        a = amount * 0.10
        amount -= a
        
        print("You got 10% Discount")
else:
    print("No discount")
print(f"The final Amount : {amount}")
'''
#41. Hospital Consultation
#Accept patient's age and consultation fee.
#• If age is 60 or above, give a 25% discount.
#• Otherwise, give a 10% discount.
#• Display final fee.
#• If final fee is exactly ₹750, display "Special Consultation Rate".
'''
age = int(input("Enter the patient's age :"))
fee = int(input("Enter the Consultation Fee: "))

if age >= 60:
    dis = fee * 0.25
    fee -= dis
else:
    dis = fee * 0.10
    fee -= dis

print(f"The final Fee : {fee}")

if fee == 750:
    print("Special Consultation Rate")
'''
#42. Flight Baggage
#Accept baggage weight.
#• If baggage is above 20 kg, calculate excess baggage charges at ₹500 per extra kg.
#• Otherwise, charge ₹0.
#• Display excess weight and charge.
#• If excess charge exceeds ₹5,000, display "Heavy Excess Baggage".
'''
weight = int(input("Enter the Baggage Wight: "))
charge = 500

if weight > 20:
    weight -= 20
    charge *= wight
    
else:
    charge = 0

print(f"The Excess Weight: {wight}")
print(f"The Charge is :  {charge}")

if charge > 5000:
    print("Heavy Excess Baggage")
'''
#43. Water Tank
#A water tank has a capacity of 1,000 litres.
#Accept current water level and amount of water added.
#• Add the water.
#• If total exceeds 1,000 litres, set the level to 1,000.
#• Display final water level.
#• If final level is exactly 1,000, display "Tank Full".
'''
tank = 1000
level = int(input("Enter the Current Water level :"))
added = int(input("Enter the amount of water added: "))

add = added + level

if add > tank:
    add = 1000
else:
    add
print(f"Level is: {add}")

if add == 1000:
    print("Tank Full")
'''
#44. Employee Leave Balance
#An employee has 15 leave days.
#Accept requested leave days.
#• If requested leave is available, deduct it.
#• Otherwise, display "Leave Request Denied".
#• If remaining leave is exactly 5, display "Five Leaves Remaining".
#• Otherwise, display "Leave Updated".
'''
leave = 15
a = int(input("Enter the Requested Leave Days: "))

if a <= leave:
    a = leave - a
else:
    print("Leave Request Denied")

if a == 5:
    print("Five Leaves Remaining")
else:
    print("Leave Updated")
'''
#45. Mobile Recharge Expiry
#Accept remaining validity days.
#• If validity is below 5 days, add 28 days after recharge.
#• Otherwise, add 10 days.
#• Display updated validity.
#• If updated validity is exactly 33 days, display "Long Validity".
'''
days = int(input("Enter the Remaining validity Days: "))

if days <= 5:
    days += 28
else:
    days += 10
print(f"the updated validity is : {days}")

if days == 33:
    print("Long Validity")
'''

#46. Online Wallet Security
#Accept wallet balance and transaction amount.
#• If transaction amount is greater than ₹10,000, display "OTP Required".
#• Otherwise, display "OTP Not Required".
#• If transaction can be afforded, deduct it.
#• Otherwise, display "Insufficient Wallet Balance".
#• Display the remaining balance if the transaction succeeds.
'''
balance = int(input("Enter the Wallet Balance: "))
amount = int(input("Enter the Transaction amount:"))

if amount > 10000:
    print("OTP Required")
else:
    print("OTP Not Required")

if amount <= balance :
    balance -= amount
else:
    print("Insufficient Wallet Balance:")

print(f"The Remaining Balance: {balance}") 
'''
#47. Bus Fare Calculation
#Accept passenger age and base fare.
#• If age is below 12, give 50% discount.
#• Otherwise, charge the full fare.
#• Display final fare.
#• If the final fare is exactly ₹50, display "Minimum Fare".
'''
age = int(input("Enter the Passenger age :"))
fare = int(input("Enter the Passenger base fare:"))

if age < 12:
    f = fare * 0.50
    fare -= f
else:
    fare
print(f"The Passenger Final Fare: {fare}")

if fare == 50:
    print("Minimum Fare")
'''
#48. Employee Overtime
#Accept regular working hours and overtime hours.
#• If overtime is greater than 10 hours, calculate overtime pay at ₹500 per hour.
#• Otherwise, calculate it at ₹300 per hour.
#• Display overtime pay.
#• If overtime pay is above ₹5,000, display "High Overtime".
'''
working = int(input("Enter the Regular working hours: "))
o_hours = int(input("Enter the Overtime working hours: "))

if o_hours > 10:
    overtime = 500 * o_hours
else:
    overtime = 300 * o_hours

print(f"The Overtime pay: {overtime}")

if overtime > 5000:
    print("High Overtime")
'''
#49. E-Commerce Delivery Challenge
#Accept cart value, membership type, and delivery distance.
#• If cart value is at least ₹5,000, delivery is free.
#• Otherwise, charge ₹100.
#• If distance is greater than 20 km, add ₹200 delivery charge.
#• If membership is "Premium", remove the ₹100 basic delivery charge.
#• Display the final delivery charge.
#Challenge: Carefully decide which charges should actually be applied.
'''
cart = int(input("Enter the cart value: "))
membership = str(input("Enter the Membership type: "))
distance = int(input("Enter the Delivery Distance: "))
charge = 0

if cart >= 5000:
    charge = 0
else:
    charge = 100
if distance > 20:
    charge = charge + 200

if membership == "Premium":
    charge = charge - 100

print(f"The final delivery charge is: {charge}")
'''
#50. Student Result System
#A student has:
#• Theory marks
#• Practical marks
#• Attendance percentage
#• Internal marks
#The program must:
#1. Accept all four values.
#2. If theory marks are below 35, add 5 grace marks.
#3. Otherwise, leave theory marks unchanged.
#4. If practical marks are below 35, add 5 grace marks.
#5. Calculate total marks.
#6. If attendance is below 75%, display "Attendance Shortage".
#7. Otherwise, check whether internal marks are at least 40.
#8. If internal marks are sufficient, check the final theory and practical marks.
#9. Display "PASS" only when all required conditions are satisfied.
#10.Otherwise, display "FAIL".
'''
theory = int(input("Enter the Theory Marks : "))
practical = int(input("Enter the Practical Marks : "))
attendance = int(input("Enter the Attendance Percentage : "))
internal = int(input("Enter the Internal Marks : "))

if theory < 35:
    theory = theory + 5

if practical < 35:
    practical = practical + 5

total = theory + practical

if attendance < 75:
    print("Attendance Shortage")
else:
    if internal >= 40:
        if theory >= 35 and practical >= 35:
            print("PASS")
        else:
            print("FAIL")
    else:
        print("FAIL")

print(f"Total Marks: {total}")
'''   


