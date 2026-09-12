#Nested if statements


#1. Salary Increment Decision
#A company wants to calculate an employee's increment. Accept the employee's salary and performance
#rating. If the salary is below ₹50,000, check whether the performance rating is at least 8; if it is, give a
#15% increment, otherwise give a 5% increment. If the salary is ₹50,000 or above, check whether the
#rating is at least 9; if it is, give a 10% increment, otherwise give a 3% increment. Display the increment
#amount and the final salary.
'''
salary = int(input("Enter the Employee's salary amount: "))
rating = int(input("Enter the Employee's performance Rating: "))

if salary < 50000:

    if rating >= 8:
        increment = 0.15
    else:
        increment = 0.05
else:

    if rating >= 9:
        increment = 0.10
    else:
        increment = 0.03

total = salary * increment
salaryy = salary + total

print(f"The incremetn percent: {increment * 100:.0f}%")
print(f"The increment amount: {total:.2f}")
print(f"The increment Salary: {salaryy:.2f}")
'''
#2. Shopping Discount
#An online shopping website wants to calculate a customer's discount. Accept the cart value and
#membership type. If the cart value is at least ₹5,000, check whether the customer is a "Gold" member; if
#yes, give a 20% discount, otherwise give a 10% discount. If the cart value is below ₹5,000, check whether
#the customer is a "Gold" member; if yes, give a 10% discount, otherwise give no discount. Display the
#discount and final amount.
'''
value = int(input("Enter the Cart Value:"))
m = (input("Enter the Membership Type:"))

if value >= 5000:

    if m == "Gold":
        d = 0.20
    else:
        d = 0.10

else:

    if m == "Gold":
        d = 0.10
    else:
        d = 0.00

discount = value * d
amount = value + discount

print(f"The Discount is : {d * 100: .0f}%")
print(f"The final Amount is: {amount: .2f}")
'''        
#3. Restaurant Bill
#A restaurant wants to calculate the final bill. Accept the bill amount and whether the customer is a
#member. If the bill is above ₹3,000, check whether the customer is a member; if yes, provide a 15%
#discount, otherwise provide a 5% discount. If the bill is ₹3,000 or below, check whether the customer is a
#member; if yes, provide a 5% discount, otherwise provide no discount. Display the final bill.
'''
bill = int(input("Enter the Bill amount: "))
m = input("Enter the You are Member Yes or Not:")

if bill >= 3000:

    if m == "Yes":
        d = 0.15
    else:
        d = 0.05
else:

    if m == "Yes":
        d = 0.05
    else:
        d = 0.00

discount = bill * d
billl = bill + discount

print(f"The final bill is :{billl: .2f}")
'''
#4. Electricity Bill
#An electricity company wants to calculate a customer's bill. Accept units consumed. If units are greater
#than 300, calculate the bill at ₹10 per unit and then check whether the bill exceeds ₹4,000; if it does, add
#a ₹500 surcharge. Otherwise, calculate the bill at ₹7 per unit and check whether the bill exceeds ₹2,000;
#if it does, add a ₹200 surcharge. Display the final bill.
'''
units = int(input("Enter the total Units Consumed: "))

if units > 300:
    bill = units * 10
    if bill > 4000:
        c = 500
    else:
        c = 0
else:
    bill = units * 7
    if bill > 2000:
        c = 200
    else:
        c = 0

final = bill + c

print(f"The final bill: ₹{final:.2f}")
'''
#5. ATM Withdrawal
#An ATM contains a customer's balance. Accept balance and withdrawal amount. If the withdrawal
#amount is less than or equal to the balance, check whether the withdrawal is greater than ₹20,000. If yes,
#display "Large Withdrawal"; otherwise display "Normal Withdrawal". If the withdrawal is greater
#than the balance, check whether the customer has an overdraft facility. If yes, allow the transaction;
#otherwise display "Insufficient Balance".
'''
b = int(input("Enter the Balance amount:"))
w = int(input("Enter the Withdrawal Amount:"))
 

if w <= b:

    if w >= 20000:
        print("Large withdrawal")
    else:
        print("Normal Withdrawal")

else:

    o = input("Enter the Yes or No, you has an overdraft Facility:")

    if o == "Yes":
        print("You are allowd for Transaction")
    else:
        print("Insufficient Balance")
'''    

