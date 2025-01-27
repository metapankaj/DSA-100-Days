#1 Take a number and return "ODD" if the number is odd and "EVEN" if the number is even.without using function

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("EVEN")
else:
    print("ODD")

#2 Find out if the age is greater than or equal to 18 and return "Adult" if it is, otherwise return "Minor".

age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")
    
#3 Take an integer and return "YES" if the input is divisible by 3 or 5, otherwise return "NO" in all other cases.

num = int(input("Enter a number: "))
if num % 3 == 0 or num % 5 == 0:
    print("YES")
else:
    print("NO")
    

#4 Take an integer ranging from 0-6 as input and print out the corresponding weekdays. 0 corresponds to Sunday and 6 to Saturday.

day = int(input("Enter a number between 0-6: "))

if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
else:
    print("Please enter a number between 0-6")
    

#5 Check if a number is even or odd and print it out using a match statement.

num = int(input("Enter a number: "))
match num:
    case _ if num % 2 == 0:
        print("EVEN")
    case _:
        print("ODD")
        
#6 Write a program to check whether a number is positive, negative, or zero.

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    
#7 Write a program to input any character and check whether it is an alphabet, digit, or special character.

char = input("Enter a character: ")
if char.isalpha():
    print("Alphabet")
elif char.isdigit():
    print("Digit")
else:
    print("Special Character")
    
    
#8 Write a program to input any character and check whether it is a vowel or consonant.

char = input("Enter a character: ")
if char in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
    
