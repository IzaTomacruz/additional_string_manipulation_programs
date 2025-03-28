# Ask to enter any text
text = input("Enter a text: ")

# Convert all characters to lowercase without using lower
translate_lower = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")

# Print the result
print("Result:", text.translate(translate_lower))