#6. Loan Eligibility
#A bank wants to determine whether a person qualifies for a loan. Accept salary, credit score and existing
#EMI. If salary is at least ₹50,000, check whether the credit score is at least 700. If it is, check whether the
#existing EMI is below ₹15,000; if yes, display "Loan Approved", otherwise display "High Existing
#EMI". If the credit score is below 700, display "Low Credit Score". If salary is below ₹50,000, display
#"Salary Too Low".
'''
s = int(input("Enter the salary amount:"))
c = int(input("Enter the credit score:"))
emi = int(input("Enter the existing EMI:"))

if s >= 50000:

    if c >= 700:

        if emi < 15000:
            print("Loan Approved")
        else:
            print("High Existing EMI")

    else:
        print("Low Credit score")

else:
    print("Salary Too Low")

'''
#7. Employee Bonus
#A company calculates annual bonuses based on salary and performance. If salary is below ₹40,000,
#check whether the performance rating is at least 8. If yes, calculate a 10% bonus; otherwise calculate
#5%. If salary is ₹40,000 or above, check whether the performance rating is at least 9. If yes, calculate
#15%; otherwise calculate 7%. Display the bonus.
'''
s = int(input("Enter the salary:"))
p = int(input("Enter the performance rating:"))

if s < 40000:

    if p >= 8:
        b = 0.10
    else:
        b = 0.05
else:

    if p >= 9:
        b = 0.15
    else:
        b = 0.07

bonus = s * b
print(f"The bonus is: {bonus:0.2f}")
'''       
#8. Student Result
#Accept theory marks and practical marks. If theory marks are at least 40, check practical marks. If
#practical marks are also at least 40, calculate the average. If the average is at least 75, display
#Distinction"; otherwise display "Pass". If practical marks are below 40, display "Fail in
#Practical". If theory marks are below 40, display "Fail in Theory".
'''
t = int(input("Enter the Theory Marks:"))
p = int(input("Enter the Practical Marks:"))

if t >= 40:

    if p >= 40:
        a = (t + p) / 2

        if a >=75:
            print("Distinction")
        else:
            print("Pass")
    else:
        print("Fail in Practical")
else:
    print("Fail in Theory")
'''
#9. Mobile Recharge
#A telecom company wants to calculate a recharge bonus. Accept recharge amount and customer type. If
#recharge is ₹500 or above, check whether the customer is "Premium". If yes, provide ₹200 cashback;
#otherwise provide ₹100 cashback. If recharge is below ₹500, check whether the customer is "Premium".
#If yes, provide ₹50 cashback; otherwise provide no cashback.
'''
a = int(input("Enter the Recharge Amount:"))
c = input("Enter the Type of Customer:").strip()

if a >= 500:

    if c == "Premium":
        print("You got ₹200 cashback")
    else:
        print("You got ₹100 cashback")

else:

    if c == "Premium":
        print("You got ₹50 cashback")
    else:
        print("You got No cashback")

'''
#10. Hotel Booking
#A hotel calculates room charges based on room type and number of nights. If the room type is "Deluxe",
#check whether the stay is more than 3 nights. If yes, give a 20% discount; otherwise give 10%. If the room
#type is "Standard", check whether the stay is more than 5 nights. If yes, give 15%; otherwise give 5%.
#Calculate the final bill.
'''
t = input("Enter the Room Type:")
n = int(input("Enter the Number of Nights:"))

if t == "Delux":
    bill = 3000 * n

    if n > 3:
        discount = bill * 0.20
    else:
        discount = bill * 0.10
else:

    if t == "Standard":
        bill = 2000 * n
        
        if n > 5:
            
            discount = bill * 0.15
        else:
            discount = bill * 0.05

f_bill = bill - discount
print("Final bill:₹", f_bill)
'''
#11. The "Why Did You Like Her Photo?" Problem
#A boy notices that his girlfriend liked another boy's Instagram photo. Accept whether she liked the photo
#and whether the boy is her close friend. If she liked the photo, check whether the boy is a close friend. If
#yes, display "Relax, He Is Just A Friend"; otherwise display "Investigation Started". If she
#did not like the photo, display "Boy Can Sleep Peacefully".
'''
l = input("Enter the whether she liked the Phot, Yes or No :")
f = input("The boy is her close Frind, Yes or No:")

if l == "Yes":

    if f == "Yes":
        print("Relax, He Is Just A Friend")
    else:
        print("Investigation Started")
else:
    print("Boy Can Sleep Peacefully")
'''
#12. The Late Reply Mystery
#A girl sends a message to her boyfriend, but he replies after two hours. Accept reply time in minutes. If
#the reply takes more than 60 minutes, check whether he had informed her beforehand. If yes, display
#"Okay, Forgiven"; otherwise display "Long Explanation Required". If the reply takes 60 minutes
#or less, display "Normal Conversation".
'''
r = int(input("Enter the Boy's Reply Time in Minutes: "))
i = input("Enter the wherther he had Informed her beforehad Yes or No: ")

if r > 60:
    
    if i == "Yes":
        print("Okay, Forgiven")
    else:
        print("Long Explanation Required")

else:
    print("Normal Conversation")
'''
#13. The "Good Night" Investigation
#A girl receives "Good Night " from her boyfriend. Accept whether the heart emoji was included. If the
#heart was included, check whether the message was sent before midnight. If yes, display
#"Relationship Safe"; otherwise display "Why Are You Awake At 2 AM?". If there is no heart
#emoji, display "Suspicious Good Night".
'''
m = input("Was the heart emoji included?:")
t = int(input("Enter the massage Time:"))

if m == "Yes":

    if  t < 24:
        print("Relationship Safe")
    else:
        print("Why Are You Awake At 2 AM?")
else:
    print("Suspicious Good Night")
'''
#14. The Ex-Girlfriend Like
#A boy discovers that his girlfriend liked her ex-boyfriend's old photo. Accept whether the photo is recent
#or old. If she liked the photo, check whether the photo is from before their relationship started. If yes,
#display "Historical Evidence"; otherwise display "Emergency Relationship Meeting".
'''
liked = input("Did she like the photo? ")
photo = input("Is the photo recent or old? ")

if liked == "Yes":

    if photo == "old":
        print("Historical Evidence")
    else:
        print("Emergency Relationship Meeting")

else:
    print("No Problem")
'''
#15. The "Who Is She?" Question
#A girl sees her boyfriend chatting with another girl. Accept whether the girl is a classmate and whether
#the conversation is related to studies. If the girl is a classmate, check whether the conversation is studyrelated. If yes, display "Academic Conversation"; otherwise display "Further Investigation
#Required". If she is not a classmate, display "Suspicious Person Detected".
'''
c = input("Is the girl a classmate? ")
s = input("Is the conversation related to studies? ")

if c == "Yes":

    if s == "Yes":
        print("Academic Conversation")
    else:
        print("Further Investigation Required")

else:
    print("Suspicious Person Detected")
'''

