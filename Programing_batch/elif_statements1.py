#elif statements


#1. Student Grade Analyzer
#A school wants to automatically classify students according to their marks. Accept the student's marks
#out of 100 and write a Python program using if-elif-else to display "Grade A+" when the marks are
#90 or above, "Grade A" when the marks are between 80 and 89, "Grade B" when the marks are
#between 70 and 79, "Grade C" when the marks are between 60 and 69, "Grade D" when the marks are
#between 40 and 59, and "Fail" when the marks are below 40.
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

#2. ATM Withdrawal Category
#An ATM wants to categorize a customer's withdrawal amount. Accept the withdrawal amount and write a
#Python program to display "Small Withdrawal" when the amount is ₹5,000 or less, "Medium
#Withdrawal" when the amount is between ₹5,001 and ₹20,000, "Large Withdrawal" when the
#amount is between ₹20,001 and ₹40,000, and "Daily Limit Exceeded" when the amount is greater
#than ₹40,000.

amount = int(input("Enter the Withdrawal Amount: "))

if amount <= 5000:
    print("Small Withdrawal")
elif amount <= 20000:
    print("Medium Withdrawal")
elif amount <= 40000:
    print("Large Withdrawal")
else:
    print("Daily Limit Exceeded")

#3. Mobile Battery Status
#A smartphone application wants to classify the current battery condition. Accept the battery percentage
#and display "Excellent Battery" when the battery is 80% or above, "Good Battery" when it is
#between 50% and 79%, "Low Battery" when it is between 20% and 49%, "Critical Battery" when
#it is between 1% and 19%, and "Battery Empty" when the battery level is exactly 0%.

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

#4. Temperature Classification
#An automatic weather monitoring system receives the current temperature in Celsius. Accept the
#temperature and display "Extreme Heat" when it is above 40°C, "Very Hot" when it is between 31°C
#and 40°C, "Warm"when it is between 21°C and 30°C, "Cool" when it is between 11°C and 20°C, "Cold"
#when it is between 0°C and 10°C, and "Freezing" when the temperature is below 0°C.

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

#5. Movie Ticket Category
#A cinema wants to automatically determine the appropriate ticket category based on age. Accept the
#customer's age and display "Free Entry" when the age is below 5, "Child Ticket" when the age is
#between 5 and 12, "Teen Ticket" when the age is between 13 and 17, "Adult Ticket" when the age
#is between 18 and 59, and "Senior Citizen Ticket" when the age is 60 or above.

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

#6. Salary Category
#A company wants to classify employees according to their monthly salary. Accept the salary and display
#"Entry Level" when the salary is below ₹25,000, "Junior Level" when it is between ₹25,000 and
#₹49,999, "Mid Level" when it is between ₹50,000 and ₹74,999, "Senior Level" when it is between
#₹75,000 and ₹99,999, and "Executive Level" when the salary is ₹1,00,000 or above.

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

#7. Internet Speed Classification
#An internet service provider wants to classify the speed of a customer's connection. Accept the internet
#speed in Mbps and display "Very Slow" when the speed is below 10 Mbps, "Slow" when it is between
#10 and 49 Mbps, "Good" when it is between 50 and 99 Mbps, "Fast" when it is between 100 and 499
#Mbps, and "Ultra Fast" when it is 500 Mbps or above.

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
#8. Shopping Cart Classification
#An online shopping website wants to categorize customers according to their cart value. Accept the cart
#value and display "Small Cart" when it is below ₹1,000, "Regular Cart" when it is between ₹1,000
#and ₹4,999, "Large Cart" when it is between ₹5,000 and ₹9,999, "Premium Cart" when it is between
#₹10,000 and ₹19,999, and "Luxury Cart" when it is ₹20,000 or above.


#9. Exam Performance
#A college wants to classify students according to their examination percentage. Accept the percentage
#and display "Outstanding" when it is 90 or above, "Excellent" when it is between 75 and 89, "Good"
#when it is between 60 and 74, "Average" when it is between 40 and 59, and "Poor" when it is below 40.


#10. Fuel Level
#A vehicle monitoring system wants to classify the fuel level of a car. Accept the fuel percentage and
#display "Full" when the fuel is between 75% and 100%, "Half Tank" when it is between 50% and
#74%, "Fuel Getting Low" when it is between 25% and 49%, "Refuel Soon" when it is between 10%
#and 24%, and "Critical Fuel" when it is below 10%.


