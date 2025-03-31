# Ask to enter a text  
text = input("Enter a text: ")

# Ask to enter the prefix to check  
prefix = input("Enter the prefix to check: ")

# Check if the text starts with the given prefix  
print("Does it matched?: True or False?") 

if text[:len(prefix)] == prefix:
    print("Result: True")
else:
    print("Result: False")
  
# Print true if it matches or false if not