#16. The Birthday Test
#A girlfriend's birthday is today. Accept whether the boyfriend remembered her birthday. If he
#remembered, check whether he also bought a gift. If yes, display "Boyfriend Passed"; otherwise
#display "Birthday Gift Investigation". If he forgot the birthday, display "Relationship
#Emergency".
'''
r = input("Did boyfriend remember the birthday? ")
g = input("Did he buy a gift? ")

if r == "Yes":

    if g == "Yes":
        print("Boyfriend Passed")
    else:
        print("Birthday Gift Investigation")

else:
    print("Relationship Emergency")
'''
#17. The "I Am Fine" Problem
#A girl tells her boyfriend "I am fine." Accept whether she actually sounds angry. If she says she is
#fine, check whether she sounds angry. If yes, display "She Is Definitely Not Fine"; otherwise
#display "Probably Fine". If she does not say she is fine, display "Conversation Continues".
'''
f = input("Did she say I am fine? ")
a = input("Does she sound angry: ")

if f == "Yes":

    if a == "Yes":
        print("She Is Definitely Not Fine")
    else:
        print("Probably Fine")

else:
    print("Conversation continues")
'''
#18. The Double-Tick Mystery
#A boy sends a message to his girlfriend and receives a reply after seeing the message was read. Accept
#whether the message was read and whether she replied. If the message was read, check whether she
#replied. If yes, display "Problem Solved"; otherwise display "Why Did You Leave Me On Seen?". If
#the message was not read, display "Probably Busy".
'''
r = input("Was the message read: ")
p = input("Did she reply? ")

if r == "Yes":

    if p == "Yes":
        print("Problem Solved")
    else:
        print("Why Did You Leave Me On Seen?")

else:
    print("Probably Busy")
'''
#19. The "Online But Not Replying" Case
#A girl notices that her boyfriend is online but has not replied for 20 minutes. Accept whether he is online
#and whether he has replied. If he is online, check whether he replied. If yes, display "No Problem";
#otherwise check whether he is currently in a group chat. If yes, display "Interesting..."; otherwise
#display "Serious Investigation".
'''
o = input("Is he online? ")
r = input("Did he reply? ")
g = input("Is he in a group chat? ")

if o == "Yes":

    if r == "Yes":
        print("No Problem")
    else:

        if g == "Yes":
            print("Interesting...")
        else:
            print("Serious Investigation")

else:
    print("No Problem")
'''
#20. The "Who Is Your Best Friend?" Trap
#A boy asks his girlfriend who her best friend is. Accept whether she names him. If she names him, check
#whether she also says "You Are My Favorite Person". If yes, display "Boy Wins"; otherwise
#display "Boy Wants More Confirmation". If she names someone else, display "Relationship
#Meeting Required".
'''
b = input("Did she name him as her best friend? ")
f = input("Did she say You Are My Favorite Person? ")

if b == "Yes":

    if f == "Yes":
        print("Boy Wins")
    else:
        print("Boy Wants More Confirmation")

else:
    print("Relationship Meeting Required")
'''
#21. The Apology Decision
#A couple has a fight. Accept whether the boy apologized and whether the apology was genuine. If he
#apologized, check whether it was genuine. If yes, display "Fight Can Be Resolved"; otherwise
#display "Nice Try, But No".
'''
a = input("Did the boy apologize? ")
g = input("Was the apology genuine? ")

if a == "Yes":

    if g == "Yes":
        print("Fight Can Be Resolved")
    else:
        print("Nice Try, But No")
'''
#22. The "I Was Busy" Excuse
#A girl did not receive a reply for five hours. The boy says he was busy. Accept whether he was actually
#busy and whether he informed her earlier. If he was busy, check whether he informed her. If yes, display
#"Excuse Accepted"; otherwise display "Communication Problem". If he was not busy, display
#"Caught In 4K".
'''
b = input("Was he actually busy? ")
i = input("Did he inform her earlier? ")

if b == "Yes":

    if i == "Yes":
        print("Excuse Accepted")
    else:
        print("Communication Problem")

else:
    print("Caught In 4K")
'''
#23. The Confession
#A boy wants to confess his feelings to a girl. Accept whether she already knows and whether she likes
#him. If she already knows, check whether she likes him. If yes, display "Confession Has High
#Chances"; otherwise display "Prepare For Friend-Zone".
'''
k = input("Does she already know? ")
l = input("Does she like him? ")

if k == "Yes":

    if l == "Yes":
        print("Confession Has High Chances")
    else:
        print("Prepare For Friend-Zone")
'''
#24. The Friend-Zone Detector
#A boy asks a girl whether she likes him. Accept her response. If she says "Yes", check whether she also
#wants a relationship. If yes, display "Relationship Possible"; otherwise display "Something Is
#Complicated". If she says "No", display "Friend-Zone Confirmed".
'''
r = input("Does she like him? ")
w = input("Does she want a relationship? ")

if r == "Yes":

    if w == "Yes":
        print("Relationship Possible")
    else:
        print("Something Is Complicated")

else:
    print("Friend-Zone Confirmed")
'''

