def count_words(string):
    return len(string.split())

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    # print(file_contents)
    count_words(file_contents)
