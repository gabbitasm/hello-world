num1 = int(input("1st number: "))
num2 = int(input("2nd number: "))
print(" 1 = Multiply\n 2 = Add\n 3 = Divide\n 4 = Subtract")
act = int(input("What would you like to do? "))
if act == 3:
    print(num1 / num2)
elif act == 1:
    print(num1 * num2)
elif act == 2:
    print(num1 + num2)
elif act == 4:
    print(num1 - num2)
input("Press enter to close...")
