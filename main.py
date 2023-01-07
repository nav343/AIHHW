# All imports are up here, at the top
from os import system # clearing the screen (at the end)
from time import sleep # waiting before clearing the screen
from random import  randint, random, choice # answer 15

# Color ASCII values for making the prints and inputs look pretty
blue = '\033[0;34m'
red = '\033[0;31m'
yellow = '\033[1;33m'
green = '\033[0;32m'
noColor = '\033[0m'

# All the answers ("ans" followed by the question number, like ans1 = answer of 1st question)
def ans1():
    print(blue + "Question 1: Write a program to input a WELCOME message and display it\n" + noColor)
    name = input(yellow + 'Enter your name: ')
    print(green + "Welcome " + name + noColor)

def ans2():
    print(blue + "Question 2: Write a program that accepts radius of a circle and prints its area\n" + noColor)
    radius = float(input(yellow + "Enter the radius: "))
    res = 3.14 * radius**2
    print(green + f"Area = {res}㎡" + noColor)

def ans3():
    subIdx = 0 
    print(blue + "Question 3: Write a program that inputs a student's marks in 3 subjects (out of 100) and prints the % marks\n" + noColor)
    marks:dict[str, int | float | None] = {'sub1': None, 'sub2': None, 'sub3': None}

    for i in range(1, 4):
        marks[f'sub{i}'] = float(input(yellow + f"Enter the mark of Subject {i}: "))

    for _ in marks:
        subIdx +=1
        print(green + f"Percent of Subject{subIdx}: {marks[f'sub{subIdx}']}%")

    res = (marks['sub1'] + marks['sub2'] + marks['sub3'])/3
    print(green + f"Overall %: {res}" + noColor)

def ans4():
    print(blue + "Question 4: Write a program that reads the number n and print the value of n^2, n^3 and n^4\n" + noColor)
    number = float(input(yellow + "Enter the base: "))
    for i in range(2,5):
        print(green + f"{number}^{i}: {number**i}" +noColor)

def ans5():
    print(blue + "Question 5: Write a program to calculate the simple interest\n" + noColor)
    p = float(input(yellow + "Principal: "))
    r = float(input(yellow + "Rate: "))
    t = float(input(yellow + "Time: "))
    res = (p * r * t)/100
    print(green + f"Simple Interest with \nP = {p}\nR = {r}\nT = {t}\n==> {res}")

def ans6():
    print(blue + "Question 6: Write a program to input length and breadth of a rectangle and calculate its area\n" + noColor)
    length = float(input(yellow + "Length: "))
    breadth = float(input(yellow + "Breadth: "))
    print(green + f"Area = {length * breadth}㎡")

def ans7():
    print(blue + "Question 7: Write a program to obtain temperature in Celsius and convert it into Fahrenheit\n" + noColor)
    # F = C * (9/5 + 32)
    c = float(input(yellow + "Enter the temperature in Celsius: "))
    print(green + f"{c}°C = {c * 9/5 + 32}°F" + noColor)

def ans8():
    print(blue + "Question 8: Write a program to read details like name, class, age of a student and then print the detail in same line and then in separate lines\n" + noColor)
    name = input(yellow + "What's your name? ")
    _class = input(yellow + "What class are you studying in? ")
    age = input(yellow + "How old are you? ")
    
    print(yellow + "Single Line:" + noColor)
    print(green + f"My name is: {name}, I'm in : {_class}th, and I am: {age} years old !!")

    print()
    print()
    print(yellow + "Multiple Lines:" + noColor)
    print(green + f"My name is: {name}\nI'm in : {_class}th\nand I am: {age} years old !!")

