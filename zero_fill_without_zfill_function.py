# Ask to enter a digit 
number = input("Enter a number: ")

# Check if it has six digits and add zeros until it reaches six digits
while len(number) < 6:
    number = '0' + number

# Print the result  
print(f"Result: {number}")

