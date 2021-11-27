# A simple calculator

# This function adds two numbers
# notice that it returns this sum to the instruction that called the function
# can you find where it returns a value to?
def add(x, y):
    return x + y

# This function subtracts two numbers
# notice that it returns this difference to the instruction that called the function
# can you find where it returns a value to?
def subtract(x, y):
    return x - y

print("Select operation.")
print("1.Add")
print("2.Subtract")

while True:
    # take input from the user
    choice = input("Enter choice(1/2): ")

    # check if choice is one of the 2 options
    if choice in ('1', '2'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do another calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")

# Challenge: Can you add division and multiplication to this calculator?
