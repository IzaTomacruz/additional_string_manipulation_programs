# Ask to enter any text that has a prefix to remove
text = input("Enter a text: ")

# Remove the prefix from the text without using removeprefix
prefix = input("Enter the prefix to remove: ")

if text[:len(prefix)] == prefix:
    without_prefix = text[len(prefix):]
else:
    without_prefix = text

# Print the result
print("Result:", without_prefix)