#25. The Breakup Decision
#A couple has been fighting frequently. Accept number of fights and whether both people are willing to
#communicate. If fights are more than 5, check whether both are willing to communicate. If yes, display
#"Relationship Can Be Saved"; otherwise display "Breakup Discussion Required". If fights are
#5 or fewer, display "Normal Relationship Conflict".
'''
f = int(input("Enter number of fights: "))
c = input("Are both willing to communicate? ")

if f > 5:

    if c == "Yes":
        print("Relationship Can Be Saved")
    else:
        print("Breakup Discussion Required")

else:
    print("Normal Relationship Conflict")
'''
#26. The Jealousy Test
#A boy gets jealous when his girlfriend talks to another boy. Accept whether the other boy is a close friend
#and whether the conversation is personal. If the boy is a close friend, check whether the conversation is
#personal. If yes, display "Talk About Boundaries"; otherwise display "No Serious Issue". If he is
#not a close friend, display "Suspicion Level Increased".
'''
f = input("Is the other boy a close friend? ")
p = input("Is the conversation personal? ")

if f == "Yes":

    if p == "Yes":
        print("Talk About Boundaries")
    else:
        print("No Serious Issue")

else:
    print("Suspicion Level Increased")
'''
#27. The Secret Phone Password
#A girlfriend asks for her boyfriend's phone password. Accept whether he shares it and whether he is
#comfortable sharing it. If he shares it, check whether he is comfortable. If yes, display "Mutual Trust";
#otherwise display "Awkward Situation". If he refuses, display "Privacy Discussion Needed".
'''
s = input("Did he share the password? ")
c = input("Is he comfortable sharing it? ")

if s == "Yes":

    if c == "Yes":
        print("Mutual Trust")
    else:
        print("Awkward Situation")

else:
    print("Privacy Discussion Needed")
'''
#28. The "We Need To Talk" Message
#A girl receives a message from her boyfriend saying "We need to talk." Accept whether he has
#previously argued with her and whether the message was sent late at night. If they recently argued, check
#whether the message was sent after midnight. If yes, display "Maximum Anxiety"; otherwise display
#"Serious Conversation Expected". If they did not argue, display "Probably Something
#Important".
'''
a = input("Did they recently argue? ")
t = input("Was the message sent after midnight? ")

if a == "Yes":

    if t == "Yes":
        print("Maximum Anxiety")
    else:
        print("Serious Conversation Expected")

else:
    print("Probably Something Important")
'''
#29. The Relationship Score
#Start with 100 relationship points. Accept whether the partner forgot the birthday, ignored messages,
#apologized, and planned a surprise. If the birthday was forgotten, deduct 30 points. Inside that decision,
#check whether an apology was given; if yes, restore 10 points. If no apology was given, deduct another 10
#points. Then check whether a surprise was planned and adjust the score accordingly. Display the final
#relationship status based on the final score.
'''
score = 100

b = input("Was the birthday forgotten? ")
a = input("Was an apology given? ")
s = input("Was a surprise planned? ")

if b == "Yes":
    score = score - 30

    if a == "Yes":
        score = score + 10
    else:
        score = score - 10

if s == "Yes":
    score = score + 20
else:
    score = score - 10

print("Relationship Score:", score)

if score >= 75:
    print("Good Relationship")
elif score >= 50:
    print("Relationship Needs Attention")
else:
    print("Relationship In Trouble")
'''
#30. The Breakup Countdown
#A couple starts with 100 trust points. Accept whether there was lying, whether the person confessed the
#truth, and whether an apology was made. If lying occurred, deduct 40 points. Inside that decision, check
#whether the person confessed. If yes, restore 20 points and then check whether an apology was made; if
#yes, restore another 10 points. Finally, classify the relationship as "Safe", "Unstable", or "Breakup
#Zone" based on the final score.
'''
score = 100

l = input("Was there lying? ")
t = input("Did the person confess the truth? ")
a = input("Was an apology made? ")

if l == "Yes":
    score = score - 40

    if t == "Yes":
        score = score + 20

        if a == "Yes":
            score = score + 10

print("Trust Score:", score)

if score >= 80:
    print("Safe")
elif score >= 50:
    print("Unstable")
else:
    print("Breakup Zone")
'''

