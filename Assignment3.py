# ------------------- ques1 ----------------

def my_add(a,b) :
    add = a+b
    print("the sum of 2 number is :",add)

def my_sub(a,b) :
    sub = a-b
    print("The subtraction of 2 number is :",sub)

def my_mul(a,b) :
    mul = a*b
    print("The Multiplication of 2 number is :",mul)

def my_div(a,b) :
    div = a/b
    print("The division of 2 number is :",div)


while True :
    print("--------------- Menu Driven ----------------")
    print("1.addition")
    print( "2.subtraction")
    print( "3.multiplication")
    print("4.division")
    print("5.Exit")
    print("----------------------------------------------")
    choice = int(input("enter your choice :"))

    if choice == 1:
        a = int(input("enter first number:"))
        b = int(input("enter second number:"))
        my_add(a,b)

    if choice == 2:
        a = int(input("enter first number:"))
        b = int(input("enter second number:"))
        my_sub(a,b)

    if choice == 3:
        a = int(input("enter first number:"))
        b = int(input("enter second number:"))
        my_mul(a,b)

    if choice == 4:
        a = int(input("enter first number:"))
        b = int(input("enter second number:"))
        my_div(a,b)

    if choice == 5:
        print("exit from the loop.")
        break


# ------------------------------------ question 2 Palindrome ------------------------

def check_palindrome(n) :

    original = n
    rev = 0
    while int(n) != 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = int(n / 10)

    if rev == original:
        print(f"Number is Palindrome")
    else:
        print(f"Number is not palindrome")


n = int(input("enter a number:"))
check_palindrome(n)


# ----------------------- Billing question implement by using Dictionary --------------------
bill = {}
while True :
    print("-------------------- Menu Driven -----------------")
    print("1.create a Bill")
    print("2.display bill item and there price")
    print("3.display total price")
    print("4.Exit")
    print("---------------------------------------------------")
    choice = int(input("enter your choice:"))

    if choice == 1:
        while True :
            x = input("enter the item name first(-1 for exit)):")

            if x == '-1':
                print("end of the Loop")
                break
            else :
                y = int(input("enter price :"))
                bill[x] = y
                print("Item entered successfully")
    elif choice == 2:
        if not bill :
            print("Bill is empty")
        else:
            print("the Bill is :",bill)
            print("Total Items are:",bill.keys())
            print("prices are :",bill.values())
    elif choice == 3:
        addition = sum(bill.values())
        print("Total amount of all the items is :",addition)
    elif choice == 4:
        print("end of the loop.")
        break
    else:
        print("invalid Choice Entered .")




# ------------------------- Create a game Rock , paper , scissor -------------------------------

import random
comp_points = 0
user_points = 0
options = {1:"rock" , 2:"paper" , 3:"scissor" ,4:"exit"}
while True:
    print("\n----------------- Game -------------------")
    print("1.Rock")
    print("2.Paper")
    print("3.scissor")
    print("4.End the Game")
    print("------------------------------------------")

    user_choice = int(input("Choose one option:\nyour choice is :"))

    if user_choice not in options :
        print("Invalid choice")
        print("choose a valid choice")
        continue

    if user_choice == 4:
        print("\n------------- Final Result ---------------")
        print("your points :",user_points)
        print("computer points",comp_points)
        if user_points > comp_points:
            print("You Win !")
        elif user_points < comp_points:
            print("computer Win !")
        else:
            print("Draw , Play again")
        break
    comp_choice = random.randrange(1,4,1)

    print("your choice is :", options[user_choice])
    print("computer choice is :",options[comp_choice])

    if user_choice == comp_choice:
        print("Draw round !")
        user_points += 1
        print("your points :", user_points)
        comp_points+=1
        print("computer points :",comp_points)


    elif user_choice == 1 and comp_choice == 3 or user_choice == 2 and comp_choice == 1 or user_choice == 3 and comp_choice == 2 :
        print("you Win this round !")
        user_points+=2
        print("your points :", user_points)
        print("computer points :", comp_points)

    else:
        print("computer Win this round !")
        comp_points+=2
        print("your points :", user_points)
        print("computer points :", comp_points)





