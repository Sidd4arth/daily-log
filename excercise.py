#Declare your age as integer variable
age=20
print(age)
#Declare your height as a float variable
height=6.1
print(height)
#Declare a variable that store a complex number
complex_no=2+5j;
print(complex_no)


#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
input_base=input("Enter the base of the triangle:\n"
                 )
input_height=input("Enter the height of the triangle:\n"
                   )
area=0.5*float(input_base)*float(input_height)
print("The area of the triangle is:", area)

#Write a Python script that displays the following table
#1- 1 1 1 1
#2- 1 2 4 8 
#3- 1 3 9 27
#4- 1 4 16 64       
#5- 1 5 25 125


for i in range(1,6):
    print(i,1,i**2, i**3)