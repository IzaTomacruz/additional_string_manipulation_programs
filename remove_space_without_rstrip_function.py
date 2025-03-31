# Ask to enter a text that has space at the end
name = input("Enter your name: ")

# Remove the space of the end of the string
while name[-1] == " ":
    name = name[:-1]  
  
# Print the result
print(f"Hello {name}!")
