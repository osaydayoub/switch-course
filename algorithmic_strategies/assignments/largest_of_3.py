# Largest of 3
# Write a function that receives 3 numbers and return the biggest one.
# You are not allowed to use any functions including built in ones.

def get_largest_of_3(a, b, c):
    current_max = a if a>b else b
    return current_max if current_max > c else c
    
    
        
print(get_largest_of_3(3,2,1))