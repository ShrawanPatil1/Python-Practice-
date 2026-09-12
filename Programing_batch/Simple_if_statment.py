#Simple if statements
'''
1. ATM Withdrawal: An ATM accepts a withdrawal amount from a customer. The bank allows
customers to withdraw money only when the amount entered is exactly divisible by ₹500. Write a
Python program to display "Withdrawal Approved" when the condition is satisfied. For example,
if the input is 2500, the output should be Withdrawal Approved.

amount = int (input("Enter withdrawl amount : "))

if amount % 500 ==0:
        print("Withdrawal Approved")

'''
'''
2. Attendance Warning: A college wants to automatically identify students whose attendance is
below the required limit. Accept the student's attendance percentage and write a Python program
to display "Attendance Shortage" when the attendance is less than 75%. For example, if the
input is 68, the output should be Attendance Shortage.

a = int(input("Enter Your Attendance IN %: "))

if a <= 75 :
    print("Attendance Shortage")
'''

#3. Salary Bonus: A company has decided to give a special bonus announcement to employees
#whose salary is greater than ₹50,000. Accept the employee's salary and write a program to
#display "Eligible for Special Bonus" when the condition is satisfied.
'''
salary = int(input("Enter the salary : "))

if salary >= 50000:
    print("Eligible for Special Bonus")

'''

#4. Mobile Battery: A mobile phone should warn its user when the battery level reaches 20% or
#below. Accept the current battery percentage and write a program to display "Low Battery" when
#the battery percentage is less than or equal to 20.
'''
battery = int(input("Enter the Mobile Battery level: "))

if battery <=20:
    print("Low Battery")
'''

#5. Traffic Fine: A traffic monitoring system records the speed of a vehicle. If the vehicle is travelling
#at more than 80 km/h, the system should display "Fine Imposed". For example, an input of 95
#should produce Fine Imposed.
'''
speed = int(input("enter the vehicle Speed: "))

if speed >=80:
    print("Fine Imposed")
'''

#6. Pizza Offer: A pizza restaurant gives a free soft drink whenever a customer orders at least 3
#pizzas. Accept the number of pizzas ordered and write a program to display "Free Drink Added"
#when the customer qualifies.
'''
pizza = int(input("Enter the Pizza Orders number: "))

if pizza >=3:
    print("Free Drink Added")
'''
#7. Premium Customer: A bank considers a customer a premium customer if their monthly spending
#exceeds ₹1,00,000. Accept the monthly spending amount and display "Premium Customer"
#vwhen the spending crosses the required limit.
'''
amount = int(input("Enter the amount: "))

if amount >= 100000:
    print("Premium customer")

'''
#8. Login Security: A website locks an account when the user has made exactly 5 failed login
#attempts. Accept the number of failed attempts and write a program to display "Account Locked"
#when the number of attempts is 5.
'''
number = int(input("Enter the Login attempts: "))

if number >=5:
    print("Account Locked")
'''
#9. Birthday Reward: A shopping application gives a special birthday reward to customers who are
#exactly 25 years old. Accept the customer's age and display "Birthday Reward Unlocked" when
#the age is exactly 25.
'''
number = int(input(" Enter the Birthday Year : "))

if number == 25:
    print( "Birthday Reward Unlocked" )
'''
#10.Shopping Coupon: An online shopping website gives a special coupon to customers whose cart
#value is greater than ₹5,000. Accept the cart value and write a program to display "Coupon
#Applied" when the condition is satisfied.
'''
coupon = int(input("Enter the coupon count / cart value: "))

if coupon >= 5000:
    print("Coupon Applied")
'''

#11.Car Service: A car company recommends servicing a vehicle once it has travelled at least 10,000
#kilometres. Accept the number of kilometres travelled and display "Service Due" when the
#vehicle has reached or crossed the service limit.
'''
number = int(input("Enter the vehicle Travelled In Kilometres : "))

if numver >= 10000:
    print("Service Due")
    
'''

#12.Library Fine: A library charges a fine when a book is returned more than 7 days late. Accept the
#number of overdue days and display "Fine Applicable" when the overdue period is greater than 7
#days.
'''
number = int(input("Enter the fine days : "))

if number >=7:
    print("Fine Applicable")
'''

