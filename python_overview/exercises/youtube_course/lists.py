# collections = single "variable" used to store multiple values
# List = [] ordered and changeable. duplicates OK
# Set = {} unordered and immutable (individual items can’t change), but add/remove OK. NO duplicates
# Tuple = () ordered and unchangeable. duplicates OK. FASTER to access

# Create a list (collection) of fruit names
fruits = ["apple", "orange", "banana", "coconut"]

# Print the entire list
print(fruits)

# Print the first and second items (indexing starts at 0)
print(fruits[0])  # apple
print(fruits[1])  # orange

# Print a slice of the list (items from index 0 up to, but not including, 3)
print(fruits[0:3])  # ['apple', 'orange', 'banana']

# Same as above — start from beginning, stop before index 3
print(fruits[:3])

# Print every second item in the list
print(fruits[::2])  # ['apple', 'banana']

# Print the list in reverse order
print(fruits[::-1])  # ['coconut', 'banana', 'orange', 'apple']

# Loop through each fruit and print it
for fruit in fruits:
    print(fruit)

# print(dir(fruits))  # Shows all available methods and attributes of the list
# print(help(fruits)) # Shows documentation/help info for the list object

# Print how many items are in the list
print(len(fruits))  # 4

# Check if "apple" exists in the list (returns True or False)
print("apple" in fruits)

# Change the first item to "pineapple"
fruits[0] = "pineapple"

# Add "pineapple" to the end of the list
fruits.append("pineapple")

# Remove the first occurrence of "apple" from the list
fruits.remove("apple")

# Insert "pineapple" at the beginning of the list (index 0)
fruits.insert(0, "pineapple")

# Sort the list in alphabetical order
fruits.sort()

# Reverse the order of the list (in place)
fruits.reverse()

# Remove all items from the list (the list becomes empty)
fruits.clear()

# Return the index (position) of the first occurrence of "apple"
fruits.index("apple")

# Count how many times "apple" appears in the list
fruits.count("apple")


# Set = a collection of unique values (no duplicates), unordered, and you can’t access items by index
fruits = {"apple", "orange", "banana", "coconut"}  # create a set with four fruits

print(fruits)  # print the whole set (order may be different each time because sets are unordered)

# Loop through all items in the set
for fruit in fruits:
    print(fruit)  # print each fruit (order is random)

len(fruits)  # returns the number of items in the set (but doesn’t print it)

print("apple" in fruits)  # check if "apple" is in the set (returns True or False)

fruits.add("pineapple")  # add a new item to the set (if it’s not already there)

fruits.remove("apple")  # remove a specific item; throws an error if "apple" doesn’t exist

fruits.pop()  # remove a random item (since sets don’t have order)

fruits.clear()  # remove all items — the set becomes empty

print(fruits)  # prints an empty set: set()


# Tuple = an ordered and unchangeable collection. Allows duplicates and is faster than a list.
fruits = ("apple", "orange", "banana", "coconut", "coconut")  # create a tuple with 5 items

print(fruits)  # print the entire tuple

len(fruits)  # get the number of items (but doesn’t print it)

print("apple" in fruits)  # check if "apple" is in the tuple (returns True or False)

fruits.index("apple")  # get the index (position) of the first "apple"

fruits.count("apple")  # count how many times "apple" appears in the tuple

# Loop through all items in the tuple
for fruit in fruits:
    print(fruit)  # print each fruit

