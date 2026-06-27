"""
#1.find the area of rectangle.
length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
area=length*breadth
print("area of rectangle=",area)
#2.Area of circle.
radius=float(input("enter the given radius:"))
area=3.14*radius*radius
print("area of circle=",area)
#3.Find area of square.
side=int(input("enter the side of square:"))
area=side*side
print("area of square=",area)
#4.Find the cube of any number.
side=int(input("enter the side of cube:"))
cube=side*side*side
print("cube of any no=",cube)
#5.Find Area of Traingle.
base=float(input("enter the base of traingle:"))
height=float(input("enter the height of traingle:"))
area=0.5*base*height
print("area of traingle=",area)
#6.Enter any 5 different subjects marks at run time & find out aggregate marks & average marks of each subject out of 100 marks.
sub1=float(input("enter the result of first subject:"))
sub2=float(input("enter the result of second subject:"))
sub3=float(input("enter the result of third subject:"))
sub4=float(input("enter the result of fourth subject:"))
sub5=float(input("enter the result of fifth subject:"))
aggregate=(sub1+sub2+sub3+sub4+sub5)
average=(sub1+sub2+sub3+sub4+sub5)/5
print("the aggregate of five subject in 500 =",aggregate)
print("the average of five subject in 500 =",average)
#7.Enter any basic salary of an employee at run time & find DA,HRA,TA,NET SALARY.
#DA=10% Of basic salary.
#HRA=20% Of basic salary.
#TA=5% Of basic salary.
salary=int(input("Enter the Employe basic salary:"))
DA=10/100*salary
HRA=20/100*salary
TA=5/100*salary
net_salary=salary+DA+HRA+TA
print("the DA of basic salary is:",DA)
print("the HRA of basic salary is:",HRA)
print("the TA of basic salary is:",TA)
print("the net_salary of basic salary is:",net_salary)
#8.Enter any no.of days at run time & find out. how many months & how many remaining days?.
Days=int(input("Enter the no of days:"))
Month=Days//30
remaning_days=Days%30
print(Month,"month(s) and",remaning_days,"day(s)")
#9.Enter any temp. at run time in Fahrenheit and convert into celcius?
Fahrenheit=int(input("Enter any Fahrenheit tempture:"))
Celcius=(Fahrenheit-32)*5/9
print("Celius =",Celcius,"c")
#10.Enter any temp. at run time in celcius and convert into Fahrenheit?
Celcius=int(input("Enter any Celcius tempture:"))
Fahrenheit=(Celcius*9/5)+32
print("Fahrenheit =",Fahrenheit,"c")
"""