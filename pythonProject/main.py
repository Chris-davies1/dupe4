# Pseudocode:
# 1. Prompt the user for their name and store it.
name = input("What is your name: ")
# 2. Prompt the user for their first number and store it.
first_number = float(input(f"{name}, give me your first number: "))
# 3. Prompt the user for their second number and store it.
second_number = float(input(f"{name}, give me a second number: "))


sum_numbers = first_number + second_number
# 4. Calculate the sum of the two numbers.
print(f"{first_number} + {second_number} = {sum_numbers}")
# 5. Print the sum and the user's name with the result.
print(f"{name} you get {sum_numbers}.")