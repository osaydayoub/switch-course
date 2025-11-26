# Given a string of words, you need to find the highest scoring word. 
# Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3 etc.

# ○	You need to return the highest scoring word as a string.
# ○	If two words score the same, return the word that appears earliest in the original string.
# ○	All letters will be lowercase and all inputs will be valid.

def get_max_score_word(words):
    words_list=words.split()
    max_score = 0
    max_word = ""
    for word in words_list:
        current_score = 0
        for char in word:
            current_score+=ord(char)-ord("a")+1
        if current_score >max_score:
            max_score = current_score
            max_word =word
    return max_word



