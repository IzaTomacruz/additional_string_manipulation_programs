# Ask to enter a text  
text = input("Enter a text: ")

# Check if all characters are lowercase  
lowercase = True

for character in text:
    if not character.isupper():
        lowercase = True
    else:
        lowercase = False
        break
      
# Print true if all are lowercase or false if not 
print(f"Are all characters in text lowercase?: {lowercase}")
