keepgoing = True
import time
while (keepgoing == True):
    num1 = int(input("1st number: "))
    num2 = int(input("2nd number: "))
    print(" 1 = Multiply\n 2 = Add\n 3 = Divide\n 4 = Subtract")
    act = int(input("What would you like to do? "))
    if act == 3:
        print("Your answer is: " + str(num1 / num2))
    elif act == 1:
        print("Your answer is: " + str(num1 * num2))
    elif act == 2:
        print("Your answer is: " + str(num1 + num2))
    elif act == 4:
        print("Your answer is: " + str(num1 - num2))
    keepgoing = int(input("Continue? \n 1 = Yes\n 0 = No\n"))
print(" Goodbye")
time.sleep(1.5)

