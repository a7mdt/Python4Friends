# Notes :
"""
1- Word (dir) => We use it to know all the functions I can use with something :
myList = []
print(dir(myList))
2- List => []
3- Tuple => ()
4- Dictionary => {}
5- The output of a Set => { ... , ... , ... }
6- To convert something to List , Tuple , Set :
list = [0, 1, 2, 3, 4, 5, 5]
st = set(list)
tp = tuple(list)
lst = list(st)
7- in Files :
----------------------!-----!-------!------!-------!------!-------!
                      !  r  !   r+  !   w  !   w+  !   a  !   a+  !
----------------------!-----!-------!------!-------!------!-------!
read                  !  +  !   +   !      !   +   !      !   +   !
write                 !     !   +   !   +  !   +   !   +  !   +   !
create                !     !       !   +  !   +   !   +  !   +   !
truncate              !     !       !   +  !   +   !      !       !
position at beginning !  +  !   +   !   +  !   +   !      !       !
position at the end   !     !       !      !       !   +  !   +   !
----------------------!-----!-------!------!-------!------!-------!
8- In the Child class you don't use __init__ .
9- name = "Ahmed"
print("my name is " + name) = print("my name is", name) = print(f"my name is {name}")
10- The Difference between args and kwargs that : args=>arguments , kwargs=>keyword arguments.
11- args works like Tuple , kwargs works like Dictionary.
12- args => * , kwargs => ** .
13- Note : when u Write ur for loop u have 3 Cases
for x in kwargs => We will print Keys
for x in kwargs.values() => We will print the values
for x , y in kwargs.items() => We will print keys and values
14- When u write parameters u must write them in this way
( x, y, *args, option=True, **kwargs) ==> u cant write **kwargs before *args or Change this way.
15-
"""

# 8) Strings :
"""
print("1 AhmedTarek")
print("2 Ahmed\nTarek")
print("3 Ahmed\"Tarek")
print("4 Ahmed\tTarek")
myName1 = "AHMEDTAREK"
# Converts to lower chars
print("5 " + myName1.lower())
# Checks the case of ur chars
print(myName1.islower())
print(myName1.lower().islower())
myName2 = "ahmedtarek"
# Converts to upper chars
print("6 " + myName2.upper())
# Checks the case of ur chars
print(myName2.isupper())
print(myName2.upper().isupper())
myName3 = "AhmedTarekMohamedIbrahemElabd"
# Checks the length of a word
print(len(myName3))
print(len("AhmedTarekMohamedIbrahemElabd"))
# Checks the index of specific char
print(myName3.index("T"))
# Printing the char in specific index
print(myName3[0], myName3[5], myName3[10])
myName4 = "AhmedMohamed"
# Replacing text
print(myName4.replace("Mohamed", "Tarek"))
"""

# 9) Numbers :
"""
from math import *
myNum = 5
# if u want to add this (myNum) to text with (+) it must me string , So
# Converting Int to String
print("1 " + str(myNum) + " is my favourite number.")
# Printing the absolute value for a number ==> |5| = 5 , |-5| = 5
print(abs(myNum))
# The power ==> 5^2 = 25
print(pow(myNum, 2))
print(5**2)
# The square root ==>  25 = 5
print(sqrt(25))
# Max and min
print(max(1, myNum, 10, 256))
print(min(1, myNum, 10, 256))
# Rounding a number ==> 3.6 = 4 , 3.4 = 3
print(round(3.6))
print(round(3.4))
# Our Library (Math)
# The floor ==> Removes the point , 3.5 = 3
print(floor(3.5))
print(floor(4.5))
# The ceil ==> It always goes to the next number , 3.5 = 4
print(ceil(3.5))
print(ceil(4.5))
"""

# 10) Getting Inputs :
"""
# note : When u take inputs from a user , U take them as Strings
firstName = input(" 1- Whats ur first name? ")
lastName = input(" 2- Whats ur last name? ")
age = input(" 3- Whats ur age? ")
print("Hello " + firstName + " " + lastName + " ur age is " + age)
"""