#13.Gym Reward: A gym gives a free protein shake to members who attend at least 20 times in a
#month. Accept the number of visits and display "Free Protein Shake" when the member qualifies.
'''
number = int(input("Enter the number of attend the gym: "))

if number >=20:
    print("Free Protein Shake")
'''
#14.Movie Discount: A cinema offers a senior citizen discount to customers who are 60 years old or
#above. Accept the customer's age and display "Senior Citizen Discount" when the condition is
#satisfied.
'''
age = int(input("Enter the age: "))

if age >=60:
    print("Senior Citizen Discount")
'''
#15.Air Conditioner: An automatic air-conditioning system should activate cooling mode whenever
#the room temperature rises above 30°C. Accept the temperature and display "Cooling Mode
#Activated" when the temperature exceeds 30.
'''
mod = int(input("Enter the Temperature : "))
if mod >=30:
    print("Cooling Mode")
'''
#16.Laptop Storage: A laptop should warn the user when available storage falls below 10 GB. Accept
#the available storage and display "Storage Almost Full" when the value is less than 10.
'''
sto = int(input("Enter the Storage number: "))
if sto <=10:
    print("Storage Almost Full")
'''
#17.Courier Weight: A courier company categorizes a package as a heavy package when its weight
#exceeds 20 kg. Accept the package weight and display "Heavy Package" when the package
#crosses the limit.
'''
weight = int(input("Enter the Package Weight: "))
if weight >=20:
    print("Heavy Package")
'''
#18.Coffee Shop Reward: A coffee shop gives a free cookie whenever a customer's bill is exactly
#₹500. Accept the bill amount and display "Free Cookie" when the amount is exactly 500.
'''
a = int(input("Enter the bill amount: "))
if a == 500:
    print("Free Cookie")
'''

#19.Gaming Achievement: A video game unlocks a special achievement when the player's score
#exceeds 10,000. Accept the player's score and display "Achievement Unlocked" .
'''
game = int(input("Enter the Player's score: "))
if game == 10000:
    print("Achievement Unlocked")
'''

#20.Even Number Prize: A competition awards a prize whenever the participant enters an even
#number. Accept an integer and display "You Won a Prize!" when the entered number is even.
'''
game = int(input("Enter the number: "))
if game % 2==0 :
    print("You Won a Prize!")
'''
#21.Lucky Number: A school has declared 27 as the lucky roll number for a particular event. Accept a
#student's roll number and display "You Are Today's Lucky Student" only when the roll number is
#exactly 27.
'''
num = int(input("Enter the roll number: "))
if num == 27:
    print("You are Today's Lucky Student")
'''
#22.Divisibility Bonus: A mathematical game gives a bonus point whenever the entered number is
#exactly divisible by 7. Accept an integer and display "Bonus Point" when the number satisfies the
#condition.
'''
num = int(input("Enter the number: "))
if num % 7==0 :
    print("Bonus Point")
'''
#23.ATM PIN: An ATM accepts a predefined PIN of 4321. Accept the PIN from the user and display
#"PIN Accepted" only when the entered PIN matches exactly.
'''
pin = int(input("Enter the PIN: "))

if pin == 4321:
    print("PIN Accepted")
'''

#24.Password Security: A website considers a password strong when it contains at least 8
#characters. Accept a password from the user and display "Strong Password" when the password
#length is 8 or more.
'''
pas = int(input("Enter the 8 digit Password: "))
if pas // 10000000:
    print("Strong Password")
'''

