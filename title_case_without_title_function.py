# Ask to enter a text
text = input("Enter a text: ")

# Convert first character in each word to uppercase without using title() function
words = text.split()

for i in range(len(words)):
    words[i] = words[i][0].upper() + words[i][1:].lower()    

title_case_text = " ".join(words)

# Print the result
print("Result:", title_case_text)