# 11) Building a Calculator(1) :
"""
from math import *
num1 = input(" 1- Enter ur first number : ")
num2 = input(" 2- Enter ur second number : ")
Addition = float(num1) + float(num2)
Subtraction = float(num1) - float(num2)
Multiplication = float(num1) * float(num2)
Division = float(num1) / float(num2)
squareRoot1 = sqrt(float(num1))
squareRoot2 = sqrt(float(num1))
n1Power2 = pow(float(num1), float(num2))
n2Power1 = pow(float(num2), float(num1))
print("1- The Addition is : " + str(Addition))
print("2- The Subtraction is : " + str(Subtraction))
print("3- The Multiplication is : " + str(Multiplication))
print("4- The Division is : " + str(Division))
print("5- The Square Root for the first number is : " + str(squareRoot1))
print("6- The Square Root for the second number is : " + str(squareRoot2))
print("7- Number 1 power to Number 2 is: " + str(n1Power2))
print("8- Number 2 power to Number 1 is : " + str(n2Power1))
"""

# 13) Lists(1) :
"""
List1 = [1, "Ahmed", True, "Tarek", 5]
# Printing a list
print(List1)
# Printing an item in a list
print(List1[1])
print(List1[-1])
print(List1[1] + " " + List1[-2])
# Printing Items in a list from .... to .... , Note ==> [1:4] means indexes 1 , 2 , 3
print(List1[1:4])
print(List1[1:-1])
# Printing Items in a list from .... to the end of this list
print(List1[1:])
# Changing a value of specific Index
List1[2] = "is Son of"
print(List1[1] + " " + List1[2] + " " + List1[-2])
"""

# 14) Lists(2) :
"""
oddNums = [1, 3, 5, 7, 9]
evenNums = [2, 4, 6, 8]
# Printing two lists
print("1:", oddNums, evenNums)
# Concatenation two lists
'''oddNums.extend(evenNums)
print(oddNums)
evenNums += oddNums
print(evenNums)'''
# Adding item to a list (It will be added in the last index)
evenNums.append(10)
print("*", evenNums)
# Adding item to a list (It will be added in a specific index) ==> listName.insert(index, item)
oddNums.insert(0, -1)
evenNums.insert(0, -2)
print("2:", oddNums, evenNums)
# Removing item from a list :
evenNums.remove(-2)
oddNums.remove(-1)
print("3:", oddNums, evenNums)
# Removing all items in a list :
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("** Before clearing :", nums)
nums.clear()
print("** After clearing :", nums)
# Removing the last item from a list (I can store it in a Variable)
popingList = ["Ahmed", "Tarek", "Elabd"]
print("*** Before poping :", popingList)
popedItem = popingList.pop()
print("*** After poping :", popingList)
print("*** Poped item :", popedItem)
# Knowing the index of an item (I can store it in a Variable):
print(oddNums.index(1))
print(evenNums.index(10))
# Knowing how many times I have an item in one list :
countList1 = [0, 1, 2, 3, 4]
countList2 = [0, 1, 1, 2, 3]
print("**** Count1 :", countList1)
print("**** Count2 :", countList2)
# Sorting a list with alphabatical order :
sortingList = ["Ahmed", "Mohamed", "Tarek", "Menna", "Fahmy", "Eyad"]
sortingList.sort()
print("***** Sorted list :", sortingList)
# Coping a list (if u change something in the old one , the new one won't care)
oldList = [1, 1, 1, 2, 5, 8, 7]
newList = oldList.copy()
print("****** Old list (before adding) :", oldList)
print("****** New list (Before adding) :", newList)
oldList.append(10)
print("****** Old list (After adding) :", oldList)
print("****** New list (After adding) :", newList)
"""

# 15) Tuples :
"""
# What is the Tuple? It's a List with different brackets and I can't change or Edit in its Items
Coordinates = (10, 20)
listOfCoordinates = [(10, 20), (15.5, 16.7), (-102, 12.6), (0, 16)]
print("1- Printing a Tuple :", Coordinates)
print("2- Printing an Index of a Tuple :", Coordinates[0])
print("3- Printing a List of Tuples :", listOfCoordinates)
print("4- Printing a Tuple in a List of Tuples :", listOfCoordinates[2])
print("5- Printing an Index of a Tuple in a List of Tuples :", listOfCoordinates[2][1])
"""

