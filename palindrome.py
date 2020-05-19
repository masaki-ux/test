def paildrome(word):
    word = word.lower()
    return word[::-1] == word

print(paildrome('Monster'))
print(paildrome('Mom'))
