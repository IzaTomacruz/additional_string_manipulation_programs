# Ask to enter a text
text = input("Enter a text: ")

# Check if all characters are uppercase without using isupper
all_upper = True

for character in text:
    if "a" <= character <= "z":  
        all_upper = False
        break
      
# Print true if all characters are in upper case and false if not
print("Are all characters in text in uppercase?", all_upper)
