# Odd number of times 
# Given an array, find the int that appears an odd number of times.  

# Example: for [2, 4, 4, 10, 2] => the function will return 10, because it appears 1 time.

def find_odd_appearance_number(numbers):
    appearance_counter={}
    for num in numbers:
        if num in appearance_counter:
            appearance_counter[num] += 1
        else:
            appearance_counter[num] = 1
    
    for num in numbers:
        if appearance_counter.get(num) %2 ==1:
            return num 
    return None

print(find_odd_appearance_number([2, 4, 4, 10, 2]))