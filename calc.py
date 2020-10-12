#import time module
import time

#set username
usr = "gabbitasm"

#set password
pwrd = "2002"

#ask for username
checkusr = input("Username: ")

#compare with stored username
#if username is wrong retry
while checkusr != usr:
    checkusr = input(str("Incorrect. Please try again: "))
    
#if not check ask for password
checkpass = input("Password: ")

#if password is wrong retry
while checkpass != pwrd:
    checkpass = input(str("Incorrect. Please try again: "))
    
#if not print login successful!
print("Login successful!")

#wait for 1 second
time.sleep(1)

####################################

#turn on keepgoing
keepgoing = True

#if keepgoing is on ask for 2 numbers
while (keepgoing == True):
    num1 = int(input("1st number: "))
    num2 = int(input("2nd number: "))
    
    #ask if you want to *\+-
    print(" 1 = Multiply\n 2 = Add\n 3 = Divide\n 4 = Subtract")
    act = int(input("What would you like to do? "))
    
    #depending on what you choose follow with appropriate action
    if act == 3:
        print("Your answer is: " + str(num1 / num2))
    elif act == 1:
        print("Your answer is: " + str(num1 * num2))
    elif act == 2:
        print("Your answer is: " + str(num1 + num2))
    elif act == 4:
        print("Your answer is: " + str(num1 - num2))
        
        #ask if they would like to keep going and update keepgoing appropriately
    keepgoing = int(input("Continue? \n 1 = Yes\n 0 = No\n"))
    
#goodbye and wait one second
print(" Goodbye")
time.sleep(1)