# Ask to enter any text that has space at the beginning
text = input("Enter a text: ")

# Remove the space at the beginning of the text without using lstrip
non_space_indices = [i for i in range(len(text)) if text[i] != " "]

if non_space_indices:
    text_without_leading_spaces = text[min(non_space_indices):]
else:
    text_without_leading_spaces = ""
  
# Print the result
print("Result:", text_without_leading_spaces)
