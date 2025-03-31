# Ask to enter text
text = input("Enter a text: ")

# Ask to enter a character to find  
character = input("Enter a character to find: ")

# Find the first occurrence of the character 
location = text.find(character)

# Print the result 
if location != -1:
    print(location)
else:
    print(f'The "{character}" is not in the text')
