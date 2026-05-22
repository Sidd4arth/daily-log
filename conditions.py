a= int(input("Enter a number: "))

if a>0:
    print("a is positive")
else:
    print("a is not positive")  


###
#If Elif Else
age=int(input("enter your age: "))
if age<0:
    print("age cannot be negative")
elif age<18:
    print("you are a minor")
elif age<65:
    print("you are an adult")
else:
    print("you are a senior citizen")