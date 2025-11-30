 # Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

 
    # Error handling for division by zero
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    return num1 / num2

# Main program loop
def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Multiply")

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2 ): ")

        # Check if choice is one of the valid options
        if choice in ('1', '2' ):
                print("Exiting calculator.")
                break

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter a number.")
     

if   '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
elif  '2':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
                if isinstance(result, str) and "Error" in result:
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
else:
    print("Invalid Input")

# Run the calculator function
if __name__ == "__main__":
    calculator()
 