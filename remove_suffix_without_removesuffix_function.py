# Ask to enter a text that has a suffix to remove
text = input("Enter a text: ")

# Ask to enter the suffix to remove  
suffix = input("Enter the suffix to remove: ")

# Remove the suffix if it matches the end of the string  
if text.endswith(suffix):  
    text = text[:-len(suffix)] 
  
# Print the result 
print(f"Result: {text}")
