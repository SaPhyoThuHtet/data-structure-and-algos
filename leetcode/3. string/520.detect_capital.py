"""
e define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if re.match(r"^[A-Z]+$", word):
            return True
        
        elif re.match(r"^[a-z]+$", word):
            return True
        
        elif re.match(r"^[A-Z][a-z]+$", word):
            return True
        
        else:
            return False
        
        
