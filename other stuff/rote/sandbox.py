# MERGE STRINGS ALTERNATELY

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = [char for pair in zip(word1, word2) for char in pair]
        
        remainder = word1[len(word2):] if len(word1) > len(word2) else word2[len(word1):]
        
        return ''.join(result) + remainder
    
    
# drill

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        result = [char for pair in zip(word1, word2) for char in pair]
        
        remainder = word1[len(word2):] if len(word1) > len(word2) else word2[len(word1):]
        
        return ''.join(result) + remainder 