# 16) Functions(1) :
""""
# The Key Word that I use to write a Function is : def

def sayHello(Name, Age):
    print("Hello Mr." + Name + " You are " + str(Age) + " years old.")

sayHello("Ahmed", 19)
sayHello("Taha", 45)
sayHello("Yasser", 22)
"""

# 17) Functions(2) :
"""
def Addition(num1, num2):
    return num1+num2

def Subtraction(num1, num2):
    subResult = num1-num2
    return subResult

print("Addition = ", Addition(20, 25))
print("Subtraction = ", Subtraction(30, 10))
"""

# 18) Conditions :
"""
# If Statement
isHungryy = True
if isHungryy:
    print("Eat.")
# Note this words in ur Condition : and=>&& , or=>|| , and not , or not.
# If , Else
isHungry = input("Are you Hungry? ")
if isHungry == "yes" or isHungry == "true":
    print("Go eat right now.")
else:
    print("Dont eat.")
# else if ==> elif , Else
print("Choose a number from 1 to 4")
num = input("Enter ur number : ")
if num == "2":
    print("You are a Winner")
elif num == "3":
    print("You are a Winner ,too")
else:
    print("You are a Loser.")
"""

# 19) Comparisons :
"""
def comp(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print("1- Without built in function :", comp(10, 20, 60))
print("2- With built in function :", max(10, 20, 60))
"""

# 20) Building a Calculator(2) :
"""
num1 = float(input(" * Enter ur first number : "))
num2 = float(input(" * Enter ur second number : "))
operator = input(" * Enter ur operator : ")
if operator == '+':
    print("The Addition if this nums = ", num1+num2)
elif operator == '-':
    print("The Subtraction if this nums = ", num1 - num2)
elif operator == '*':
    print("The Multiplication if this nums = ", num1 * num2)
elif operator == '/':
    print("The Division if this nums = ", num1 / num2)
else:
    print("pls enter invaild operator!")
"""

# 21) Dictionaries :
"""
# DictionaryName = { "key1" : "....." , "key2" : "....." , "key3" : "....."} ==> Keys must be UNIQUE
# If u put 2 keys equals themselves , the output will be the last time u use this key
convertMonths = {1: "January", "2": "February", "3": "March", "ap": "April", "5": ["May", "May is the fifth month"]}
# Printing Dictionary
print(convertMonths)
# Printing Item in Dictionary
# You can do this in 2 ways But => The second way is better because u can put default value
print(convertMonths["5"])
print(convertMonths[1])
print(convertMonths.get("2"))
print(convertMonths.get("6", "The value doesn't exist"))
"""

# 22) While Loop :
"""
# Syntax :
#           While condition:
#                print()
#                Updating
i = 1
while i <= 10:
    print(i)
    i += 1
print("======================")
# Continue ==> When ur Condition in the If happens , It will be skipped then the code continues.
j = 0
while j <= 10:
    j += 1
    if j == 6:
        continue
    print(j)
print("======================")
# Break ==> When ur Condition in the If happens , The code will stop at this point.
k = 0
while k <= 10:
    k += 1
    if k == 6:
        break
    print(k)
print("======================")
"""

# 24) For Loop :
"""
# Syntax :
# for (somthing) in (something_else):
#     print(something)
# note : range(x) => will print all the nums from 0 to x-1 , range(x, y) will print all nums from x to y-1 .
for char in "AhmedTarek":
    print(char)
print("======================")
Numbers = [1, 2, 3, 7, 4, 5]
for num in Numbers:
    print(num)
print("======================")
for x in range(10):
    print(x)
print("======================")
for x in range(5, 10):
    print(x)
print("======================")
# Printing Items from A list
myList1 = ["Ahmed", "Menna", "Tarek", "Mohamed"]
for index in range(len(myList1)):
    print(myList1[index])
print("======================")
myList2 = ["Ahmed", 2, "Menna", 10, "Yasser", "Honda", "BMW"]
for index in range(len(myList2)):
    if index == 4:
        break
    print(myList2[index])
print("======================")
# Even and Odd with For Loop
for i in range(10):
    if i % 2 == 0:
        print(i, " is an Even.")
    else:
        print(i, " is an Odd")
print("======================")
"""

