# Ask to enter a text  
text1 = input("Enter a text: ")
text2 = input("Enter another text: ")

# Ask to enter the total width of the final string  
width = int(input("Enter the total width: "))

# Add spaces at the beginning until it reaches the specified width  
text1 = " " * (width - len(text1)) + text1
text2 = " " * (width - len(text2)) + text2

# Print the result  
print(f"Result: \n'{text1}'\n'{text2}'") 
