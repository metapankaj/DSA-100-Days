#1 Write a program to calculate the sum, difference, product and quotient of two numbers.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

sum = a + b
difference = a - b
product = a * b
quotient = a / b

print("The sum of the two numbers is: ", sum)
print("The difference of the two numbers is: ", difference)
print("The product of the two numbers is: ", product)
print("The quotient of the two numbers is: ", quotient)


#2 Take marks in 5 subjects Maths, English , Science , Social , Computers and print ut the average of marks from five subject marks.

maths = int(input("Enter the marks in Maths: "))
english = int(input("Enter the marks in English: "))
science = int(input("Enter the marks in Science: "))
social = int(input("Enter the marks in Social: "))
computers = int(input("Enter the marks in Computers: "))

average = (maths + english + science + social + computers) / 5
print("The average of the marks is: ", average)


#3 Write a program to compare two numbers and print whether they are equal, greater or smaller.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a == b:
    print("The numbers are equal")
elif a > b:
    print("The first number is greater than the second number")
else:
    print("The first number is smaller than the second number")
    

#4 You are given a variable height.You are allowed to enter the waterpark only if your height is between 5 and 10. Apply the condition and output 1 if the condition is true or 0 if the condition is false.

height = int(input("Enter your height: "))
if height >= 5 and height <= 10:
    print(1)
else:
    print(0)


#5 Rahul and sam are brothers , input their age and find out who is elder one and younger one.

rahul = int(input("Enter Rahul's age: "))
sam = int(input("Enter Sam's age: "))

if rahul > sam:
    print("Rahul is elder than Sam")
else:
    print("Sam is elder than Rahul")
    
#6 Using an assignment operator , assign a value to a variable and find the modulus of that value.

a = 14
b = 3

print(a % b)

#7 Write a program to check if a number is positive or negative.

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive")
else:
    print("The number is negative")
    
#8 Write a program to check if a number is divisible by 5.

num = int(input("Enter a number: "))
if num % 5 == 0:
    print("The number is divisible by 5")
    
else:
    print("The number is not divisible by 5")
    
#9 Write a program to check if a number is prime or not.

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("The number is not prime")
            break
    else:
        print("The number is prime")


#10 Write a program to check if a year is a leap year.

year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year is a leap year")
        else:
            print("The year is not a leap year")
    else:
        print("The year is a leap year")
 