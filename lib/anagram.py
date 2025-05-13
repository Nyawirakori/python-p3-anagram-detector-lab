# your code goes here!
#Pseudocode:
# Create a class called Anagram
# Create an __init__ that takes a word as a parameter
# Create a instance method called match(), which takes a list of anagrams
# Iterate through the word checking for matching letters using a for in loop
# Use sorted() method to compare
# The method returns matches and if none are are found, it returns an empty list

# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word =word.lower()
        self.sorted_word = sorted(self.word)
        
    def match(self, word_list):
        matches = []
        for letter in word_list:
            if letter.lower() != self.word and sorted(letter.lower()) == self.sorted_word:
                matches.append(letter)
        return matches
                
                
listen = Anagram("listen")
print(listen.match(["enlists", "google", "inlets", "banana"]))
        

