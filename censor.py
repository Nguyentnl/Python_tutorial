# that takes two strings, text and word, as input. It should return the text with the word you chose replaced with
# asterisks

def censor(text, word):
    words = text.split()
    result = ""
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result = ' '.join(words)

    return result


censor("hey hey hey", "hey")
print censor
