
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, wordsToCheck):
        #["e", "i", ...] -> "ei..."
        ourWordInOrder = ''.join(sorted([letter for letter in self.word]))
        result = []
        for wordToCheck in wordsToCheck:
            theirWordInOrder = ''.join(sorted([letter for letter in wordToCheck]))
            if(ourWordInOrder == theirWordInOrder):
                result.append(wordToCheck)
                
        return result
            
                
            
        
        #ways we can tell if words are anagrams
        #exclude any word thats not the same length
        
        