# Ask to enter ten fruits
basket = []
print("Enter 10 fruits")

for i in range(10):
    fruit = input(f"Fruit {i + 1}: ")
    basket.append(fruit)
  
# Ask what fruit you want to count
find_fruit = input("Enter a fruit you want to count: ")

# Count how many times you entered the fruit
count = 0
for fruit in basket:
    if fruit == find_fruit:
        count += 1

# Print the result  
if count > 0:
    print(f"You entered the {find_fruit} {count} times.")
else:
    print(f"No fruit named {find_fruit} found")
