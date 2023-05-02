
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

# Returns the words in word_list that contain the letter
def check_contain_letter(word_list, letter):
    words_with_letter = []
    for x in word_list:
        if letter in x:
            words_with_letter.append(x)
    return words_with_letter

def anagram():
    word = input("enter a word: ")
    same_length_words = check_same_length(load_words(), word)
    anagram = same_length_words
    for letter in word:
        anagram = check_contain_letter(anagram, letter)
        #print(letter + ": " + str(anagram))
    print(anagram)

anagram()