def ans9():
    i= 0
    print(blue + "Question 9: Write a program to enter a number and check if it is a prime number or a composite number.\n" + noColor)
    while i != 6:
        num = int(input(yellow + "Enter a number: "))
        for i in range(2, num//2+1):
            if num%i == 0:
                print(green + f"{num} is a composite number.")
                break
        else:
            print(green + f"{num} is a prime number.")
        i += 1

def ans10():
    print(blue + "Question 10: Write a program to display the n terms of Fibonacci series\n" + noColor)
    n = int(input(yellow + "Enter the range number: "))
    a = 0 
    b = 1 
    if n == 1:
        print(green + f"{a}" + noColor)
    else:
        print(green + f"{a, b}")
        for _ in range(2,n):
            c = a + b
            a = b
            b = c
            print(green + f'{c}' + noColor)

def ans11():
    print(blue + "Question 11: Write a Program to input a number is perfect number, an Armstrong number or a palindrome.\n" + noColor)
    while True:
        num = int(input(yellow + "Number: "))
       
        # Perfect Numbers
        divs = [1] 
        for i in range(2, num):
            if num%i == 0:
                divs.append(i)
        if (sum(divs) == num & num != 1):
           print(green + f"{num} is a Perfect number")
        else:
            print(red + f"{num} is not a Perfect number")

        # Armstrong numbers
        length = len(str(num)) 
        arr = [] 
        finalNum = int()

        for i in str(num):
            j = int(i)
            res = j**length
            arr.append(res)
        for j in arr:
            finalNum += j
        if (finalNum == num):
            print(green + f"{num} is an Armstrong Number")
        else:
            print(red + f"{num} is not an Armstrong Number")

        # Palindrome
        palNum = str(num)[::-1]
        if (int(palNum) == num):
            print(green + f"{num} is a Palindrome" + noColor)
        else:
            print(red + f"{num} is not a Palindrome" + noColor)
    

def ans12():
    print(blue + "Question 12: Write a program to input 2 numbers and display the largest/smaller number\n" + noColor)
    nums = [float(input(yellow + "Number 1: ")), float(input(yellow + 'Number 2: '))]

    if nums[0] == nums[1]:
        print(green + "They are the same" + noColor)
    else:
        print(green + f"{max(nums)} is greater than {min(nums)}")
        print(green + f"{min(nums)} is less than {max(nums)}" + noColor)

def ans13():
    print(blue + "Question 13: Write a program to input 3 integers and display the largest/smaller number\n" + noColor)
    nums = [int(input(yellow + "Number 1: ")), int(input(yellow + 'Number 2: ')), int(input(yellow + 'Number 3: '))]

    if (nums[0] == nums[1] == nums[2] or 
        nums[0] == nums[1] or 
        nums[1] == nums[2] or 
        nums[0] == nums[2]):
        print(green + "They are the same" + noColor)
    else:
        print(green + f"Largest number among {nums} is: {max(nums)}")
        print(green + f"Smallest number among {nums} is: {min(nums)}" + noColor)

def ans14():
    Animals = ['cat', 'dog', 'mouse', 'hamster']
    print(blue + "Question 14: Write a program to take a list of items and print each item in the list using for loop\n" + noColor)
    for animal in Animals:
        print(green + f"Animal is: {animal}" + noColor)

def ans15():
    print(blue + "Question 15: Write a program to create a list namely 'test' having at least 3 integers,2 floating point numbers and 2 strings\n" + noColor)
    test = []
    for _ in range(0,3):
        test.append(randint(0, 100))
    for _ in range(0,2):
        test.append(random())
    for _ in range(0,2):
        test.append(choice([
            'Monkey', 
            'Po/Lotus', 
            'Viper', 
            'Tigress', 
            'Crane', 
            'Master Ogway', 
            'Master Shifu', 
            'Kai', 
            'Lord Shen', 
            'Tai Lung']))
    print(green + f"Test List = {test}" + noColor)

# Running and clearing the console
for i in range(11, 12):
    try:
     system('clear')
     exec(f"ans{i}()")
     sleep(5000)
     system('clear')
    except KeyboardInterrupt:
        system('clear')