#31. Instagram Story Investigation
#A girl posts a story. Accept whether her boyfriend viewed the story and whether he replied to it. If he
#viewed it, check whether he replied. If he replied, display "Boy Is Active"; otherwise display "Seen
#But Silent". If he did not view it, check whether he was online. If yes, display "Suspicious";
#otherwise display "Probably Busy".
'''
v = input("Did he view the story? ")
r = input("Did he reply to the story? ")
o = input("Was he online? ")

if v == "Yes":

    if r == "Yes":
        print("Boy Is Active")
    else:
        print("Seen But Silent")

else:

    if o == "Yes":
        print("Suspicious")
    else:
        print("Probably Busy")
'''
#32. The Unfollow Mystery
#A boy discovers that his girlfriend unfollowed him. Accept whether she also blocked him. If she
#unfollowed him, check whether she blocked him. If yes, display "Relationship Emergency";
#otherwise display "Conversation Required". If she did not unfollow him, display "Everything Is
#Fine".
'''
u = input("Did she unfollow him? ")
b = input("Did she also block him? ")

if u == "Yes":

    if b == "Yes":
        print("Relationship Emergency")
    else:
        print("Conversation Required")

else:
    print("Everything Is Fine")
'''

#33. The New Follower
#A girl notices that her boyfriend has gained a new female follower. Accept whether he followed her back
#and whether they know each other. If he followed her back, check whether they know each other. If yes,
#display "Probably Normal"; otherwise display "Investigation Required".
'''
f = input("Did he follow her back? ")
k = input("Do they know each other? ")

if f == "Yes":

    if k == "Yes":
        print("Probably Normal")
    else:
        print("Investigation Required")
'''
#34. The Deleted Message
#A boy sees "This message was deleted" in the chat. Accept whether he saw the message before
#deletion. If yes, check whether he remembers what it said. If yes, display "Evidence Available";
#otherwise display "Mystery Continues". If he never saw it, display "No Evidence".
'''
s = input("Did he see the message before deletion? ")
m = input("Does he remember what it said? ")

if s == "Yes":

    if m == "Yes":
        print("Evidence Available")
    else:
        print("Mystery Continues")

else:
    print("No Evidence")
'''
#35. The Typing Indicator
#A girl sees her boyfriend typing for a long time but receives no message. Accept whether he eventually
#sends a message. If he sends one, check whether it is an apology. If yes, display "Fight Resolution
#Incoming"; otherwise display "Normal Message". If he does not send anything, display "Typing
#Mystery".
'''
s = input("Did he eventually send a message? ")
a = input("Is it an apology? ")

if s == "Yes":

    if a == "Yes":
        print("Fight Resolution Incoming")
    else:
        print("Normal Message")

else:
    print("Typing Mystery")
'''
#36. Grocery Shopping List
#A person has a grocery list containing "milk", "bread", "eggs" and "butter". Accept an item from the
#user. If the item is already present in the list, check whether it is "milk". If yes, display "Milk Already
#On List"; otherwise display "Item Already Added". If the item is not present, add it to the list using
#append() and display the updated list.
'''
items = ["milk", "bread", "eggs", "butter"]

i = input("Enter the item: ")

if i in items:

    if i == "milk":
        print("Milk Already On List")
    else:
        print("Item Already Added")

else:
    items.append(i)
    print(items)
'''
#37. Party Guest List
#A person maintains a party guest list. Accept a guest name. If the guest is already in the list, check
#whether the guest is the birthday person's best friend. If yes, display "VIP Guest"; otherwise display
#"Guest Already Added". If the guest is not in the list, add the name using append().
'''
guests = ["Rahul", "Amit", "Sneha"]

g = input("Enter the guest name: ")
best = input("Is the guest the birthday person's best friend? ")

if g in guests:

    if best == "Yes":
        print("VIP Guest")
    else:
        print("Guest Already Added")

else:
    guests.append(g)
    print(guests)
'''

