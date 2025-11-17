# Exercise 1: Counting vowels
# Write a Python program that counts how many vowels (a, e, i, o, u) are in a given string.
# Example input: "hello world"
# Example output: 3

string1="abd d db o"
def count_vowels(string):
    vowels=["a", "e", "i", "o", "u"]
    count=0
    for char in list(string):
        if char in vowels:
            count=count+1
    return count
print(count_vowels("aabw"))