#25.Breakup Cancellation: A girl tells her boyfriend that she will cancel the breakup only if he brings
#at least 10 flowers. Accept the number of flowers and display "Breakup Cancelled " when the
#number is 10 or more.
'''
a = int(input("Enter the Flower count: "))
if a >=10:
    print("Greakup Cancelled")
'''
#26.Chocolate Condition: A boyfriend promises his girlfriend that if she gives him more than 10
#chocolates, he will share his Netflix password with her. Accept the number of chocolates and
#display "Netflix Password Shared " when the number is greater than 10.
'''
a = int(input("Enter the count: "))
if a >=10:
    print("Netflix Password Shared")
'''
#27.Screen-Time Warning: A smartphone application wants to encourage users to spend less time
#on their phones. Accept the number of hours spent on the phone and display "Go Outside!" if the
#screen time exceeds 8 hours.
'''
a = int(input("Enter the smartphone application use in time : "))
if a >=8:
    print("Go Outside!")
'''
#28.GST Verification: An accounting application requires additional verification whenever an invoice
#amount is ₹50,000 or more. Accept the invoice amount and display "GST Verification Required"
#when the amount satisfies the condition.
'''
a = int(input("Enter the amount: "))
if a >=50000:
    print("GST Verification Required")
'''
#29.Sports Qualification: A sports competition awards a qualification bonus to a player who scores
#exactly 100 points. Accept the player's score and display "Qualification Bonus" only when the
#score is exactly 100.
'''
a = int(input("Enter the amount: "))
if a >=100:
    print("Qualification Bonus")
'''
#30.Fuel Warning: A vehicle application receives the current fuel percentage and the distance
#travelled. The application should display "Refuel Now" when the fuel percentage is below 20%.
#The distance travelled should also be accepted as input even though it is not required for the
#condition.
'''
a = int(input("Enter the current fuel percentage: "))
b = int(input("Enter the how many destent Travelled: "))
if a <=20:
    print("Refuel Now")
'''
#31.VIP Shopping: An online shopping website gives a VIP gift only when the customer's purchase
#amount is greater than ₹10,000 and the customer has a "VIP" membership. Accept both values
#and display "VIP Gift Added" when both conditions are satisfied.
'''
amount = int(input("Enter the Purchase Amount: "))
m = str(input("Enter Yes or No wen you have VIP Membership: "))

if amount >= 10000 and m == "Yes":
    print("VIP Gift Added")
'''
#32.Exam Eligibility: A university allows a student to appear for the final examination only when their
#attendance is at least 75% and their internal marks are at least 40. Accept both values and display
#"Allowed for Exam" when both requirements are satisfied.
'''
attendance = int(input("Enter the Attendance Persentage: "))
internal = int(input("Enter the Internal marks: "))

if attendance >=75 and internal >=40:
    print("Allowed for Exam")
'''
#33.Bank Loan: A bank starts processing a loan application only when the applicant's salary is greater
#than ₹50,000 and their credit score is at least 750. Accept the salary and credit score and display
#"Loan Processing Started" when both conditions are satisfied .
'''
salary = int(input("Enter the Applicant's Salary: "))
credit = int(input("Enter the credit Score: "))

if salary >= 50000 and credit >= 750:
    print("Loan Processing Started")
'''
#34.Concert Entry: A concert organizer allows VIP entry only to customers who are at least 18 years
#old and have purchased a "VIP" ticket. Accept the age and ticket type and display "VIP Entry"
#when both conditions are satisfied.
'''
age = int(input("Enter the Age: "))
ticket = str(input("Enter Yes or No wen you have VIP Ticket: "))

if age >= 18 and ticket == "Yes":
    print("VIP Entry")
'''
#35.Breakup Challenge: A girl tells her boyfriend, "I will forgive you only if you bring at least 10
#flowers, at least 5 chocolates, and apologize." Accept the number of flowers, number of
#chocolates, and apology status. Display "Forgiven " only when all three conditions are satisfied.
'''
flowers = int(input("Enter the Flowers Count: "))
chocolates = int(input("Enter the Chocolates Count: "))
a = str(input("Enter Yes or No wen you are Apologize: "))

if flowers >= 10 and chocolates >= 5 and a == "Yes":
    print("Forgiven ")
'''
#36.ATM Security: An ATM should approve a transaction only when the entered PIN is 4321 and the
#withdrawal amount is ₹20,000 or less. Accept both values and display "Transaction Approved"
#only when both conditions are satisfied.
'''
pin = int(input("Enter the ATM pin: "))
amount = int(input("Enter the Withdrawal Amount: "))

if pin == 4321 and amount <= 20000:
    print("Transaction Approved")
'''
#37.Smartphone Offer: An electronics store offers a free smartwatch to customers whose budget is
#greater than ₹50,000 and who select the "Premium" model. Accept the budget and model choice
#and display "Free Smartwatch Added " when both conditions are satisfied.
'''
budget = int(input("Enter the Budget: "))
gift = str(input("Enter the model: " ))

if budget >= 50000 and gift == "Premium":
    print("Free Smartwatch Added")
'''
#38.Interview Shortlisting: A company wants to shortlist candidates whose Python score, SQL score,
#and communication score are all at least 70. Accept the three scores and display "Shortlisted"
#only when all three conditions are satisfied.
'''
python = int(input("Enter the Python Score: "))
sql = int(input("Enter the SQL Score: "))
c = int(input("Enter the Communication Score: "))

if python and sql and c >= 70:
    print("Shortlisted")
'''
#39.Employee Promotion: A company considers an employee for promotion when their experience is
#at least 3 years, their performance rating is at least 8, and their attendance is at least 90%. Accept
#all three values and display "Promotion Eligible" only when all requirements are satisfied.
'''
e = int(input("Enter the Employee Experience: "))
p = int(input("Enter the Employee Rating: "))
a = int(input("Enter the Employee Attendance: "))

if e >=3 and p >= 8 and a >= 90:
    print("Promotion Eligible")
'''
#40.Best Student Award — Ultimate Challenge: A college wants to automatically identify its best
#student. The student must have attendance of at least 90%, Python marks of at least 85, must
#have completed at least 5 projects, and must have a discipline rating of "Excellent". Accept all
#four values and display "BEST STUDENT AWARD " only when every requirement is satisfied.
'''
attendance = int(input("Enter the Attendance Persentages : "))
python = int(input("Enter the python marks :"))
p = int(input("Enter the How many projects completed : "))

if attendance >= 90 and python >= 80 and p >= 5:
    print("BEST STUDENT AWARD")
'''

