# Ask to enter text
text = input("Enter a text: ")

# Ask to enter a text to find  
character = input("Enter a character to find: ")

# Find the last occurrence of the text 
location = text.rfind(character)

# Print the result 
if location != -1:
    print(f'The "{character}" last occured in {location}')
else:
    print(f'The "{character}" is not in the text')
