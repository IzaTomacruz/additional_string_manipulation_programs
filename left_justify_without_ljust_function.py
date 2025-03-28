# Ask to enter any text 
text = input("What is your favorite fruit: ")
width = int(input("Enter the total width: "))

# Add spaces to the end of the text without using ljust
if len(text) < width:
    text_with_space = text + " " * (width - len(text))
else:
    text_with_space = text 
  
# Print the result
print("The", text_with_space, "is my favorite fruit")
