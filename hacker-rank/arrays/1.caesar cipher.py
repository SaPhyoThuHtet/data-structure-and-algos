"""In changing the character, for the case that does not exceed 122, we just need to return ord(char)+k. Note, ord('z') is 122.

If the value exceed 122 by n, we can get the first character by adding 96 and their difference.

Example 1: 
k=2 and 'z'
ord('z')+k, 122+2 => 124
124-ord('z')=>144-122=> 2 refers to the second character of the english alphabets. We can obtain the second character by adding 96.
chr(96+2) => chr(98)=>'b'


Example 2: 
k=2 and 'y'
ord('y')+k, 121+2 => 123
123-ord('z')=>1=> 1 refers to the first character of the english alphabets. We can obtain the second character by adding 96.
chr(96+1) => chr(97)=>'a'
"""


def caesarCipher(s, k):
    # Write your code here
    k = k%26
    # 96+(difference)  E.g. 96+( (ord('z')+k) - ord('z')) if range exceeds
    
    result = ""
    for i in s:
        if(i.isalpha() and i.islower()):
            result += change_char(i,k)
                
        elif(i.isalpha() and i.upper()):
            i = i.lower()
            result += change_char(i,k).upper()
            
        else:
            result += i
                
    return result

def change_char(i,k):
    result = ""
    if(ord(i)+k <= 122):
        result += chr(ord(i)+k)
    else:
        result += chr(96+ ((ord(i)+k)-ord('z')) )
    return result