# 25) Sets :
"""
# Removing duplicated items from a list
# First way
myList = [1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 7, 9, 8]
notDupList = []
for item in myList:
    if item not in notDupList:
        notDupList.append(item)
print("Without Set :", notDupList)
# Note : The Set is a Tuple but has unique items 
# Second way
uniqueSet = set(myList)
print("With Set :", uniqueSet)
"""

# 26) Power App with (Functions , For Loop) :
"""
def power(baseNum , powNum):
    result = 1
    for i in range(powNum):
        result *= baseNum
    return result
print(power(5, 3))
"""

# 27) 2D Lists , Nested Loops :
"""
# 2D Lists :
my2dList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10]
]
# Printing A full 2D list
print(my2dList[1])
print("======================")
# printing A specific item in a List from 2D List
print(my2dList[1][2])
print("======================")

# Nested Loops :
# Printing A list
for row in my2dList:
    print(row)
print("======================")
# Printing Items from A 2D list
for row in my2dList:
    for column in row:
        print(column)
print("======================")
# Example for the previous Hashtag ==> (Multiplication of this items)
for row in my2dList:
    for column in row:
        print(column*2)
print("======================")
"""

# 29) Python Errors (Try / Except) :
"""
try:
    myNum1 = int(input("Enter ur first number: "))
    myNum2 = int(input("Enter ur second number: "))
    print("Here is the Division of the first number By the second Number :", myNum1 / myNum2)
except ZeroDivisionError as errZeroDivision:
    print("you can't divide by Zero..")
    print(errZeroDivision)
except ValueError as errValue:
    print("Invalid input")
    print(errValue)
# Note : in the except syntax
# except (Case) ==> 1 , if u don't want to pass a case u must but it at the last exception (Default)
# except (Case) as (name) ==> 2 , This [ as (name) ] will print a message from the system about this error.
"""

# 30) Python Reading Files :
"""
# U can use built_in functions with the files :
# 1- r => read
# 2- w => write
# 3- a => append (we will add in the end of the file)
# 4- r+ => read and write
# note : Don't write the type of the file (.txt) for example ==> Line 442
ourProjectR = open(r"C:\\Users\\ahmed tarek\\PycharmProjects\\pythonProject\\30", "r")
ourProjectW = open(r"C:\\Users\\ahmed tarek\\PycharmProjects\\pythonProject\\30", "w")
# (.........).readable() ==> checks if u can read this file or not => True or False (Bool)
print("The Reading File :", ourProjectR.readable())
print("The Writing File :", ourProjectW.readable())
print("======================")
# Read A file
print(ourProjectR.read())
print("======================")
# Read each Line in a file and print it
# note : if u write it again it will go to the next line and print it.
print(ourProjectR.readline())
print("======================")
# Read an specific line in a file (With its Index)
print(ourProjectR.readlines()[1])
print("======================")
# Read A file and puts its items in a list 
# U can make it with for loop :
# for line in ourProjectR.readlines():
#      print(line)
print(ourProjectR.readlines())
print("======================")
"""

# 31) Python Writing Files :
"""
ourProjectW = open(r"C:\\Users\\ahmed tarek\\PycharmProjects\\pythonProject\\30", "w")
ourProjectR = open(r"C:\\Users\\ahmed tarek\\PycharmProjects\\pythonProject\\30", "r")
# Add item in a File :
ourProjectW.write( "1) The Project : Animal Shelter \n"
                   "2) Team Members : Ahmed Tarek , Menna Salem , Shahd Samir and Rwan Matter\n"
                   "3) Data Base : Ahmed Tarek and Shahd Samir\n"
                   "4) PyQt : Menna Salem and Rwan Matter\n"
                   "5) Python : Ahmed , Menna , Shahd and Rwan\n"
                   "*) =======================================\n")
# WriteLines :
projectLines = ["1) The Project : Animal Shelter \n"
                   "2) Team Members : Ahmed Tarek , Menna Salem , Shahd Samir and Rwan Matter\n"
                   "3) Data Base : Ahmed Tarek and Shahd Samir\n"
                   "4) PyQt : Menna Salem and Rwan Matter\n"
                   "5) Python : Ahmed , Menna , Shahd and Rwan\n"
                   "*) =======================================\n"]
ourProjectW.writelines(projectLines)
ourProjectW.write("6) Project instructor : Dr Amr AboHany")
ourProjectW.write("\n7) Project instructor : Eng Nada Nassef")
ourProjectW.close()
ourProjectR.close()
"""