#Multiple if condition questions
#1.
#A customer has ₹10,000 in an ATM account and wants to withdraw ₹7,000. After withdrawal:
#• If balance is below ₹5,000, display "Low Balance".
#• If balance is exactly ₹3,000, display "Critical Balance".
#• If balance is above ₹8,000, display "Healthy Balance".
'''
w = int(input("Enter the Withdraw amount: "))
a = 10000 - w
if a <=5000:
    print("Low Balance")
if a == 3000:
    print("Critical Balance")
if a >= 8000:
    print("Healthy Balance")
'''
#2.
#A boy starts the day with 100 love points. His girlfriend deducts 30 points because he replied late and
#another 20 because he forgot to call.
#• If love is below 60, display "Danger Zone".
#• If love is exactly 50, display "She is Angry".
#• If love is below 30, display "Breakup Alert".
'''
a = 100-30-20
if a <=60:
    print("Danger Zone")
if a == 50:
    print("She is Angry")
if a <=30:
    print("Breakup Alert")
'''
#3.
#A customer has ₹8,000 and purchases items worth ₹2,000.
#• If purchase is affordable, deduct it.
#• If remaining balance is below ₹7,000, display "Balance Reduced".
#• If balance is exactly ₹6,000, display "Half Wallet Gone".
'''
amount = 8000
purchases = 2000
if purchases <= amount:
    amount -= purchases
    print(f"Purchase Sucessful Remeaning balancee: {amount}")
if amount <= 7000:
    print("Balance Reduced")
if amount == 6000:
    print("Half Wallet Gone")
'''
#4.
#A phone has 80% battery.
#• If battery is above 50%, use 20%.
#• If battery becomes below 50%, display "Charge Soon".
#• If battery becomes exactly 60%, display "Still Healthy".
#• If battery is below 20%, display "Critical Battery".
'''
phone_battery = 80
if phone_battery >=50:
    phone_battery -= 20
    print("Battery is above 50%")
if phone_battery <=50:
    print("Charge Soon")
if phone_battery == 60:
    print("Still Healthy")
if phone_battery <= 20:
    print("Critical Battery")
'''
#5.
#A customer has ₹1,000 and orders a pizza for ₹700.
#• If the customer can afford it, deduct the price.
#• If remaining money is below ₹500, display "Low Cash".
#• If remaining money is exactly ₹300, display "Wallet Almost Empty".
#• If remaining money is above ₹800, display "Rich Customer".
'''
customer = 1000
pizza = 700

if pizza <= customer:
    customer -= pizza
    print(f"The customer can afford pizza! Balance : {customer}")
if customer <= 500:
    print("Low Cash")
if customer == 300:
    print("Wallet Almost Empty")
if customer >= 800:
    print(" Rich Customer")
'''