#11. Electricity Bill Classification
#An electricity company wants to calculate and classify a customer's electricity bill based on units
#consumed. Accept the number of units and calculate the bill using ₹5 per unit when consumption is up
#to 100 units, ₹7 per unit when consumption is between 101 and 300 units, ₹10 per unit when
#consumption is between 301 and 500 units, and ₹15 per unit when consumption is above 500 units.
#Display the total bill and classify the usage as "Low Usage", "Moderate Usage", "High Usage", or
#"Very High Usage" according to the applicable range.


#12. Employee Bonus
#A company gives different bonuses depending on an employee's salary. Accept the monthly salary and
#calculate a bonus of 15% when the salary is below ₹30,000, 10% when it is between ₹30,000 and
#₹50,000, 7% when it is between ₹50,001 and ₹80,000, and 5% when it is above ₹80,000. Display the
#calculated bonus amount.


#13. Shopping Discount
#An online shopping website provides discounts according to purchase amount. Accept the purchase
#amount and apply no discount when it is below ₹2,000, a 5% discount when it is between ₹2,000 and
#₹4,999, a 10% discount when it is between ₹5,000 and ₹9,999, a 15% discount when it is between
#₹10,000 and ₹19,999, and a 20% discount when it is ₹20,000 or above. Display the final payable amount.



#14. Restaurant Service Charge
#A restaurant calculates service charges based on the customer's bill. Accept the bill amount and apply
#no service charge when the bill is below ₹1,000, a 5% service charge when the bill is between ₹1,000 and
#₹2,999, an 8% service charge when the bill is between ₹3,000 and ₹4,999, and a 10% service charge
#when the bill is ₹5,000 or above. Display the final bill after adding the service charge.


#15. Courier Charges
#A courier company charges customers according to package weight. Accept the package weight and
#charge ₹100 when the weight is up to 2 kg, ₹200 when it is above 2 kg and up to 5 kg, ₹400 when it is
#above 5 kg and up to 10 kg, ₹700 when it is above 10 kg and up to 20 kg, and ₹1,200 when it is above 20
#kg. Display the applicable courier charge.


#16. Mobile Recharge Bonus
#A mobile company provides different bonus amounts depending on recharge value. Accept the recharge
#amount and add no bonus when the recharge is below ₹199, ₹50 bonus when it is between ₹199 and
#₹499, ₹150 bonus when it is between ₹500 and ₹999, ₹300 bonus when it is between ₹1,000 and ₹1,999,
#and ₹500 bonus when it is ₹2,000 or above. Display the total amount credited to the customer's account.


#17. Loan Interest Calculation
#A bank provides different interest rates according to loan amount. Accept the loan amount and calculate
#interest at 12% when the loan is below ₹1,00,000, 10% when it is between ₹1,00,000 and ₹4,99,999, 8%
#when it is between ₹5,00,000 and ₹9,99,999, and 7% when it is ₹10,00,000 or above. Display the
#calculated interest amount.


#18. Employee Overtime Payment
#A company pays employees different overtime rates according to the number of overtime hours worked.
#Accept overtime hours and calculate payment at ₹300 per hour when overtime is up to 5 hours, ₹400 per
#hour when overtime is between 6 and 10 hours, ₹500 per hour when overtime is between 11 and 20
#hours, and ₹700 per hour when overtime is above 20 hours. Display the total overtime payment.


#19. Flight Baggage Fee
#An airline allows passengers to carry up to 15 kg of baggage for free. Accept baggage weight and display
#"Free Baggage" when the weight is 15 kg or less, "₹1,000 Fee" when it is between 16 and 20 kg,
#"₹2,000 Fee" when it is between 21 and 25 kg, "₹4,000 Fee" when it is between 26 and 30 kg, and
#"Baggage Not Allowed" when it is above 30 kg.


#20. Electricity Consumption Reward
#An electricity-saving program wants to classify customers according to their monthly consumption.
#Accept the number of units and display "Excellent Saving" when consumption is below 100 units,
#"Good Saving" when it is between 100 and 199 units, "Normal Usage" when it is between 200 and 299
#units, "High Consumption" when it is between 300 and 499 units, and "Excessive Consumption"
#when it is 500 units or above.


#21. Student Result
#A college wants to determine a student's final result using theory and practical marks. Accept both
#marks. If either mark is below 35, display "Fail". If both marks are at least 35 and the average is 75 or
#above, display "Distinction". If the average is between 60 and 74, display "First Division". If the
#average is between 50 and 59, display "Second Division". Otherwise, display "Pass".


