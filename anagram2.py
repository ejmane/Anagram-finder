# Load all the words in words_alpha.txt into a list
def load_words():
    word_list = []
    f = open("words_alpha.txt", "r")
    for x in f:
        word_list.append(x.split("\n")[0])
    return(word_list)

# Returns the words in word_list that contain the same letters as word
def check_same_length(word_list, word):
    words_of_length = []
    for x in (word_list):
        if len(x) == len(word):
            words_of_length.append(x)
    return words_of_length

def get_letters(word):
    letters_in_word = {}
    for letter in word:
        if letter in letters_in_word:
            continue
        letters_in_word[letter] = word.count(letter)
    return letters_in_word

def check_letters_in_word(word_list, letters_list):
    anagram = []
    letter_list_keys = list(letters_list.keys())
    for word in word_list:
        for letter in letter_list_keys:
            if letter == letter_list_keys[-1] and word.count(letter) == letters_list[letter]:
                anagram.append(word)
            elif word.count(letter) == letters_list[letter]:
                continue
            else:
                break
    return anagram

def anagram():
    word = input("Enter a word: ")
    anagrams = []
    anagrams = check_letters_in_word(check_same_length(load_words(), word) , get_letters(word))
    return anagrams

print(anagram())