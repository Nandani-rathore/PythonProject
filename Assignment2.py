# ------------ question1 : practice calculator using if else elif ----------------

a = int(input("enter first number :"))
b = int(input("enter second number :"))
op = input("enter an operator :")

if op =='+':
    print("output :",a+b)
elif op == '-':
    print("output :",a-b)
elif op == '*':
    print("output :",a*b)
elif op == '/':
    print("output :",a/b)
elif op == '%':
    print("output :",a%b)
else :
    print("Invalid operator or input")

# ---------------------------------------question 2  Grade --------------------------------------------
name = input("enter your name :")
Class = int(input("enter your class :"))
print("enter your 5 Subject Marks :")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
total=a+b+c+d+e
per=total/5
print(f"Name :{name}")
print(f"class :{Class}")
print(f"Total Marks Obtained (out of 500) :{total}")
print(f"Percentage :{per}")

if per >= 60:
    print("Grade A")
elif per >= 50 and per < 60:
    print("Grade B")
elif per >= 40 and per < 50:
    print("Grade C")
elif per >= 33 and per < 40:
    print("Grade D")
else :
    print("Fail")


# ------------------------------------ question3 Factorial -------------------------
result =1
n = int(input("enter a number:"))
for x in range(n,1,-1):
    result=result*x
print(f"the factorial of {n} is :{result} ")


# -------------- question4 billing program -----------------

lists = []
while True:
    print("-------------------- Menu Driven --------------------")

    print("1.Create Bill")
    print("2.Display item price and total bill amount" )
    print("3.Display Total")
    print("4.exit")

    print("------------------------------------------------------")
    choice = int(input("enter your choice :"))
    addition =  0

    if choice == 1:
       print("Creating a new Bill ......")
       while True:
            l = int(input("enter the price of items (-1 to end)"))

            if l == -1:
                print("No item in the Bill.")
                break
            else:
                lists.append(l)
       print("Bill Created Successfully.")

    elif choice == 2:
        if not lists:
            print("No Item in the Bill. Create new bill( Press 1)")

        else :
            print("The Bill is :",lists)

            for x in lists :
              addition += x
            print("Total Sum :",addition)

    elif choice == 3:

        for x in lists:
            addition += x
        print("Total Sum :",addition)

    elif choice == 4:
        print("end of the loop.")
        break



# ------------------------------- question5 ---------------------------------

list = [1,22,3344,56,56,67,6,789,89,55,4332,3]
print(list)
largest = float("-inf")
slargest = float("-inf")
for x in list:
    if x>largest:
        slargest = largest
        largest=x
    elif  x>slargest and x<largest:
        slargest = x

if slargest == float("-inf"):
  print("the largest element in the list is :",largest)
  print(f"the second largest elements is not exits")
else :
  print("the largest element in the list is :",largest)
  print("the second largest element in the list is:",slargest)


# second smallest

mini = float("inf")
smini = float("inf")

for x in list:
    if x<mini:
        smini = mini
        mini = x
    elif x>mini and x<smini:
        smini = x

if smini == float("inf"):
    print("the minimum element is :",mini)
    print("the second minimum element is not exist")

else :
    print("the minimum element is :", mini)
    print("the second minimum element is :",smini)

