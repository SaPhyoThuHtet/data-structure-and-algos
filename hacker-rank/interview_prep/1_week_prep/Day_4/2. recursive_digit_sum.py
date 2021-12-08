#!/bin/python3
# ဒီမှာက ဖြေရှင်းရတာက လွယ်တယ်။ Time Complexitiy က ခက်တာ။ 9999999999999..................................9 ကို အကြိမ်1000 စာ ပွားပြီး ပေါင်းမိတော့ Time Complexity တက်တယ်။
# Solution is 9999999999999..................................9 ကို အရင် ပေါင်းပြီး ရလာတဲ့ တန်ဖိုးကိုမှ 1000 နဲ့မြှောက်လိုက်တာ။
import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:

#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    str_n = str(n)
    if(len(str_n) == 1):
        return n
    
    str_n = str(sum([int(i) for i in str_n])*k)
    #print("First Sum", str_n)
    
    while (len(str_n) !=1 ):
        str_n = str(sum([int(i) for i in str_n]))
        #print(str_n)
    return int(str_n)
        
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