#6.
#A girlfriend starts with 100 patience points.
#• If the boy replies after more than 10 minutes, reduce patience by 30.
#• If patience is still above 50, reduce another 20.
#• If patience becomes below 60, display "She is Angry ".
#• If patience becomes exactly 50, display "Dangerous Situation ".
#• If patience becomes below 20, display "BREAKUP ALERT ".
'''
point = 100
boy_replies = int(input("Enter the boy replies in how many Minutes: "))
if boy_replies >= 10:
    point -= 30
    print("Boy Reduce patience by 30%")
if point >= 50:
    point -= 20
    print("It is still above 50% so Boy loss patience by 20%")
if point <= 60:
    print("She is Angry")
if point == 50:
    print("Dangeous Situation")
if point <= 20:
    print("BREAKUP ALEART")
'''
#7.
#A player starts with 100 health points.
#• If enemy damage is greater than 20, reduce health by 30.
#• If health is above 50, reduce another 10.
#• If health is below 50, display "Warning".
#• If health is exactly 60, display "Barely Survived".
#• If health is below 20, display "Game Over".

'''
point = 100
enemy_damage = int(input("Enter the enemy Damage : "))
if enemy_damage >= 20:
    point -= 30
    print("The Damage is Greater than 20 so Health is reduce by 30")
if point >= 50:
    point -= 10
    print("The health is above 50")
if point <= 50:
    print("Warning")
if point == 60:
    print("Barely Survivel")
if point <= 20:
    print("Game Over")
'''
#8.
#A car has 50 litres of fuel.
#• If fuel is above 40, consume 10 litres.
#• If fuel becomes below 45, display "Fuel Decreasing".
#• If fuel becomes exactly 40, display "Half Tank".
#• If fuel is below 20, display "Refuel Immediately".
'''
fuel = 50
if fuel >= 40:
    fuel -= 10
    print("fuel is above 40")
if fuel <= 45:
    print("fuel Decreasing")
if fuel == 40:
    print("Half Tank")
if fuel <= 20:
    print("Refuel Immediately")
'''
#9.
#An employee has a salary of ₹40,000.
#• If salary is below ₹50,000, add ₹5,000.
#• If salary becomes ₹45,000, add another ₹5,000.
#• If salary becomes ₹50,000, display "Good Salary".
#• If salary exceeds ₹50,000, display "High Salary".
'''
salary = 40000
if salary <= 50000:
    salary += 5000
    print("The salary is Below ₹50,000")
if salary == 45000:
    salary += 5000
    print("The salary Become ₹45,000")
if salary == 50000:
    print("Good Salary")
if salary >= 50000:
    print("High Salary")
'''
#10.
#A boy starts with 100 relationship points.
#• If he talks to another girl, deduct 20.
#• If he replies late, deduct 30.
#• If relationship points are below 60, display "Girlfriend Angry ".
#• If points are exactly 50, display "Danger Zone ".
#• If points are below 30, display "Breakup Incoming ".
#• If points become 0, display "Single Again ".
'''
points = 100
a = str(input(" Boy talks to anothe girl (Yes or No): "))
if a == "Yes":
    points -= 20
    print("He Talks to anothe girl")
b = str(input(" Boy replies late (Yes or No): "))
if b == "Yes":
    points -= 30
    print("He replies late")
    if points <= 60:
        print("Girlfrind Angry")
    if points == 50:
        print("Danger Zone")
    if points <30:
        print("Greakup Incoming")
    if points == 0:
        print("single Again")
'''

