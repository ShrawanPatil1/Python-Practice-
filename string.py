#STRING & STRING METHODES
"""In Python, string methods are often known as string
functions, but technically they are methods.
These terms are used interchangeably."""


"""UPERCASE AND LOWERCASE"""
"""
name = "How are you Shrawan!"
print(len(name))
print(type(name))  #IT PRINT THE DATATYPE OF THE ANY VARIABLE STORED IN
print(name.upper())  #IT UPPWERCASE THE STRING #IT IS A FUNCTION
print(name.lower())   #IT LOWERCASE THE STRING  #IT IS A FUNCTION
print(name.capitalize()) #IT CAPITAL THE FIRST LETER ONLY OF THE STRING  #IT IS A FUNCTION
print(name.title()) #IT ONLY CAPATIL THE FIRST LETER IN THE STRING
print("-" * 52)
print(name.replace("Shrawan", "Nandhani")) #IT ONLY REPLACE THE STEING IN WHATEVER WE WANT
#IT DEDENT MODIFY THE STRING
print(name)

# SLICING IN THE STRING

print("-" * 52)
gmail = "https://google.com"
print(gmail[8:])
print(gmail[8:-4])

#To SEE THE HOW MANY REPETED STEING OR SIMILAR COUNT IS THER
print("-" * 52)
url = "root of the root is called"
print(url.count("root"))


#STRIPING THE WORD LAST SPACESS
print("-" * 52)
name = " I am Shrawan Patil! from Korpana "
print("Len befor the using the method of strip:", len(name))
name = name.strip()
print("Len after the using the method of strip:", len(name))
print("IT REMOVE THE SPACING OF LAST!")


#STRING FOR MAPING

name = "Shrawan"
id = 1234
print(f"My name is {name} and id is {id}!") #IT PRINT THE ID AND NAME FROM THE MAPING USING (f) starting
print(f"My name is {name} and {25 * 2}!")
print(f"My name is {name} and {25 / 3}!")   #IT GIVE THE OUTPUT OF DIVISION
print(f"My name is {name} and {25 / 3:.2f}!")  #IT GIVES ONLY THE TWO FLOTTING VALUES AFTER THE (.00)
# AND WE CAN INCREASE THE FOLTING NUMBER BY (:.nf) N = ANY NUMBER

#SPOT MAPING BY USING {}
print("-" * 52)

name = "root"
id = 456
print("My name is {} id is {}" .format(name, id))
print()


n = "I have my wone choice!"
print("have" not in n)

print("-" * 52)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

b = "Hello, World!"
print(b[-5:-2])
"""

print(help(str))