#22. Loan Risk Classification
#A bank wants to classify loan applicants based on salary and credit score. Accept salary and credit
#score. Display "High Risk" when salary is below ₹30,000, "High Risk" when salary is sufficient but
#the credit score is below 600, "Medium Risk" when the credit score is between 600 and 699, "Low
#Risk" when the credit score is between 700 and 749, and "Very Low Risk" when the credit score is
#750 or above.


#23. Employee Promotion
#A company wants to classify employees according to experience and performance rating. Accept years
#of experience and performance rating. Display "Not Eligible" when experience is below 1 year,
#"Junior Employee" when experience is between 1 and 2 years, "Needs Improvement" when
#experience is between 3 and 5 years but rating is below 7, "Promotion Consideration" when
#experience is between 3 and 5 years and rating is 7 or above, and "Strong Promotion Candidate"
#when experience is above 5 years and rating is 8 or above.


#24. ATM Transaction Category
#An ATM wants to categorize withdrawal requests. Accept the withdrawal amount and display "Mini
#Withdrawal" when the amount is ₹2,000 or less, "Regular Withdrawal" when it is between ₹2,001
#and ₹10,000, "Large Withdrawal" when it is between ₹10,001 and ₹20,000, "Maximum Withdrawal"
#when it is between ₹20,001 and ₹40,000, and "Transaction Declined" when it exceeds ₹40,000.


#25. Student Scholarship
#A university awards scholarships according to marks and attendance. Accept marks and attendance.
#Display "Not Eligible" when marks are below 60. Display "Basic Scholarship" when marks are
#between 60 and 74. Display "Scholarship Denied - Attendance" when marks are between 75 and
#89 but attendance is below 75%. Display "Good Scholarship" when marks are between 75 and 89 and
#attendance is at least 75%. Display "Full Scholarship" when marks are 90 or above and attendance
#is at least 90%.


#26. Insurance Premium
#An insurance company determines premium category according to age. Accept age and display "Not
#Eligible" when age is below 18, "₹5,000 Premium" when age is between 18 and 30, "₹7,500
#Premium" when age is between 31 and 45, "₹10,000 Premium" when age is between 46 and 60, and
#"₹15,000 Premium" when age is above 60.



#27. Bank Account Category
#A bank wants to recommend an account type based on monthly income. Accept monthly income and
#display "Basic Account" below ₹20,000, "Standard Account" between ₹20,000 and ₹49,999,
#"Premium Account" between ₹50,000 and ₹99,999, "Platinum Account" between ₹1,00,000 and
#₹1,99,999, and "Elite Account" when income is ₹2,00,000 or above.


#28. Hotel Room Category
#A hotel wants to recommend a room according to the customer's budget. Accept the budget and display
#"Economy" below ₹2,000, "Standard" between ₹2,000 and ₹4,999, "Deluxe" between ₹5,000 and
#₹9,999, "Executive" between ₹10,000 and ₹19,999, and "Luxury Suite" when the budget is ₹20,000
#or above.


#29. Gaming Rank
#A video game wants to assign a rank based on the player's score. Accept the score and display
#"Beginner" below 500, "Bronze" between 500 and 999, "Silver" between 1,000 and 1,999, "Gold"
#between 2,000 and 4,999, "Platinum" between 5,000 and 9,999, and "Diamond" at 10,000 or above.


#30. Delivery Priority
#An online shopping company determines delivery priority based on order value and delivery distance.
#Accept order value and distance. Display "Normal" when the order is below ₹1,000, "Priority" when
#the order is at least ₹1,000 and distance is below 10 km, "Express" when the order is at least ₹1,000
#and distance is between 10 and 20 km, and "Special Handling" when the order is at least ₹1,000 and
#distance is above 20 km.


#31. Salary After Increment
#A company wants to calculate an employee's new salary based on the current salary. Accept the current
#salary. If the salary is below ₹30,000, increase it by 20%; if it is between ₹30,000 and ₹49,999, increase it
#by 15%; if it is between ₹50,000 and ₹79,999, increase it by 10%; and if it is ₹80,000 or above, increase it
#by 5%. After calculating the new salary, display "Low Salary" if it is below ₹40,000, "Moderate
#Salary" if it is between ₹40,000 and ₹59,999, "Good Salary" if it is between ₹60,000 and ₹99,999, and
#"High Salary" if it is ₹1,00,000 or above.


