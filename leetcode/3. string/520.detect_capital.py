"""
e define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Given a string word, return true if the usage of capitals in it is right.
"""

# Please be aware of $ for the last
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if re.match(r"^[A-Z]+$", word): #checking All letters in this word are capitals, like "USA".
            return True
        
        elif re.match(r"^[a-z]+$", word):# checking All letters in this word are not capitals, like "leetcode".
            return True
        
        elif re.match(r"^[A-Z][a-z]+$", word):# checking  Only the first letter in this word is capital, like "Google".
            return True
        
        else:
            return False
        
        
# နောက်ထပ် ကြိုက်တဲ့ code လေးတစ်ခု (Not my code)
def detectCapitalUse(self, word):
        return word.upper()==word or word.lower()==word or word.capitalize()==word