#38. Shopping Cart Using append()
#A customer has an empty shopping cart. Accept a product name and its price. If the price is above
#₹5,000, check whether the product is "Laptop". If yes, add it to the cart and display "Premium Product
#Added"; otherwise display "Expensive Product". If the price is ₹5,000 or below, add the product
#normally using append().
'''
cart = []

p = input("Enter the product name: ")
price = int(input("Enter the price: "))

if price > 5000:

    if p == "Laptop":
        cart.append(p)
        print("Premium Product Added")
    else:
        print("Expensive Product")

else:
    cart.append(p)
    print(cart)
'''
#39. Grocery Restocking Using extend()
#A grocery store has a list of available products. Another supplier sends a list of new products. If the
#supplier list contains more than three products, check whether "Milk" is included. If yes, add all
#products using extend() and display "Major Restocking Completed". Otherwise, add them using
#extend() and display "Regular Restocking".
'''
products = ["Milk", "Bread", "Eggs"]

new_products = ["Rice", "Oil", "Sugar", "Tea"]
 
if len(new_products) > 3:

    if "Milk" in new_products:
        products.extend(new_products)
        print("Major Restocking Completed")
    else:
        products.extend(new_products)
        print("Regular Restocking")

else:
    products.extend(new_products)
    print("Regular Restocking")

print(products)
'''
#40. Playlist Management Using insert()
#A student has a music playlist containing several songs. Accept a new song name. If the song is already
#in the playlist, check whether it is the student's favorite song. If yes, display "Favorite Song Already
#Exists"; otherwise display "Song Already Exists". If the song is not present, insert it at position 1
#using insert() and display the updated playlist.
'''
playlist = ["Song1", "Song2", "Song3"]

s = input("Enter the song name: ")
f = input("Is it your favorite song? ")

if s in playlist:

    if f == "Yes":
        print("Favorite Song Already Exists")
    else:
        print("Song Already Exists")

else:
    playlist.insert(1, s)
    print(playlist)
'''
#41. Emergency Contact
#A phone contains a list of emergency contacts. If the list contains more than three contacts, remove the
#last contact using pop(). Inside this condition, check whether the removed contact was "Mom". If yes,
#display "Important Contact Removed"; otherwise display "Old Contact Removed". If the list
#contains three or fewer contacts, display "Do Not Remove Any Contact".
'''
contacts = ["Dad", "Mom", "Brother", "Friend"]

if len(contacts) > 3:

    removed = contacts.pop()

    if removed == "Mom":
        print("Important Contact Removed")
    else:
        print("Old Contact Removed")

else:
    print("Do Not Remove Any Contact")

print(contacts)
'''
#42. Remove Ex From Contact List
#A person has a contact list containing friends and an ex-partner. Accept a name to remove. If the name
#exists in the list, check whether it is the ex-partner's name. If yes, remove it using remove() and display
#"Ex Removed From Contacts"; otherwise remove it and display "Contact Removed". If the name
#vdoes not exist, display "Contact Not Found".
'''
contacts = ["Rahul", "Amit", "Priya", "Neha"]

name = input("Enter the name to remove: ")
ex = input("Enter the ex-partner's name: ")

if name in contacts:

    if name == ex:
        contacts.remove(name)
        print("Ex Removed From Contacts")
    else:
        contacts.remove(name)
        print("Contact Removed")

else:
    print("Contact Not Found")

print(contacts)
'''
#43. Relationship Anniversary
#A couple stores their anniversary information in a tuple such as (day, month, year). Accept the
#month number. If the month matches the stored anniversary month, check whether the day also
#matches. If both match, display "Happy Anniversary!"; otherwise display "Wrong Date, But Nice
#Try!". If the month does not match, display "Wrong Month".
'''
anniversary = (15, 8, 2025)

m = int(input("Enter the month: "))
d = int(input("Enter the day: "))

if m == anniversary[1]:

    if d == anniversary[0]:
        print("Happy Anniversary!")
    else:
        print("Wrong Date, But Nice Try!")

else:
    print("Wrong Month")
'''
#44. Student Subjects
#A student's registered subjects are stored in a tuple. Accept a subject name. If the subject exists in the
#tuple, check whether it is "Python". If yes, display "Programming Subject Selected"; otherwise
#display "Subject Already Registered". If it does not exist, display "Subject Not Registered".
'''
subjects = ("Python", "Maths", "English", "Physics")

s = input("Enter the subject: ")

if s in subjects:

    if s == "Python":
        print("Programming Subject Selected")
    else:
        print("Subject Already Registered")

else:
    print("Subject Not Registered")
'''
#45. Friend Group
#A person has a set containing their close friends. Accept a friend's name. If the name is already in the set,
#check whether the person is "BestFriend". If yes, display "Best Friend Already In Group";
#otherwise display "Friend Already In Group". If the name is not in the set, add it using add() and
#display the updated set.
'''
friends = {"Rahul", "Amit", "Priya"}

name = input("Enter friend's name: ")

if name in friends:

    if name == "BestFriend":
        print("Best Friend Already In Group")
    else:
        print("Friend Already In Group")

else:
    friends.add(name)
    print(friends)
'''
#46. Party Invitations
#A person has a set of invited guests and receives another set of names. If the new guest is already
#present in the invitation set, check whether the guest is a family member. If yes, display "Family
#Member Already Invited"; otherwise display "Guest Already Invited". If the guest is not
#present, add the name using add().
'''
guests = {"Rahul", "Amit", "Priya"}

name = input("Enter the guest name: ")
family = input("Is the guest a family member? ")

if name in guests:

    if family == "Yes":
        print("Family Member Already Invited")
    else:
        print("Guest Already Invited")

else:
    guests.add(name)
    print(guests)
'''
#47. Student Marks
#A school stores student names and marks in a dictionary. Accept a student's name. If the name exists in
#the dictionary, check whether the student's marks are at least 75. If yes, display "Excellent Student";
#otherwise display "Needs Improvement". If the student does not exist, add the student and their marks
#to the dictionary.
'''
students = {
    "Rahul": 80,
    "Amit": 65,
    "Priya": 90
}

name = input("Enter student's name: ")

if name in students:

    if students[name] >= 75:
        print("Excellent Student")
    else:
        print("Needs Improvement")

else:
    marks = int(input("Enter student's marks: "))
    students[name] = marks
    print(students)
'''
#48. Contact Management
#A phone stores names and phone numbers in a dictionary. Accept a person's name. If the name exists,
#check whether the name belongs to a family member. If yes, display "Family Contact"; otherwise
#isplay "Regular Contact". If the name does not exist, add the person and phone number to the
#dictionary.
'''
contacts = {
    "Rahul": "Friend",
    "Amit": "Family",
    "Priya": "Friend"
}

name = input("Enter the person's name: ")

if name in contacts:

    if contacts[name] == "Family":
        print("Family Contact")
    else:
        print("Regular Contact")

else:
    number = input("Enter phone number: ")
    contacts[name] = number
    print(contacts)
'''
#49. Boyfriend/Girlfriend Investigation
#A girl maintains a dictionary containing people's names and their relationship status, such as "Friend",
#"Best Friend", "Ex", or "Boyfriend". Accept a person's name. If the name exists, check whether the
#relationship is "Boyfriend". If yes, display "Current Relationship"; otherwise check whether it is
#"Ex". If yes, display "Past Relationship"; otherwise display "Friend/Other Contact". If the name
#does not exist, display "Person Not Found".
'''
people = {
    "Rahul": "Friend",
    "Amit": "Boyfriend",
    "Priya": "Ex"
}

name = input("Enter the person's name: ")

if name in people:

    if people[name] == "Boyfriend":
        print("Current Relationship")
    else:

        if people[name] == "Ex":
            print("Past Relationship")
        else:
            print("Friend/Other Contact")

else:
    print("Person Not Found")
'''

