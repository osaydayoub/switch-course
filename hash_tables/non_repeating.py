# Find the first non-repeating character 
# Return the first non-repeating char in a string. 

# example: abacce => b

def find_first_non_repeating(string):
    appearance_counter={}
    for char in string:
        if char in appearance_counter:
            appearance_counter[char] += 1
        else:
            appearance_counter[char] = 1
    
    for char in string:
        if appearance_counter.get(char) == 1:
            return char 

print(find_first_non_repeating("abacce"))