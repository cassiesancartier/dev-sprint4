# Name: Cassie Sancartier


# 10.7 - Anagrams

def is_anagram(word1, word2):
    word_one_list = list(word1)
    word_two_list = list(word2)

    if sorted(word_one_list) == sorted(word_two_list):
        return True

    else:
        return False


# 10.13 - Interlocking words


def does_interlock(word_list):
    words = set(line.strip() for line in word_list)
    for w in words:
        word1, word2 = w[::2], w[1::2]
    if word1 in words and word2 in words:
        print word1, word2


def does_interlock(word_list):
    words = set(line.strip() for line in word_list)
    for w in words:
        word1, word2, word3 = w[::3], w[1::3], w[2::3]
    if word1 in words and word2 in words and word3 in words:
        print word1, word2, word3        



