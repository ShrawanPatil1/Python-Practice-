#elif statements


#1. Student Grade Analyzer
#A school wants to automatically classify students according to their marks. Accept the student's marks
#out of 100 and write a Python program using if-elif-else to display "Grade A+" when the marks are
#90 or above, "Grade A" when the marks are between 80 and 89, "Grade B" when the marks are
#between 70 and 79, "Grade C" when the marks are between 60 and 69, "Grade D" when the marks are
#between 40 and 59, and "Fail" when the marks are below 40.
'''
marks = int(input("Enter the Marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")
'''
#2. ATM Withdrawal Category
#An ATM wants to categorize a customer's withdrawal amount. Accept the withdrawal amount and write a
#Python program to display "Small Withdrawal" when the amount is ₹5,000 or less, "Medium
#Withdrawal" when the amount is between ₹5,001 and ₹20,000, "Large Withdrawal" when the
#amount is between ₹20,001 and ₹40,000, and "Daily Limit Exceeded" when the amount is greater
#than ₹40,000.
'''
amount = int(input("Enter the Withdrawal Amount: "))

if amount <= 5000:
    print("Small Withdrawal")
elif amount <= 20000:
    print("Medium Withdrawal")
elif amount <= 40000:
    print("Large Withdrawal")
else:
    print("Daily Limit Exceeded")
'''
#3. Mobile Battery Status
#A smartphone application wants to classify the current battery condition. Accept the battery percentage
#and display "Excellent Battery" when the battery is 80% or above, "Good Battery" when it is
#between 50% and 79%, "Low Battery" when it is between 20% and 49%, "Critical Battery" when
#it is between 1% and 19%, and "Battery Empty" when the battery level is exactly 0%.
'''
battery = int(input("Enter the Battery Percentage: "))

if battery >= 80:
    print("Excellent Battery")
elif battery >= 50:
    print("Good Battery")
elif battery >= 20:
    print("Low Battery")
elif battery >= 1:
    print("Critical Battery")
else:
    print("Battery Empty")
'''
#4. Temperature Classification
#An automatic weather monitoring system receives the current temperature in Celsius. Accept the
#temperature and display "Extreme Heat" when it is above 40°C, "Very Hot" when it is between 31°C
#and 40°C, "Warm"when it is between 21°C and 30°C, "Cool" when it is between 11°C and 20°C, "Cold"
#when it is between 0°C and 10°C, and "Freezing" when the temperature is below 0°C.
'''
temp = int(input("Enter the Temperature: "))

if temp > 40:
    print("Extreme Heat")
elif temp >= 31:
    print("Very Hot")
elif temp >= 21:
    print("Warm")
elif temp >= 11:
    print("Cool")
elif temp >= 0:
    print("Cold")
else:
    print("Freezing")
'''
#5. Movie Ticket Category
#A cinema wants to automatically determine the appropriate ticket category based on age. Accept the
#customer's age and display "Free Entry" when the age is below 5, "Child Ticket" when the age is
#between 5 and 12, "Teen Ticket" when the age is between 13 and 17, "Adult Ticket" when the age
#is between 18 and 59, and "Senior Citizen Ticket" when the age is 60 or above.
'''
age = int(input("Enter the Age: "))

if age < 5:
    print("Free Entry")
elif age <= 12:
    print("Child Ticket")
elif age <= 17:
    print("Teen Ticket")
elif age <= 59:
    print("Adult Ticket")
else:
    print("Senior Citizen Ticket")
'''
#6. Salary Category
#A company wants to classify employees according to their monthly salary. Accept the salary and display
#"Entry Level" when the salary is below ₹25,000, "Junior Level" when it is between ₹25,000 and
#₹49,999, "Mid Level" when it is between ₹50,000 and ₹74,999, "Senior Level" when it is between
#₹75,000 and ₹99,999, and "Executive Level" when the salary is ₹1,00,000 or above.
'''
salary = int(input("Enter the Salary: "))

if salary < 25000:
    print("Entry Level")
elif salary <= 49999:
    print("Junior Level")
elif salary <= 74999:
    print("Mid Level")
elif salary <= 99999:
    print("Senior Level")
else:
    print("Executive Level")
'''
#7. Internet Speed Classification
#An internet service provider wants to classify the speed of a customer's connection. Accept the internet
#speed in Mbps and display "Very Slow" when the speed is below 10 Mbps, "Slow" when it is between
#10 and 49 Mbps, "Good" when it is between 50 and 99 Mbps, "Fast" when it is between 100 and 499
#Mbps, and "Ultra Fast" when it is 500 Mbps or above.
'''
speed = int(input("Enter the Internet Speed: "))

if speed < 10:
    print("Very Slow")
elif speed <= 49:
    print("Slow")
elif speed <= 99:
    print("Good")
elif speed <= 499:
    print("Fast")
else:
    print("Ultra Fast")
''' 
#8. Shopping Cart Classification
#An online shopping website wants to categorize customers according to their cart value. Accept the cart
#value and display "Small Cart" when it is below ₹1,000, "Regular Cart" when it is between ₹1,000
#and ₹4,999, "Large Cart" when it is between ₹5,000 and ₹9,999, "Premium Cart" when it is between
#₹10,000 and ₹19,999, and "Luxury Cart" when it is ₹20,000 or above.
'''
cart = int(input("Enter the Cart Value: "))

if cart < 1000:
    print("Small Cart")
elif cart <= 4999:
    print("Regular Cart")
elif cart <= 9999:
    print("Large Cart")
elif cart <= 19999:
    print("Premium Cart")
else:
    print("Luxury Cart")
'''
#9. Exam Performance
#A college wants to classify students according to their examination percentage. Accept the percentage
#and display "Outstanding" when it is 90 or above, "Excellent" when it is between 75 and 89, "Good"
#when it is between 60 and 74, "Average" when it is between 40 and 59, and "Poor" when it is below 40.
'''
percentage = int(input("Enter the Percentage: "))

if percentage >= 90:
    print("Outstanding")
elif percentage >= 75:
    print("Excellent")
elif percentage >= 60:
    print("Good")
elif percentage >= 40:
    print("Average")
else:
    print("Poor")
'''
#10. Fuel Level
#A vehicle monitoring system wants to classify the fuel level of a car. Accept the fuel percentage and
#display "Full" when the fuel is between 75% and 100%, "Half Tank" when it is between 50% and
#74%, "Fuel Getting Low" when it is between 25% and 49%, "Refuel Soon" when it is between 10%
#and 24%, and "Critical Fuel" when it is below 10%.
'''
fuel = int(input("Enter the Fuel Percentage: "))

if fuel >= 75:
    print("Full")
elif fuel >= 50:
    print("Half Tank")
elif fuel >= 25:
    print("Fuel Getting Low")
elif fuel >= 10:
    print("Refuel Soon")
else:
    print("Critical Fuel")
'''
#11. Electricity Bill Classification
#An electricity company wants to calculate and classify a customer's electricity bill based on units
#consumed. Accept the number of units and calculate the bill using ₹5 per unit when consumption is up
#to 100 units, ₹7 per unit when consumption is between 101 and 300 units, ₹10 per unit when
#consumption is between 301 and 500 units, and ₹15 per unit when consumption is above 500 units.
#Display the total bill and classify the usage as "Low Usage", "Moderate Usage", "High Usage", or
#"Very High Usage" according to the applicable range.
'''
units = int(input("Enter the Units Consumed: "))

if units <= 100:
    bill = units * 5
    print("Low Usage")
elif units <= 300:
    bill = units * 7
    print("Moderate Usage")
elif units <= 500:
    bill = units * 10
    print("High Usage")
else:
    bill = units * 15
    print("Very High Usage")

print(f"The Total Bill is: ₹{bill}")
'''
#12. Employee Bonus
#A company gives different bonuses depending on an employee's salary. Accept the monthly salary and
#calculate a bonus of 15% when the salary is below ₹30,000, 10% when it is between ₹30,000 and
#₹50,000, 7% when it is between ₹50,001 and ₹80,000, and 5% when it is above ₹80,000. Display the
#calculated bonus amount.
'''
salary = int(input("Enter the Monthly Salary: "))

if salary < 30000:
    bonus = salary * 0.15
elif salary <= 50000:
    bonus = salary * 0.10
elif salary <= 80000:
    bonus = salary * 0.07
else:
    bonus = salary * 0.05

print(f"The Bonus Amount is: ₹{bonus}")
'''
#13. Shopping Discount
#An online shopping website provides discounts according to purchase amount. Accept the purchase
#amount and apply no discount when it is below ₹2,000, a 5% discount when it is between ₹2,000 and
#₹4,999, a 10% discount when it is between ₹5,000 and ₹9,999, a 15% discount when it is between
#₹10,000 and ₹19,999, and a 20% discount when it is ₹20,000 or above. Display the final payable amount.
'''
amount = int(input("Enter the Purchase Amount: "))

if amount < 2000:
    discount = 0
elif amount <= 4999:
    discount = amount * 0.05
elif amount <= 9999:
    discount = amount * 0.10
elif amount <= 19999:
    discount = amount * 0.15
else:
    discount = amount * 0.20

final_amount = amount - discount

print(f"The Final Payable Amount is: ₹{final_amount}")
'''
#14. Restaurant Service Charge
#A restaurant calculates service charges based on the customer's bill. Accept the bill amount and apply
#no service charge when the bill is below ₹1,000, a 5% service charge when the bill is between ₹1,000 and
#₹2,999, an 8% service charge when the bill is between ₹3,000 and ₹4,999, and a 10% service charge
#when the bill is ₹5,000 or above. Display the final bill after adding the service charge.
'''
bill = int(input("Enter the Bill Amount: "))

if bill < 1000:
    charge = 0
elif bill <= 2999:
    charge = bill * 0.05
elif bill <= 4999:
    charge = bill * 0.08
else:
    charge = bill * 0.10

final_bill = bill + charge

print(f"The Final Bill is: ₹{final_bill}")
'''
#15. Courier Charges
#A courier company charges customers according to package weight. Accept the package weight and
#charge ₹100 when the weight is up to 2 kg, ₹200 when it is above 2 kg and up to 5 kg, ₹400 when it is
#above 5 kg and up to 10 kg, ₹700 when it is above 10 kg and up to 20 kg, and ₹1,200 when it is above 20
#kg. Display the applicable courier charge.
'''
weight = int(input("Enter the Package Weight: "))

if weight <= 2:
    charge = 100
elif weight <= 5:
    charge = 200
elif weight <= 10:
    charge = 400
elif weight <= 20:
    charge = 700
else:
    charge = 1200

print(f"The Courier Charge is: ₹{charge}")
'''
#16. Mobile Recharge Bonus
#A mobile company provides different bonus amounts depending on recharge value. Accept the recharge
#amount and add no bonus when the recharge is below ₹199, ₹50 bonus when it is between ₹199 and
#₹499, ₹150 bonus when it is between ₹500 and ₹999, ₹300 bonus when it is between ₹1,000 and ₹1,999,
#and ₹500 bonus when it is ₹2,000 or above. Display the total amount credited to the customer's account.
'''
amount = int(input("Enter the Recharge Amount: "))

if amount < 199:
    bonus = 0
elif amount <= 499:
    bonus = 50
elif amount <= 999:
    bonus = 150
elif amount <= 1999:
    bonus = 300
else:
    bonus = 500

total = amount + bonus

print(f"The Total Amount Credited is: ₹{total}")
'''
#17. Loan Interest Calculation
#A bank provides different interest rates according to loan amount. Accept the loan amount and calculate
#interest at 12% when the loan is below ₹1,00,000, 10% when it is between ₹1,00,000 and ₹4,99,999, 8%
#when it is between ₹5,00,000 and ₹9,99,999, and 7% when it is ₹10,00,000 or above. Display the
#calculated interest amount.
'''
loan = int(input("Enter the Loan Amount: "))

if loan < 100000:
    interest = loan * 0.12
elif loan <= 499999:
    interest = loan * 0.10
elif loan <= 999999:
    interest = loan * 0.08
else:
    interest = loan * 0.07

print(f"The Interest Amount is: ₹{interest}")
'''
#18. Employee Overtime Payment
#A company pays employees different overtime rates according to the number of overtime hours worked.
#Accept overtime hours and calculate payment at ₹300 per hour when overtime is up to 5 hours, ₹400 per
#hour when overtime is between 6 and 10 hours, ₹500 per hour when overtime is between 11 and 20
#hours, and ₹700 per hour when overtime is above 20 hours. Display the total overtime payment.
'''
hours = int(input("Enter the Overtime Hours: "))

if hours <= 5:
    payment = hours * 300
elif hours <= 10:
    payment = hours * 400
elif hours <= 20:
    payment = hours * 500
else:
    payment = hours * 700

print(f"The Total Overtime Payment is: ₹{payment}")
'''
#19. Flight Baggage Fee
#An airline allows passengers to carry up to 15 kg of baggage for free. Accept baggage weight and display
#"Free Baggage" when the weight is 15 kg or less, "₹1,000 Fee" when it is between 16 and 20 kg,
#"₹2,000 Fee" when it is between 21 and 25 kg, "₹4,000 Fee" when it is between 26 and 30 kg, and
#"Baggage Not Allowed" when it is above 30 kg.
'''
weight = int(input("Enter the Baggage Weight: "))

if weight <= 15:
    print("Free Baggage")
elif weight <= 20:
    print("₹1,000 Fee")
elif weight <= 25:
    print("₹2,000 Fee")
elif weight <= 30:
    print("₹4,000 Fee")
else:
    print("Baggage Not Allowed")
'''
#20. Electricity Consumption Reward
#An electricity-saving program wants to classify customers according to their monthly consumption.
#Accept the number of units and display "Excellent Saving" when consumption is below 100 units,
#"Good Saving" when it is between 100 and 199 units, "Normal Usage" when it is between 200 and 299
#units, "High Consumption" when it is between 300 and 499 units, and "Excessive Consumption"
#when it is 500 units or above.
'''
units = int(input("Enter the Units: "))

if units < 100:
    print("Excellent Saving")
elif units <= 199:
    print("Good Saving")
elif units <= 299:
    print("Normal Usage")
elif units <= 499:
    print("High Consumption")
else:
    print("Excessive Consumption")
'''
#21. Student Result
#A college wants to determine a student's final result using theory and practical marks. Accept both
#marks. If either mark is below 35, display "Fail". If both marks are at least 35 and the average is 75 or
#above, display "Distinction". If the average is between 60 and 74, display "First Division". If the
#average is between 50 and 59, display "Second Division". Otherwise, display "Pass".
'''
theory = int(input("Enter the Theory Marks: "))
practical = int(input("Enter the Practical Marks: "))

average = (theory + practical) / 2

if theory < 35 or practical < 35:
    print("Fail")
elif average >= 75:
    print("Distinction")
elif average >= 60:
    print("First Division")
elif average >= 50:
    print("Second Division")
else:
    print("Pass")
'''
#22. Loan Risk Classification
#A bank wants to classify loan applicants based on salary and credit score. Accept salary and credit
#score. Display "High Risk" when salary is below ₹30,000, "High Risk" when salary is sufficient but
#the credit score is below 600, "Medium Risk" when the credit score is between 600 and 699, "Low
#Risk" when the credit score is between 700 and 749, and "Very Low Risk" when the credit score is
#750 or above.
'''
salary = int(input("Enter the Salary: "))
credit = int(input("Enter the Credit Score: "))

if salary < 30000:
    print("High Risk")
elif credit < 600:
    print("High Risk")
elif credit <= 699:
    print("Medium Risk")
elif credit <= 749:
    print("Low Risk")
else:
    print("Very Low Risk")
'''
#23. Employee Promotion
#A company wants to classify employees according to experience and performance rating. Accept years
#of experience and performance rating. Display "Not Eligible" when experience is below 1 year,
#"Junior Employee" when experience is between 1 and 2 years, "Needs Improvement" when
#experience is between 3 and 5 years but rating is below 7, "Promotion Consideration" when
#experience is between 3 and 5 years and rating is 7 or above, and "Strong Promotion Candidate"
#when experience is above 5 years and rating is 8 or above.
'''
experience = int(input("Enter the Years of Experience: "))
rating = int(input("Enter the Performance Rating: "))

if experience < 1:
    print("Not Eligible")
elif experience <= 2:
    print("Junior Employee")
elif experience <= 5 and rating < 7:
    print("Needs Improvement")
elif experience <= 5 and rating >= 7:
    print("Promotion Consideration")
elif experience > 5 and rating >= 8:
    print("Strong Promotion Candidate")
'''
#24. ATM Transaction Category
#An ATM wants to categorize withdrawal requests. Accept the withdrawal amount and display "Mini
#Withdrawal" when the amount is ₹2,000 or less, "Regular Withdrawal" when it is between ₹2,001
#and ₹10,000, "Large Withdrawal" when it is between ₹10,001 and ₹20,000, "Maximum Withdrawal"
#when it is between ₹20,001 and ₹40,000, and "Transaction Declined" when it exceeds ₹40,000.
'''
amount = int(input("Enter the Withdrawal Amount: "))

if amount <= 2000:
    print("Mini Withdrawal")
elif amount <= 10000:
    print("Regular Withdrawal")
elif amount <= 20000:
    print("Large Withdrawal")
elif amount <= 40000:
    print("Maximum Withdrawal")
else:
    print("Transaction Declined")
'''
#25. Student Scholarship
#A university awards scholarships according to marks and attendance. Accept marks and attendance.
#Display "Not Eligible" when marks are below 60. Display "Basic Scholarship" when marks are
#between 60 and 74. Display "Scholarship Denied - Attendance" when marks are between 75 and
#89 but attendance is below 75%. Display "Good Scholarship" when marks are between 75 and 89 and
#attendance is at least 75%. Display "Full Scholarship" when marks are 90 or above and attendance
#is at least 90%.
'''
marks = int(input("Enter the Marks: "))
attendance = int(input("Enter the Attendance: "))

if marks < 60:
    print("Not Eligible")
elif marks <= 74:
    print("Basic Scholarship")
elif marks <= 89 and attendance < 75:
    print("Scholarship Denied - Attendance")
elif marks <= 89 and attendance >= 75:
    print("Good Scholarship")
elif marks >= 90 and attendance >= 90:
    print("Full Scholarship")
'''
#26. Insurance Premium
#An insurance company determines premium category according to age. Accept age and display "Not
#Eligible" when age is below 18, "₹5,000 Premium" when age is between 18 and 30, "₹7,500
#Premium" when age is between 31 and 45, "₹10,000 Premium" when age is between 46 and 60, and
#"₹15,000 Premium" when age is above 60.
'''
age = int(input("Enter the Age: "))

if age < 18:
    print("Not Eligible")
elif age <= 30:
    print("₹5,000 Premium")
elif age <= 45:
    print("₹7,500 Premium")
elif age <= 60:
    print("₹10,000 Premium")
else:
    print("₹15,000 Premium")
'''
#27. Bank Account Category
#A bank wants to recommend an account type based on monthly income. Accept monthly income and
#display "Basic Account" below ₹20,000, "Standard Account" between ₹20,000 and ₹49,999,
#"Premium Account" between ₹50,000 and ₹99,999, "Platinum Account" between ₹1,00,000 and
#₹1,99,999, and "Elite Account" when income is ₹2,00,000 or above.
'''
income = int(input("Enter the Monthly Income: "))

if income < 20000:
    print("Basic Account")
elif income <= 49999:
    print("Standard Account")
elif income <= 99999:
    print("Premium Account")
elif income <= 199999:
    print("Platinum Account")
else:
    print("Elite Account")
'''
#28. Hotel Room Category
#A hotel wants to recommend a room according to the customer's budget. Accept the budget and display
#"Economy" below ₹2,000, "Standard" between ₹2,000 and ₹4,999, "Deluxe" between ₹5,000 and
#₹9,999, "Executive" between ₹10,000 and ₹19,999, and "Luxury Suite" when the budget is ₹20,000
#or above.
'''
budget = int(input("Enter the Budget: "))

if budget < 2000:
    print("Economy")
elif budget <= 4999:
    print("Standard")
elif budget <= 9999:
    print("Deluxe")
elif budget <= 19999:
    print("Executive")
else:
    print("Luxury Suite")
'''
#29. Gaming Rank
#A video game wants to assign a rank based on the player's score. Accept the score and display
#"Beginner" below 500, "Bronze" between 500 and 999, "Silver" between 1,000 and 1,999, "Gold"
#between 2,000 and 4,999, "Platinum" between 5,000 and 9,999, and "Diamond" at 10,000 or above.
'''
score = int(input("Enter the Score: "))

if score < 500:
    print("Beginner")
elif score <= 999:
    print("Bronze")
elif score <= 1999:
    print("Silver")
elif score <= 4999:
    print("Gold")
elif score <= 9999:
    print("Platinum")
else:
    print("Diamond")
'''
#30. Delivery Priority
#An online shopping company determines delivery priority based on order value and delivery distance.
#Accept order value and distance. Display "Normal" when the order is below ₹1,000, "Priority" when
#the order is at least ₹1,000 and distance is below 10 km, "Express" when the order is at least ₹1,000
#and distance is between 10 and 20 km, and "Special Handling" when the order is at least ₹1,000 and
#distance is above 20 km.
'''
order = int(input("Enter the Order Value: "))
distance = int(input("Enter the Delivery Distance: "))

if order < 1000:
    print("Normal")
elif distance < 10:
    print("Priority")
elif distance <= 20:
    print("Express")
else:
    print("Special Handling")
'''
#31. Salary After Increment
#A company wants to calculate an employee's new salary based on the current salary. Accept the current
#salary. If the salary is below ₹30,000, increase it by 20%; if it is between ₹30,000 and ₹49,999, increase it
#by 15%; if it is between ₹50,000 and ₹79,999, increase it by 10%; and if it is ₹80,000 or above, increase it
#by 5%. After calculating the new salary, display "Low Salary" if it is below ₹40,000, "Moderate
#Salary" if it is between ₹40,000 and ₹59,999, "Good Salary" if it is between ₹60,000 and ₹99,999, and
#"High Salary" if it is ₹1,00,000 or above.
'''
salary = int(input("Enter the Current Salary: "))

if salary < 30000:
    salary += salary * 0.20
elif salary <= 49999:
    salary += salary * 0.15
elif salary <= 79999:
    salary += salary * 0.10
else:
    salary += salary * 0.05

print(f"The New Salary is: ₹{salary}")

if salary < 40000:
    print("Low Salary")
elif salary <= 59999:
    print("Moderate Salary")
elif salary <= 99999:
    print("Good Salary")
else:
    print("High Salary")
'''
#32. Shopping Discount After Coupon
#An online store gives discounts based on the original cart value. Accept the cart value and apply a 5%
#discount below ₹5,000, 10% between ₹5,000 and ₹9,999, and 20% at ₹10,000 or above. After calculating
#the final price, display "Budget Purchase" when it is below ₹4,000, "Regular Purchase" when it is
#between ₹4,000 and ₹7,999, "Premium Purchase" when it is between ₹8,000 and ₹14,999, and
#"Luxury Purchase" when it is ₹15,000 or above.
'''
cart = int(input("Enter the Cart Value: "))

if cart < 5000:
    discount = cart * 0.05
elif cart <= 9999:
    discount = cart * 0.10
else:
    discount = cart * 0.20

final_price = cart - discount

print(f"The Final Price is: ₹{final_price}")

if final_price < 4000:
    print("Budget Purchase")
elif final_price <= 7999:
    print("Regular Purchase")
elif final_price <= 14999:
    print("Premium Purchase")
else:
    print("Luxury Purchase")
'''
#33. Student Marks After Grace
#A school gives grace marks to students based on their original marks. Accept the marks and add 5 grace
#marks when the marks are below 33, add 3 grace marks when marks are between 33 and 39, and add no
#grace marks when marks are 40 or above. After calculating the final marks, display "Fail" below 40,
#"Pass" between 40 and 59, "First Class" between 60 and 74, "Distinction" between 75 and 89,
#and "Outstanding" at 90 or above.
'''
marks = int(input("Enter the Marks: "))

if marks < 33:
    marks += 5
elif marks <= 39:
    marks += 3

print(f"The Final Marks are: {marks}")

if marks < 40:
    print("Fail")
elif marks <= 59:
    print("Pass")
elif marks <= 74:
    print("First Class")
elif marks <= 89:
    print("Distinction")
else:
    print("Outstanding")
'''
#34. Fuel After Consumption
#A car initially has 100 litres of fuel. Accept the amount of fuel consumed. If consumption is below 20
#litres, consume the actual amount; if it is between 20 and 50 litres, consume 20 litres; and if it is above
#50 litres, consume 50 litres. After calculating the remaining fuel, display "Critical" when it is below 20
#litres, "Low" when it is between 20 and 39 litres, "Moderate" when it is between 40 and 69 litres, and
#"High" when it is 70 litres or above.
'''
fuel = 100
consume = int(input("Enter the Fuel Consumed: "))

if consume < 20:
    fuel -= consume
elif consume <= 50:
    fuel -= 20
else:
    fuel -= 50

print(f"The Remaining Fuel is: {fuel} Litres")

if fuel < 20:
    print("Critical")
elif fuel <= 39:
    print("Low")
elif fuel <= 69:
    print("Moderate")
else:
    print("High")
'''
#35. Bank Balance After Withdrawal
#A customer has a certain bank balance and wants to withdraw money. Accept the balance and
#withdrawal amount. If the withdrawal amount is greater than the balance, display "Insufficient
#Balance". Otherwise, calculate the remaining balance and display "Critical" when it is below
#₹1,000, "Low" when it is between ₹1,000 and ₹4,999, "Safe" when it is between ₹5,000 and ₹19,999,
#and "Healthy" when it is ₹20,000 or above.
'''
balance = int(input("Enter the Bank Balance: "))
withdraw = int(input("Enter the Withdrawal Amount: "))

if withdraw > balance:
    print("Insufficient Balance")
else:
    balance -= withdraw

    if balance < 1000:
        print("Critical")
    elif balance <= 4999:
        print("Low")
    elif balance <= 19999:
        print("Safe")
    else:
        print("Healthy")
'''
#36. Mobile Battery After Usage
#A mobile phone application wants to estimate remaining battery after usage. Accept the current battery
#percentage and number of hours used. Reduce the battery by 5% when usage is below 2 hours, 15%
#when usage is between 2 and 5 hours, 25% when usage is between 6 and 8 hours, and 40% when usage
#is above 8 hours. After calculating the remaining battery, display "Dead Soon" for 10% or below,
#"Critical" for 11–30%, "Low" for 31–60%, and "Healthy" for 61% or above.
'''
battery = int(input("Enter the Current Battery Percentage: "))
hours = int(input("Enter the Hours Used: "))

if hours < 2:
    battery -= 5
elif hours <= 5:
    battery -= 15
elif hours <= 8:
    battery -= 25
else:
    battery -= 40

print(f"The Remaining Battery is: {battery}%")

if battery <= 10:
    print("Dead Soon")
elif battery <= 30:
    print("Critical")
elif battery <= 60:
    print("Low")
else:
    print("Healthy")
'''
#37. Electricity Bill Classification
#An electricity company calculates a customer's bill based on units consumed. Accept the units and
#calculate the bill using ₹5 per unit up to 100 units, ₹7 per unit from 101 to 300 units, ₹10 per unit from
#301 to 500 units, and ₹15 per unit above 500 units. After calculating the bill, display "Low Bill" below
#₹1,000, "Moderate Bill" from ₹1,000 to ₹2,999, "High Bill" from ₹3,000 to ₹4,999, and "Very
#High Bill" when the bill is ₹5,000 or above.
'''
units = int(input("Enter the Units Consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
elif units <= 500:
    bill = units * 10
else:
    bill = units * 15

print(f"The Bill is: ₹{bill}")

if bill < 1000:
    print("Low Bill")
elif bill <= 2999:
    print("Moderate Bill")
elif bill <= 4999:
    print("High Bill")
else:
    print("Very High Bill")
'''
#38. Exam Result With Average
#A college wants to classify students based on marks in three subjects. Accept the three marks and
#calculate the average. If any subject mark is below 35, display "Fail". Otherwise, display "Pass" when#
#the average is below 50, "Second Division" when it is between 50 and 59, "First Division" when
#it is between 60 and 74, "Distinction" when it is between 75 and 89, and "Outstanding" when it is
#90 or above.
'''
mark1 = int(input("Enter Subject 1 Marks: "))
mark2 = int(input("Enter Subject 2 Marks: "))
mark3 = int(input("Enter Subject 3 Marks: "))

average = (mark1 + mark2 + mark3) / 3

print(f"The Average is: {average}")

if mark1 < 35 or mark2 < 35 or mark3 < 35:
    print("Fail")
elif average < 50:
    print("Pass")
elif average <= 59:
    print("Second Division")
elif average <= 74:
    print("First Division")
elif average <= 89:
    print("Distinction")
else:
    print("Outstanding")
'''
#39. Loan Eligibility
#A bank wants to classify loan applicants according to salary and disposable income. Accept salary and
#monthly expenses and calculate disposable income by subtracting expenses from salary. Display "Not
#Eligible" when salary is below ₹30,000, "High Risk" when disposable income is below ₹10,000,
#"Medium Risk" when disposable income is between ₹10,000 and ₹19,999, "Low Risk" when it is
#between ₹20,000 and ₹39,999, and "Excellent Eligibility" when disposable income is ₹40,000 or
#above.
'''
salary = int(input("Enter the Salary: "))
expenses = int(input("Enter the Monthly Expenses: "))

income = salary - expenses

if salary < 30000:
    print("Not Eligible")
elif income < 10000:
    print("High Risk")
elif income <= 19999:
    print("Medium Risk")
elif income <= 39999:
    print("Low Risk")
else:
    print("Excellent Eligibility")
'''
#40. Employee Performance Score
#A company calculates an employee's performance score using attendance, performance rating, and
#experience. Accept all three values and calculate the score using performance_rating × 5 +
#attendance/10 + experience × 2. Display "Poor" when the score is below 100, "Average" when it
#is between 100 and 119, "Good" when it is between 120 and 139, "Excellent" when it is between 140
#and 159, and "Outstanding" when it is 160 or above.
'''
attendance = int(input("Enter the Attendance: "))
rating = int(input("Enter the Performance Rating: "))
experience = int(input("Enter the Experience: "))

score = rating * 5 + attendance / 10 + experience * 2

print(f"The Performance Score is: {score}")

if score < 100:
    print("Poor")
elif score <= 119:
    print("Average")
elif score <= 139:
    print("Good")
elif score <= 159:
    print("Excellent")
else:
    print("Outstanding")
'''
#41. Restaurant Final Bill
#A restaurant wants to calculate the final bill based on the bill amount and number of people. Accept both
#values and calculate the per-person amount. Display "Budget Meal" when the per-person amount is
#below ₹500, "Regular Meal" when it is between ₹500 and ₹999, "Premium Meal" when it is between
#₹1,000 and ₹1,999, and "Luxury Meal" when it is ₹2,000 or above. After classification, apply a 5%
#discount when the original bill is below ₹2,000, 10% when it is between ₹2,000 and ₹4,999, and 15%
#when it is ₹5,000 or above, and display the final bill.
'''
bill = int(input("Enter the Total Bill: "))
people = int(input("Enter the Number of People: "))

person = bill / people

if person < 500:
    print("Budget Meal")
elif person <= 999:
    print("Regular Meal")
elif person <= 1999:
    print("Premium Meal")
else:
    print("Luxury Meal")

if bill < 2000:
    discount = bill * 0.05
elif bill <= 4999:
    discount = bill * 0.10
else:
    discount = bill * 0.15

final_bill = bill - discount

print(f"The Final Bill is: ₹{final_bill}")
'''
#42. Employee Final Salary
#A company wants to calculate an employee's final salary according to performance rating. Accept basic
#salary and performance rating. Give no increment when rating is below 5, a 5% increment when rating is
#between 5 and 6, a 10% increment when rating is between 7 and 8, and a 20% increment when rating is
#between 9 and 10. After calculating the final salary, display "Low Income" below ₹30,000, "Moderate
#Income" between ₹30,000 and ₹49,999, "Good Income" between ₹50,000 and ₹79,999, and "High
#Income" at ₹80,000 or above.
'''
salary = int(input("Enter the Basic Salary: "))
rating = int(input("Enter the Performance Rating: "))

if rating < 5:
    salary += 0
elif rating <= 6:
    salary += salary * 0.05
elif rating <= 8:
    salary += salary * 0.10
else:
    salary += salary * 0.20

print(f"The Final Salary is: ₹{salary}")

if salary < 30000:
    print("Low Income")
elif salary <= 49999:
    print("Moderate Income")
elif salary <= 79999:
    print("Good Income")
else:
    print("High Income")
'''
#43. Cricket Player Classification
#A cricket application wants to classify a player's performance based on runs and strike rate. Accept both
#values. Display "Low Scorer" when runs are below 50, "Average Performer" when runs are between
'''
runs = int(input("Enter the Runs: "))
strike = int(input("Enter the Strike Rate: "))

if runs < 50:
    print("Low Scorer")
elif runs <= 99 and strike < 100:
    print("Average Performer")
elif runs <= 99 and strike >= 100:
    print("Aggressive Performer")
elif runs >= 100 and strike < 120:
    print("Centurion")
else:
    print("Match Winner")
'''
#50 and 99 and strike rate is below 100, "Aggressive Performer" when runs are between 50 and 99
#and strike rate is 100 or above, "Centurion" when runs are 100 or above and strike rate is below 120,
#and "Match Winner" when runs are 100 or above and strike rate is 120 or above.



