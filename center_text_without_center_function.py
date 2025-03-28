# Ask to enter a text to center
text = input("Enter a text: ")

# Center the text without using center
total_space = max(0, 40 - len(text))
left_space = total_space // 2
right_space = total_space - left_space

text_centered = " " * left_space + text + " " * right_space

# Print the result
print("Result: |" + text_centered + "|")
