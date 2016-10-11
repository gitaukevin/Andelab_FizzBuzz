def words(phrase):
    words = {}
    phrase = phrase.split(" ")

    for word in phrase:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

    return words

