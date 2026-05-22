string='string'
print(string)   

#concatination
a='2'
b='4'
print(a+b)

#indexing
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
print(language[3])

#slicing
language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

#reverse a string
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH

language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto (skips every 2nd character)


#sting methods

abc='abcalphabet'
print(abc.capitalize)

print(abc.upper()) # ABCALPHABET
print(abc.lower()) # abcalphabet
print(abc.count('a')) # 4

