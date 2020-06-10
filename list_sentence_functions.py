            # 25: Even More Practice

stuff = ("Here is a test sample of a string.")
print(stuff)

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
print("break_words(list_name): ", break_words(stuff))

words = stuff.split(' ')
print("words = ", words)
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
print("sort_words(list_name): ", sort_words(words))

        # The strings with """ appear in the terminal if you enter "help(ex25)" along with the functions
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)
print("word = print_first_word(list_name): ", print_first_word(words))

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)
print("print_last_word(list_name): ", print_last_word(words))

def sort_sentence(sentence):
    """Takes in a full sentences and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
print("sort_sentence(sentence_name): ", )

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
