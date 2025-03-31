# Ask to enter ten numbers
list = []
print("Enter 10 numbers")

for i in range(-1, 9):
    number = int(input(f"Location ({i + 1}): "))
    list.append(number)
  
# Ask to enter a number to find  
find_number = int(input("Enter a number you want to find: "))

# Find the first occurrence of the number 
location = -1
for i in range(len(list)):
    if list[i] == find_number:
        location = i
        break
      
# Print the result 
if location != -1:
    print(f"The {find_number} first occured in Location {location}")
else:
    print(f"The {find_number} is not in the list")
