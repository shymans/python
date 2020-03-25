names = input('What is your name?')

print("Hey " + name)

#Fundamental Data Types

print(2 + 4)
print(type(2 + 4))
print(type(2 / 4)) #0.5 = float

#Adding 2 floating numbers together that equal an interger still
#saves as a float ex 9.9 + 1.1

print(2 ** 3) # = 8 (2x2x2)
print(5 // 4) # = 1 (how many times can 4 go into 5)
print(6 % 4) # = 2 (What is left after I take 4 out of 6)

#Math Functions

print(round(3.1)) #rounding a number up or down
print(abs(-20)) #absolute value of a number, no negatives

print(bin(5)) #binary number for 5
print(int('0b101', 2)) #converts a binary number into an integer

iq = 190 # iq is a variable, with a value of 190
print(iq)

user_age = iq / 4
a = user_age
a,b,c = 1,2,3 #easy way to assign multiple variables

#constant
PI = 3.14 # full capital variable names means it is a constant, won't change

#augmented assignment operator
some_value = 5
some_value += 2 # instead of having to call some_value again

#strings
"Hey there"
username = "supercoder"
password = "supersecret"
long_string = '''
Oh WOW
This is crazy!
Really cool
'''
# the 3 single quotes allows for multi line strings
print(long_string)

#from the linux machine!
#with the ssh set up!

#string concatenation and type conversion
print(type(int(str(100)))) #would print out int because it was the last conversion
print("hey" + "There")

#escape sequences, /t at the start gives a tab, /n starts a new line
weather = "\t It\'s \"kind of\" sunny \n hope you have a good day!"
print(weather)

#formatted strings
name = 'Johnny'
age = 55
print('hi ' + name '. You are ' + str(age) + ' year old')
print(f'hi {name}. You are {age} years old') #much cleaner option
print('hi {}. You are {} years old'.format(name, age)) #python 2 function






