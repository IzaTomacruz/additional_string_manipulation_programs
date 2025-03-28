# Ask to enter a text
text = input("Enter a text: ")

# Ask to enter last characters to check if it ends with the text
last_character = input("Enter last characters to check: ")

# Check if the text ends with input without using endswith
if len(last_character) > len(text):
    result = False
else:
    result = text[-len(last_character):] == last_character
  
# Print the result
if result:
    print(f"The text ends with '{last_character}'.")
else:
    print(f"The text does not end with '{last_character}'.")

