# Max repeating char 
# Return the first max repeating Char in a string
# Example: ababcd => a
# ""=>None

def max_repeating(word):
    if(len(word)==0):
        return None
    chars_repeating = {}
    max_count = 0
    max_char = ""
    for char in word:
        if chars_repeating.get(char)!=None:
            chars_repeating[char]+=1
        else:
            chars_repeating[char] = 1
        if chars_repeating[char]>max_count:
            max_count = chars_repeating[char]
            max_char = char
    return max_char

print(max_repeating(""))
print(max_repeating("a"))
print(max_repeating("ababcd"))
print(max_repeating("ababcdb"))


    