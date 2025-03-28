# Ask to enter a text
text = input("Enter a text: ")

# Swap the case of each character without using swapcase
swapped_case_text = ""

for character in text:
    if character.islower():  
        swapped_case_text += character.upper()  
    elif character.isupper():  
        swapped_case_text += character.lower()  
    else:  
        swapped_case_text += character
      
# Print the result
print("Result:", swapped_case_text)
