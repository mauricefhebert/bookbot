def count_words(string):
    return len(string.split())

def count_letters(string):
    dictionary = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    string_lower = string.lower()
    for char in string_lower:
        if char in dictionary:
            dictionary[char] = dictionary[char] + 1
    return dictionary

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    # print(file_contents)
    # print(count_words(file_contents))
    print(count_letters(file_contents))