#32. Shopping Discount After Coupon
#An online store gives discounts based on the original cart value. Accept the cart value and apply a 5%
#discount below ₹5,000, 10% between ₹5,000 and ₹9,999, and 20% at ₹10,000 or above. After calculating
#the final price, display "Budget Purchase" when it is below ₹4,000, "Regular Purchase" when it is
#between ₹4,000 and ₹7,999, "Premium Purchase" when it is between ₹8,000 and ₹14,999, and
#"Luxury Purchase" when it is ₹15,000 or above.


#33. Student Marks After Grace
#A school gives grace marks to students based on their original marks. Accept the marks and add 5 grace
#marks when the marks are below 33, add 3 grace marks when marks are between 33 and 39, and add no
#grace marks when marks are 40 or above. After calculating the final marks, display "Fail" below 40,
#"Pass" between 40 and 59, "First Class" between 60 and 74, "Distinction" between 75 and 89,
#and "Outstanding" at 90 or above.


#34. Fuel After Consumption
#A car initially has 100 litres of fuel. Accept the amount of fuel consumed. If consumption is below 20
#litres, consume the actual amount; if it is between 20 and 50 litres, consume 20 litres; and if it is above
#50 litres, consume 50 litres. After calculating the remaining fuel, display "Critical" when it is below 20
#litres, "Low" when it is between 20 and 39 litres, "Moderate" when it is between 40 and 69 litres, and
#"High" when it is 70 litres or above.


#35. Bank Balance After Withdrawal
#A customer has a certain bank balance and wants to withdraw money. Accept the balance and
#withdrawal amount. If the withdrawal amount is greater than the balance, display "Insufficient
#Balance". Otherwise, calculate the remaining balance and display "Critical" when it is below
#₹1,000, "Low" when it is between ₹1,000 and ₹4,999, "Safe" when it is between ₹5,000 and ₹19,999,
#and "Healthy" when it is ₹20,000 or above.


#36. Mobile Battery After Usage
#A mobile phone application wants to estimate remaining battery after usage. Accept the current battery
#percentage and number of hours used. Reduce the battery by 5% when usage is below 2 hours, 15%
#when usage is between 2 and 5 hours, 25% when usage is between 6 and 8 hours, and 40% when usage
#is above 8 hours. After calculating the remaining battery, display "Dead Soon" for 10% or below,
#"Critical" for 11–30%, "Low" for 31–60%, and "Healthy" for 61% or above.


#37. Electricity Bill Classification
#An electricity company calculates a customer's bill based on units consumed. Accept the units and
#calculate the bill using ₹5 per unit up to 100 units, ₹7 per unit from 101 to 300 units, ₹10 per unit from
#301 to 500 units, and ₹15 per unit above 500 units. After calculating the bill, display "Low Bill" below
#₹1,000, "Moderate Bill" from ₹1,000 to ₹2,999, "High Bill" from ₹3,000 to ₹4,999, and "Very
#High Bill" when the bill is ₹5,000 or above.


#38. Exam Result With Average
#A college wants to classify students based on marks in three subjects. Accept the three marks and
#calculate the average. If any subject mark is below 35, display "Fail". Otherwise, display "Pass" when#
#the average is below 50, "Second Division" when it is between 50 and 59, "First Division" when
#it is between 60 and 74, "Distinction" when it is between 75 and 89, and "Outstanding" when it is
#90 or above.


#39. Loan Eligibility
#A bank wants to classify loan applicants according to salary and disposable income. Accept salary and
#monthly expenses and calculate disposable income by subtracting expenses from salary. Display "Not
#Eligible" when salary is below ₹30,000, "High Risk" when disposable income is below ₹10,000,
#"Medium Risk" when disposable income is between ₹10,000 and ₹19,999, "Low Risk" when it is
#between ₹20,000 and ₹39,999, and "Excellent Eligibility" when disposable income is ₹40,000 or
#above.


#40. Employee Performance Score
#A company calculates an employee's performance score using attendance, performance rating, and
#experience. Accept all three values and calculate the score using performance_rating × 5 +
#attendance/10 + experience × 2. Display "Poor" when the score is below 100, "Average" when it
#is between 100 and 119, "Good" when it is between 120 and 139, "Excellent" when it is between 140
#and 159, and "Outstanding" when it is 160 or above.


