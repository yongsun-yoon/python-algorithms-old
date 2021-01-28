from typing import List

class Solution:
    def check(self, word, dictionary, memory):
        if word not in memory:            
            val = word in dictionary and self.check(word[:-1], dictionary, memory)
            memory[word] = val
        return memory[word]

    def longestWord(self, words: List[str]) -> str:
        memory = {'':True}
        idx = 0
        words = sorted(words, key=lambda x : [-len(x), x])
        
        while True:
            word = words[idx]
            done = self.check(word, words, memory)
            if done:
                return word
            else:
                idx += 1
                
        