# 32) Modules :
"""
There isn't codes to write but Search for this topic again!
"""

# 33) Classes and Objects :
"""
# Calling class ==> from (fileName) import (className)
from class33_Employee import Employee

emp1 = Employee("Ahmed", 19, "Cairo", True)
emp2 = Employee("Tarek", 25, "Alexandria", False)

print(emp1.age, emp2.age)
print("Is " + emp1.name + " is Manager?" + " " + str(emp1.isManager))
print(emp2.department)
"""

# 34) Class Functions :
"""
from class33_Employee import Employee
emp1 = Employee("Ahmed", 19, "Cairo", True, 5, 8500)
emp2 = Employee("Tarek", 36, "Alexandria", False, 3.5, 500)
emp3 = Employee("Rana", 55, "Tanta", False, 2.5, 700)
emp4 = Employee("Fahmy", 59, "Banha", False, 1.5, 1500)
emp5 = Employee("Menna", 46, "KFS", False, 4.5, 5500)
print("Excellence : ", emp1.isExcellent())
print("Excellence : ", emp2.isExcellent())
print("1) Salary Before Bonus for Emp1 :", emp1.salary, "\n", "Salary After Bonus for Emp1 :", emp1.bonusLvL())
print("2) Salary Before Bonus for Emp2 :", emp2.salary, "\n", "Salary After Bonus for Emp2 :", emp2.bonusLvL())
print("3) Salary Before Bonus for Emp3 :", emp3.salary, "\n", "Salary After Bonus for Emp3 :", emp3.bonusLvL())
print("4) Salary Before Bonus for Emp4 :", emp4.salary, "\n", "Salary After Bonus for Emp4 :", emp4.bonusLvL())
print("5) Salary Before Bonus for Emp5 :", emp5.salary, "\n", "Salary After Bonus for Emp5 :", emp5.bonusLvL())
"""

# 35) Inheritance :
"""
from class35_Parent import Cars
from class35_Child import newCar

c1 = Cars()
c2 = newCar()

c1.brand()
c1.speed()
c2.brand()
c2.speed()
c2.myModel()
"""

# 38) Dunder Functions :
"""
I saw 17 mins..
# What is the meaning of word (dunder)
# __(.....)__ ==> Double UnderScore before and after
# so D=>Double , under=>UnderScore.
# We can call them : Dunder, Magic methods, magic functions.

class Order:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

# if we tried to remove the next Function and in the print line we wrote print(len(o1)) we will get Error.

    def __len__(self):
        return len(self.cart)

# if we tried to call an Object without writing the next Function we will get error

    def __call__(self):
        print(f"My name is {self.customer}")

# We choose with the next method what we well get if we tried to print an Object

    def __str__(self):
       return f"Customer {self.customer} Bought {self.cart}"

# __len__
o1 = Order(["LapTop", "Keyboard", "Wires"], "Ahmed Tarek")
print("The length of Object(o1) :", len(o1))

# __call__
o1()

# __str__
print(o1)
"""

