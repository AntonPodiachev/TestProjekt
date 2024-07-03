"""
sum = 0
while a <= 100:
    print(a)
    sum = sum + a
    a = a + 1
    print(sum)
"""


"""
par = "sos"
user_par =""
index =5
while user_par != "par"
"""
"""
userInput1 = int(input("Enter first number\t "))
userInput2 = int(input("Enter second number\t"))
while  userInput1 <=  userInput2:
    if userInput1 % 2==0:
       print( userInput1 )
       break
    userInput1 += 1
"""
"""
userInput1 = int(input("Enter first numbes\t "))
userInput2 = int(input("Enter second numbes\t "))
userEnter = 0
while True:
    if userInput1 >= 0:
        break
         userEnter +=
             print(userEnter)
"""
"""
a = int(input("Enter first number\t "))
b = int(input("Enter second number\t "))
c = a + b
while True:
    print(c)
    if c > 100:
        print("Program ended")
    if a == 0 or b == 0:
        print("Program ended")
    break
"""
"""
sum = 0
for i in range(101):
    if i % 2 == 0:
        sum += i
        print(sum)
    """
"""
for i in range(11): # i =0

    for j in range(11): #j=1
        if i>=j:
            print("*  ", end="")

    print()
"""
"""
for i in range(11):

    for j in range(11):
        if i + j == 10:
            print("*  ", end=" ")
        else:
            print("\t", end =" ")


    print()

"""
"""
randNumber = random.Randomrandint(0,100)

step = 0

while True:
    userInput=int(input("Enter your number from 0 to 100: \t"))
    step+=1
    if userInput == randNumber :
        print(f"YOU WIN, your try {step}")
        break
    elif userInput < randNumber:
        print("Rand number more than your")
    elif userInput > randNumber :
        print("Rand number less than your")
    elif userInput <0 or userInput > 100:
        print("Try another number")
"""
"""
import random
randnom1 = 0
random2 = 0
for _ in range(100 ):
   rund = random.randint(0,1 )
   if rund ==0:
       random2 +=1
   elif rund ==1:
      randnom1 +=1
if  random2  > randnom1:
    print("Решка")
else:
    print("Орел")
"""
""" Завдання перше
"""

"""
while True:
    a = int(input("Enter first number\t"))
    b = int(input("Enter second number\t"))
    c = a + b
    print(c)
    break
if a == 0 or b == 0:
    print("stop")
elif c > 100:
    print("stop")
"""
"""

    if a == 0 or b == 0:
        break
        print("stop")
    elif c > 100:
        break
        print("stop")

a = 0
while a <=100:
    print(a)
    a = a + 1
"""

program_ask = int(input("Enter your age:0-120 \t"))
b = 0
while b >= 120:
    if b == program_ask:
        break
    else:
        b = b + 1
        print(b)



























