#41. Restaurant Final Bill
#A restaurant wants to calculate the final bill based on the bill amount and number of people. Accept both
#values and calculate the per-person amount. Display "Budget Meal" when the per-person amount is
#below ₹500, "Regular Meal" when it is between ₹500 and ₹999, "Premium Meal" when it is between
#₹1,000 and ₹1,999, and "Luxury Meal" when it is ₹2,000 or above. After classification, apply a 5%
#discount when the original bill is below ₹2,000, 10% when it is between ₹2,000 and ₹4,999, and 15%
#when it is ₹5,000 or above, and display the final bill.


#42. Employee Final Salary
#A company wants to calculate an employee's final salary according to performance rating. Accept basic
#salary and performance rating. Give no increment when rating is below 5, a 5% increment when rating is
#between 5 and 6, a 10% increment when rating is between 7 and 8, and a 20% increment when rating is
#between 9 and 10. After calculating the final salary, display "Low Income" below ₹30,000, "Moderate
#Income" between ₹30,000 and ₹49,999, "Good Income" between ₹50,000 and ₹79,999, and "High
#Income" at ₹80,000 or above.


#43. Cricket Player Classification
#A cricket application wants to classify a player's performance based on runs and strike rate. Accept both
#values. Display "Low Scorer" when runs are below 50, "Average Performer" when runs are between


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


#45. Online Shopping Final Status
#An e-commerce company wants to determine the type of order based on cart value, membership, and
#delivery distance. Accept all three values. Display "Small Order" when the cart value is below ₹1,000,
#"Regular Order" when the cart is ₹1,000 or above and the customer has Basic membership,
#"Priority Order" when the customer has Premium membership and the delivery distance is below 10
#km, "Express Order" when the Premium customer's distance is between 10 and 25 km, and "Special
#Delivery" when the Premium customer's distance is above 25 km.


#46. Hospital Billing Category
#A hospital calculates a patient's consultation fee based on age and emergency status. Accept age,
#consultation fee, and emergency status. Apply a 30% discount for emergency patients aged 60 or above,
#20% for emergency patients below 60, 15% for non-emergency patients aged 60 or above, and 5% for all
#other patients. After calculating the final fee, display "Low Fee" below ₹500, "Standard Fee" between
#₹500 and ₹999, "Premium Fee" between ₹1,000 and ₹1,999, and "High Fee" when the fee is ₹2,000 or
#above.

#47. ATM Risk Classification
#An ATM wants to classify the risk level of a withdrawal. Accept the account balance and withdrawal
#amount. If the withdrawal amount is greater than the account balance, display "Transaction
#Declined". Otherwise, calculate the remaining balance and display "Critical Withdrawal" when
#the remaining balance is below ₹1,000, "High Risk" when it is between ₹1,000 and ₹4,999, "Safe"
#when it is between ₹5,000 and ₹19,999, and "Very Safe" when it is ₹20,000 or above.


#48. Electricity Consumption Analysis
#An electricity company wants to analyze a customer's current bill compared with the previous bill.
#Accept units consumed and previous bill amount. Calculate the current bill using ₹5 per unit up to 100
#units, ₹7 per unit for 101–300 units, ₹10 per unit for 301–500 units, and ₹15 per unit above 500 units.
#Display "Low Consumption" when the current bill is below ₹1,000, "Consumption Increased" when
#the current bill is between ₹1,000 and ₹2,999 and is greater than the previous bill, "Consumption
#Stable"when the current bill is between ₹1,000 and ₹2,999 and is equal to or less than the previous bill,
#"High Consumption" when the bill is between ₹3,000 and ₹4,999, and "Excessive Consumption"
#when the bill is ₹5,000 or above.



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

#50. Employee Career Classification
#A company wants to automatically classify an employee's career status. Accept the employee's current
#salary, years of experience, performance rating, and attendance percentage. Calculate a performance
#score using performance_rating × 10 + attendance/10 + experience. Then use if-elif-else
#to display "Entry Level Employee" when salary is below ₹30,000, "Not Ready For Promotion"
#when the salary is at least ₹30,000 but the performance score is below 80, "Needs Improvement" when
#the score is between 80 and 99, "Promotion Consideration" when the score is between 100 and 119,
#"Promotion Recommended" when the score is between 120 and 139, and "Fast Track Candidate"
#when the score is 140 or above.
