# Ask to enter a text  
text = input("Enter a text: ")

# Convert all lowercase characters to uppercase  
uppercase = ""

for character in text:
    if character.islower():
        uppercase += character.swapcase()
    else:
        uppercase += character

# Print the result  
print(f"Result in uppercase: {uppercase}")
