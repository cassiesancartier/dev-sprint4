# Name: Cassie Sancartier


# 10.7

def is_anagram(word1, word2):
    for letter in word1:
        if letter not in word2:
            return False
    return True
    

result:

>>> is_anagram('baseball', 'bat')
False
>>> is_anagram('take', 'teak')
True


#