# Python Operators Practice Questions.
#Part A: Arithmetic Operators (+, -, *, /, %, //, **).
'''
#Q1.Take two numbers from the user and print their sum.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=a+b
print("The sum of two numbers is:",c)
#Q2.Take two numbers and print:
#Addition
#Subtraction
#Multiplication
#Division
a=25
b=15
c=a+b
print("Addition =",c)
c=a-b
print("Subtraction =",c)
c=a*b
print("Multiplication =",c)
c=a/b
print("Division =",c)
#Q3.Find the remainder when 25 is divided by 4.
a=25
b=4
c=a%4
print("the reminder is:",c)
#Q4.Find the quotient using floor division of 25 by 4
a=25
b=4
c=a//4
print("the reminder is:",c)
#Q5.Calculate 5 raised to the power of 3.
a = 5
b = a ** 3
print("5 raised to the power of 3 is:", b)
#Q6.Input the length and width of a rectangle. Find its area.
length=int(input("Enter the length of rectangle in cm:"))
width=int(input("Enter the width of rectangle in cm:"))
area=length*width
print("area of rectangle = ",area,"cm^2")
#Q7.input the radius of a circle and calculate its area. (Use 3.14 as π.)
radius=float(input("enter the radius of circle:"))
area=3.14*radius*radius
print("area of circle =",area)
#Q8.Input three numbers and calculate their average.
num1=int(input("enter the first number :"))
num2=int(input("enter the second number :"))
num3=int(input("enter the third number :"))
avg=(num1+num2+num3)/3
print("average of three number = ",avg)
#9.Convert total seconds into minutes and remaining seconds.
Time=int(input("enter the seconds:"))
minute=Time//60
second=Time%60
print("conversion = ",minute,"minutes",second,"second")
#10.Swap two numbers without using a third variable.
a=5
b=8
a,b=b,a
print("swap of two numbers:",a,b)

#Part B: Comparison Operators (==, !=, >, <, >=, <=).
#Q11.Check whether two numbers are equal.
a=5
b=6
print("check weather both equal or not :",a==b)
#12.Check whether one number is greater than another.
a=56
b=76
c=a>b
print("a is grater then b :",c)
#13.Check whether a number is less than or equal to 100.
num=int(input("Enter the number:"))
check=num<=100
print("is the number less or greater then 100:",check)

# Assignment Operators (=, +=, -=, *=, /=, %=)
#14.Assign 20 to a variable and print it.
a=20
print(a)
#15.Assign 50 to a variable. Increase it by 15 using +=
a=50
a+=15
print(a)
#16.Assign 100 to a variable. Decrease it by 30 using -=.
a=100
a-=30
print(a)
#17.Assign 8 to a variable. Double its value using *=.
a=8
a*=8
print(a)
#18.Assign 90 to a variable. Divide it by 3 using /=
num=90
num/=3
print(num)
#19.Assign 27 to a variable. Find the remainder when divided by 5 using %=.
num=27
num%=5
print(num)
#     Logical Operators (and, or, not)
#     Only print the Boolean result. No if-else.
#20.Print the result of:
10 > 5 and 8 < 12
#Ans= True
#21.Print the result of:
15 < 10 or 20 > 15
#Ans= True
#22.Print the result of:
not(10 > 5)
#Ans= False.
#23.Take two numbers and print:
num1=int(input("Enter the first number:"))
num2=int(input("enter the second number"))
c=num1 > num2 and num1 != num2
print(c)
#24.Take two numbers and print:
num1=int(input("Enter the first number:"))
num2=int(input("enter the second number"))
c=num1 == num2 or num1 > num2
print(c)

         #Membership Operators (in, not in)
#25.Create a string "Python Programming" and check whether "Python" is in it.
str='python programming'
print('python' in str)
#26.Create a list:Check whether 30 is in the list.
num=[10, 20, 30, 40, 50]
print(30 in num)
#26.Check whether 100 is not in the above list.
num=[10, 20, 30, 40, 50]
print(100 in num)
#27.Create a string with your name and check whether the first letter is present in it.
str='anupam kumar'
print(str[0]in str)

             # Identity Operators (is, is not)
#28.Create
a = 10
b = 10
print(a is b)
#29.create.
x = [1, 2, 3]
y = [1, 2, 3]
x == y
print(x is y)
#30.create.
m = [5, 6]
n = m
print(m is n)
#31.Take your name and print it three times using an operator.
str='anupam kumar'
print((str + '\n')*3)
#32.take a number and multiply it by 10 using *=.
a=56
a*=10
print(a)
#33.take a string from the user and check whether "a" is in that string.
str=input("enter the name")
print('a' in str)
#34.Write a program that prints the value of
a=(10 + 5) * 2 - 8 / 4
print(a)
'''