#50. RELATIONSHIP CHALLENGE
#A girl maintains a dictionary containing her friends' names and their relationship status, a list containing
#people she has recently chatted with, a tuple containing her favorite people, and a set containing people
#she trusts. Accept a person's name. First check whether the person exists in the dictionary. If the person
#exists, check whether their relationship status is "Boyfriend". If yes, check whether the person is also
#present in the trusted set. If yes, check whether the person is present in the favorite-people tuple. If yes,
#display "This Person Is Extremely Important"; otherwise display "Boyfriend But Not In
#Favorites". If the person is not in the trusted set, display "Boyfriend But Trust Issue". If the
#person is not the boyfriend, check whether the person is present in the recent-chat list. If yes, display
#"Recently Contacted Friend"; otherwise display "Known Person But No Recent Chat". If the
#person does not exist in the dictionary, check whether the name exists in the recent-chat list. If yes, add
#the person to the dictionary with status "New Contact" and display "New Contact Added"; otherwise
#display "Completely New Person".
'''
people = {
    "Rahul": "Boyfriend",
    "Amit": "Friend",
    "Priya": "Ex"
}

recent_chat = ["Rahul", "Amit", "Neha"]

favorite = ("Rahul", "Priya")

trusted = {"Rahul", "Amit"}

name = input("Enter the person's name: ")

if name in people:

    if people[name] == "Boyfriend":

        if name in trusted:

            if name in favorite:
                print("This Person Is Extremely Important")
            else:
                print("Boyfriend But Not In Favorites")

        else:
            print("Boyfriend But Trust Issue")

    else:

        if name in recent_chat:
            print("Recently Contacted Friend")
        else:
            print("Known Person But No Recent Chat")

else:

    if name in recent_chat:
        people[name] = "New Contact"
        print("New Contact Added")
    else:
        print("Completely New Person")
'''
