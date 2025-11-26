# Count vowels
# How do you count the number of vowels and consonants in a given string

def count_vowels_constants (string):
    vowels = {"a","e","i","o","u"}
    result = {"vowels":0,
              "constants":0}
    for char in string.lower() :
        if char in vowels:
            result["vowels"]+=1
        elif "a"<=char<="z":
            result["constants"]+=1
    
    return result
# print(count_vowels_constants("aaa   b54b 6i"))
# print(count_vowels_constants("444   4545 65 "))