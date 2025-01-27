#1. Write a Python Program to exchange the values of two numbers without using a temporary variable.

a = 5
b = 10

print("Before swapping: a =", a, "b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, "b =", b)

#2. Write a python program that reads a name and age from the user and prints a message stating "Hello {name} , you are {age} years old"

name = input("Enter your name: ")
age = input("Enter your age: ")


print("Hello", name, ", you are", age, "years old")

#3. Write a Python Program to determine if a variable is a string,interger or a float using type() function.

a = 5
b = 5.5
c = "Hello"

print(type(a))
print(type(b))
print(type(c))


#4. Write a Python Program to swap the values of two variables without using a third variable.

a = 5
b = 10

a,b = b,a

print("The value of a is ", a)
print("The value of b is ", b)

#5. Write a Python Program to check if a number is odd or even.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")
    