# 40) Converting a Python File to .EXE :
"""
# By default the python File is .PY => U want to convert it to .EXE
-The Steps (1): 
1- Go to the Folder that has the .PY File
2- press (Shift) + Right Click by the mouse
3- Choose => Open PowerShell window here
4- Write => pip install pyinstaller
5- press (Enter)
6- Write => pyinstaller --onefile '(filename).py' 
7- press (Enter)
8- U will find a new file called (dist)
9- Go to it and u will find ur (filename).exe
-The Steps (2):
1- Go to the Folder that has the .PY File
2- press (Shift) + Right Click by the mouse
3- Choose => Open PowerShell window here
4- Write => pip install auto-py-to-exe
5- When it has been installed u will write auto-py-to-exe
6- U will choose the (Path) and the second option U will choose (One File) 
7- Keep all other options (U can change the OutPut Directory from the Settings)
8- press the convert button in the end of the window 
"""

# 41) Python Args :
"""
# What will u do if u pass 2 parameters to a Function then give it 3 arguments ? => It will give me TypeError
# So how Can I solve this problem ?

# 1

def sumList1(myList1):
    result1 = 0
    for x in myList1:
        result1 += x
    return f"The Result is {result1}"

myList1 = [1, 2, 3, 4, 5]
print(sumList1(myList1))

print("=============================")

#2
# U can remove the word (args) and make it anything like (ahmed),(ints) 
# But u must put (*) ==> It works like a tuple

def sumList2(*args):
    result2 = 0
    i = 0
    for i in args:
        result2 += i
    return f"{i-1} The Result is {result2}"

print(sumList2(1, 2))
print(sumList2(1, 2, 3,))
print(sumList2(1, 2, 3, 4))
print(sumList2(1, 2, 3, 4, 5))
"""

# 42) Python Kwargs :
"""
# The concept of it :
def mySum(a, b, *args, flag=True):
    result = 0
    if flag:
        for x in args:
            result += x
        return  a + b + result
    else:
        return result

# The parameter flag here ie keyword => I choose what will happen because of the condition of this keyword
# note : if I haven't Write the keyword (flag) as argument it will be By default like my parameter.

print(mySum(1, 2))
print(mySum(1, 2 , flag=False))
print(mySum(1, 2, 3, 4, 5, 6, 7 ))
print(mySum(1, 2, 3, 4, 5, 6, 7, flag=False))

print("=============================")

# Note : when u Write ur for loop u have 3 Cases
# for x in kwargs => We will print Keys
# for x in kwargs.values() => We will print the values
# for x , y in kwargs.items() => We will print keys and values

def studentDetails(**kwargs):
    for key , value in kwargs.items():
            print(f"{key} : {value}")

studentDetails(name="Ahmed", age="19", GPA="3.8", Department="CS")
print("-----------------------")
studentDetails(name="Mohamed", age="22", GPA="2.0" )
print("-----------------------")
studentDetails(name="Honda", age="23", GPA="3.2", Department="IS")
print("-----------------------")
studentDetails(name="Yasser", age="20", GPA="3.1", Department="IT")
print("-----------------------")
studentDetails(name="Tarek", age="21", GPA="2.7" )
"""

# 43) Python Unpacking Operators :
"""
# it means the * and ** Before args and kwargs
# The Concept
myList = [1, 2, 3, 4]
print("Without * ==>", myList)
print("-----------------------")
print("With * ==>", *myList)
print("=============================")
def mySum1(x, y, z):
    print(x+y+z)
# if we make myList = [1, 2, 3, 4] it will give me Error because I have only 3 parameters
myList = [1, 2, 3]
mySum1(*myList) # = mySum1(1, 2, 3)
print("=============================")

def mySum2(*args):
    result = 0
    for x in args:
        result += x
    return result

myList1 = [1, 2, 3]
myList2 = [4, 5, 6]
myList3 = [7, 8, 9]
print(mySum2(*myList1, *myList2, *myList3)) # = mySum(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("=============================")

# APPS :

abcdList = [1, 2, 3, 4, 5, 6, 7, 8]
a, *b, c, d = abcdList
print(a)
print(b)
print(c)
print(d)
print("=============================")

myFirstList = [1, 2, 3, 4]
mySecondList = [5, 6, 7, 8]
mySecondList.append(9) # it will be in the Second and Merged Lists 
myMergedList = [*myFirstList, *mySecondList]
myFirstList.insert(0, 0) # it will be in the First list, only
print(myFirstList)
print(mySecondList)
print(myMergedList)
print("=============================")
"""
