print("For Addition --- Press 1")
print("For Subtraction --- Press 2")
print("For Multiplication --- Press 3")
print("For Division --- Press 4")

choice = int(input("Enter Your Choice (1/2/3/4): "))

if(choice in [1,2,3,4]):
    number1 = int(input("Enter First Number: "))
    number2 = int(input("Enter Second Number: "))
    
    if(choice == 1):
        result = number1 + number2
    elif(choice == 2):
        result = number1 - number2
    elif(choice == 3):
        result = number1 * number2
    elif(choice == 4):
        if(number2 == 0):
            print("Error! Division by zero is not allowed.")
        else:
            result = float(number1 / number2)
else:
    print("Invalid Choice! Please enter a number between 1 and 4.")

print("The result of the operation is {}".format(result))

        

