# An example of a function with parameters

# Functions are blocks of code that run whenever you call them (tell them to run)
# Functions can take in inputs (called parameters or arguments)
# Functions can also return results once they finish running

# A function that takes 3 arguments and prints the values
def greet_user(first_name, last_name, age):
    print("Running Example 1...")
    print("Hello", first_name)
    print("In the year 2025, you will be ", age + 4, "years old")

# This instruction calls the function
greet_user("Elijah", "Mccoy", 197)


# Example 2: A function that subtracts two floats and prints the result
def subtract_numbers(float_1, float_2):
  print("Running Example 2...")
  result = float_1 - float_2
  print(result)

""" 
Challenge: Create a function that adds 3 integers and prints the result. 
Remember to include an instruction to call your function. Bonus for adding comments.
Once it is done, test your code in the shell using the command: python FunctionParameters.py
"""