# 🧩 Exercise 1

# Create a list named colors that contains five color names of your choice.
# Then:

# Print the entire list.

# Print only the second color in the list.

colors = ["red", "green", "blue", "yellow", "black"]
print(colors)
print(colors[1])

# 🧩 Exercise 2

# Create a list named numbers with these values: 5, 10, 15, 20, 25.
# Then:

# Print the list.

# Print the sum of all numbers using the built-in function sum().

numbers = [5, 10, 15, 20, 25]
total = 0
for num in numbers:
    total = total + num
print (total)


numbers = list(range(1,11))
new_list = []
for num in numbers:
    new_list.append(num*10)
print(new_list)

new_list_2= [num*10 for num in numbers]
print(new_list_2)

new_list_2= [0*num for num in range(10)]
print(new_list_2)

new_list_2= [0 for _ in range(10)]
print(new_list_2)

print(numbers[::-1])
print (numbers[-1::-1])

