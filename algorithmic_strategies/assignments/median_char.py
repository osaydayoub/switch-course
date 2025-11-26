# Median char
# Find the median char (half of the letters are smaller than it, and half are bigger) in a string.
# Smaller or bigger is in relation to the place in the alphabet. Example: question => o

def get_median_letter(string):
    letters = [ char for char in string if char.isalpha()]
    if(len(letters)==0):
        return ""
    letters.sort()
    index = int((len(letters)-1)/2)
    return letters[index]

print(get_median_letter("question"))