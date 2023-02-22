def print_upper_words(words):
    """a function that turns all words into upper cases"""
    print(word.upper for word in words)

def print_upper_words3(words_list):
    """a function that turns all words that start with an e to uppercase"""
    for word in words_list:
        if word[0] == 'e':
            print(word.upper)


def print_words_with_letter(words, letter):
    """a function that takes a letter and puts the word that starts with this letter """
    for word in words:
        if word[0] == letter:
            print(word)


print_upper_words('tiny')