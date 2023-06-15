"""module to create text file with one word per line

Richard Sapp
13 June, 2023

"""

# word library
import nltk

from nltk.corpus import words

# only file used here is the word_list
file_extension = "word_list.txt"

english_words = words.words()

# change this number to change word length
# filtered_words = [word for word in english_words if len(word) <= 7] # names included
filtered_words = [word for word in english_words if len(word) <= 7 and word[0].islower()] # names excluded

# writes text file
with open(file_extension, "w") as file:
    file.write('\n'.join(filtered_words))

print("File 'word_list.txt' has been created.")


