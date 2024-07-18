# create a list with different types of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# loop through fruits and count the total fruits in the list
for i in fruits:
    # use an f-string to print the fruit name and the number of the fruit in the list
    print(f"{i} is fruit number {fruits.index(i) + 1}")

# the total number of fruits in the list
print(f"Total fruits in the list: {len(fruits)}")