#44. Student Final Classification
#A college wants to classify students using marks, attendance, and projects completed. Accept all three
#values. Display "Fail" when marks are below 40, "Pass" when marks are between 40 and 59, "Pass
#With Attendance Warning" when marks are between 60 and 74 but attendance is below 75%,
#"First Class" when marks are between 60 and 74 and attendance is at least 75%, "Distinction
#But Project Incomplete" when marks are between 75 and 89 but projects are below 3,
#"Distinction" when marks are between 75 and 89 and projects are at least 3, and "Outstanding"
#when marks are 90 or above.
'''
marks = int(input("Enter the Marks: "))
attendance = int(input("Enter the Attendance: "))
projects = int(input("Enter the Projects Completed: "))

if marks < 40:
    print("Fail")
elif marks <= 59:
    print("Pass")
elif marks <= 74 and attendance < 75:
    print("Pass With Attendance Warning")
elif marks <= 74 and attendance >= 75:
    print("First Class")
elif marks <= 89 and projects < 3:
    print("Distinction But Project Incomplete")
elif marks <= 89 and projects >= 3:
    print("Distinction")
else:
    print("Outstanding")
'''
#45. Online Shopping Final Status
#An e-commerce company wants to determine the type of order based on cart value, membership, and
#delivery distance. Accept all three values. Display "Small Order" when the cart value is below ₹1,000,
#"Regular Order" when the cart is ₹1,000 or above and the customer has Basic membership,
#"Priority Order" when the customer has Premium membership and the delivery distance is below 10
#km, "Express Order" when the Premium customer's distance is between 10 and 25 km, and "Special
#Delivery" when the Premium customer's distance is above 25 km.
'''
cart = int(input("Enter the Cart Value: "))
membership = input("Enter the Membership: ")
distance = int(input("Enter the Delivery Distance: "))

if cart < 1000:
    print("Small Order")
elif membership == "Basic":
    print("Regular Order")
elif membership == "Premium" and distance < 10:
    print("Priority Order")
elif membership == "Premium" and distance <= 25:
    print("Express Order")
else:
    print("Special Delivery")
'''
#46. Hospital Billing Category
#A hospital calculates a patient's consultation fee based on age and emergency status. Accept age,
#consultation fee, and emergency status. Apply a 30% discount for emergency patients aged 60 or above,
#20% for emergency patients below 60, 15% for non-emergency patients aged 60 or above, and 5% for all
#other patients. After calculating the final fee, display "Low Fee" below ₹500, "Standard Fee" between
#₹500 and ₹999, "Premium Fee" between ₹1,000 and ₹1,999, and "High Fee" when the fee is ₹2,000 or
#above.
'''
age = int(input("Enter the Age: "))
fee = int(input("Enter the Consultation Fee: "))
emergency = input("Enter Emergency Status Yes or No: ")

if emergency == "Yes" and age >= 60:
    discount = fee * 0.30
elif emergency == "Yes":
    discount = fee * 0.20
elif emergency == "No" and age >= 60:
    discount = fee * 0.15
else:
    discount = fee * 0.05

fee -= discount

print(f"The Final Fee is: ₹{fee}")

if fee < 500:
    print("Low Fee")
elif fee <= 999:
    print("Standard Fee")
elif fee <= 1999:
    print("Premium Fee")
else:
    print("High Fee")
'''
#47. ATM Risk Classification
#An ATM wants to classify the risk level of a withdrawal. Accept the account balance and withdrawal
#amount. If the withdrawal amount is greater than the account balance, display "Transaction
#Declined". Otherwise, calculate the remaining balance and display "Critical Withdrawal" when
#the remaining balance is below ₹1,000, "High Risk" when it is between ₹1,000 and ₹4,999, "Safe"
#when it is between ₹5,000 and ₹19,999, and "Very Safe" when it is ₹20,000 or above.
'''
balance = int(input("Enter the Account Balance: "))
withdraw = int(input("Enter the Withdrawal Amount: "))

if withdraw > balance:
    print("Transaction Declined")
else:
    balance -= withdraw

    if balance < 1000:
        print("Critical Withdrawal")
    elif balance <= 4999:
        print("High Risk")
    elif balance <= 19999:
        print("Safe")
    else:
        print("Very Safe")
'''
#48. Electricity Consumption Analysis
#An electricity company wants to analyze a customer's current bill compared with the previous bill.
#Accept units consumed and previous bill amount. Calculate the current bill using ₹5 per unit up to 100
#units, ₹7 per unit for 101–300 units, ₹10 per unit for 301–500 units, and ₹15 per unit above 500 units.
#Display "Low Consumption" when the current bill is below ₹1,000, "Consumption Increased" when
#the current bill is between ₹1,000 and ₹2,999 and is greater than the previous bill, "Consumption
#Stable"when the current bill is between ₹1,000 and ₹2,999 and is equal to or less than the previous bill,
#"High Consumption" when the bill is between ₹3,000 and ₹4,999, and "Excessive Consumption"
#when the bill is ₹5,000 or above.
'''
units = int(input("Enter the Units Consumed: "))
previous = int(input("Enter the Previous Bill Amount: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = units * 7
elif units <= 500:
    bill = units * 10
else:
    bill = units * 15

print(f"The Current Bill is: ₹{bill}")

if bill < 1000:
    print("Low Consumption")
elif bill <= 2999 and bill > previous:
    print("Consumption Increased")
elif bill <= 2999 and bill <= previous:
    print("Consumption Stable")
elif bill <= 4999:
    print("High Consumption")
else:
    print("Excessive Consumption")
'''
#49. Student Scholarship Challenge
#A university wants to determine a student's scholarship category based on marks, attendance, family
#income, and projects completed. Accept all four values. Display "No Scholarship" when marks are
#below 60, "Basic Scholarship" when marks are between 60 and 74, "Scholarship Denied -
#Attendance" when marks are between 75 and 89 but attendance is below 75%, "Partial
#Scholarship" when marks are between 75 and 89, attendance is at least 75%, but family income is
#above ₹5,00,000, "Good Scholarship" when marks are between 75 and 89, attendance is at least
#75%, and family income is ₹5,00,000 or below, "Full Scholarship" when marks are 90 or above,
#attendance is at least 90%, projects are at least 3, and family income is ₹3,00,000 or below, and
#"Special Review Required" in all remaining cases.
'''
marks = int(input("Enter the Marks: "))
attendance = int(input("Enter the Attendance: "))
income = int(input("Enter the Family Income: "))
projects = int(input("Enter the Projects Completed: "))

if marks < 60:
    print("No Scholarship")
elif marks <= 74:
    print("Basic Scholarship")
elif marks <= 89 and attendance < 75:
    print("Scholarship Denied - Attendance")
elif marks <= 89 and attendance >= 75 and income > 500000:
    print("Partial Scholarship")
elif marks <= 89 and attendance >= 75 and income <= 500000:
    print("Good Scholarship")
elif marks >= 90 and attendance >= 90 and projects >= 3 and income <= 300000:
    print("Full Scholarship")
else:
    print("Special Review Required")
'''
#50. Employee Career Classification
#A company wants to automatically classify an employee's career status. Accept the employee's current
#salary, years of experience, performance rating, and attendance percentage. Calculate a performance
#score using performance_rating × 10 + attendance/10 + experience. Then use if-elif-else
#to display "Entry Level Employee" when salary is below ₹30,000, "Not Ready For Promotion"
#when the salary is at least ₹30,000 but the performance score is below 80, "Needs Improvement" when
#the score is between 80 and 99, "Promotion Consideration" when the score is between 100 and 119,
#"Promotion Recommended" when the score is between 120 and 139, and "Fast Track Candidate"
#when the score is 140 or above.
'''
salary = int(input("Enter the Current Salary: "))
experience = int(input("Enter the Years of Experience: "))
rating = int(input("Enter the Performance Rating: "))
attendance = int(input("Enter the Attendance Percentage: "))

score = rating * 10 + attendance / 10 + experience

print(f"The Performance Score is: {score}")

if salary < 30000:
    print("Entry Level Employee")
elif score < 80:
    print("Not Ready For Promotion")
elif score <= 99:
    print("Needs Improvement")
elif score <= 119:
    print("Promotion Consideration")
elif score <= 139:
    print("Promotion Recommended")
else:
    print("Fast Track Candidate")
'''
