#!/bin/python3

import math
import os
import random
import re
import sys

#
'''
 ဒီ Problem က လွယ်တယ်။ Time Complexity ကတော့ တော်တော် လေးစဉ်းစားရတယ်။ ပထမ က ဒီတိုင်း ရိုးရိုးပဲ Loop သုံးခုနဲ့သွားတာ အဖြေမှန်ပေမယ့် အချိန်ကြောင့် ၅ test cases က မရဘူး။ နောက် အမျိုးမျိုးကနေ ခု Code ရလာတာ။
မှတ်ချက်။ ။ ပိုနေတဲ့ statement တစ်ခု ဖြုတ်ရုံနဲ့တင် အချိန်သက်သာ စေတယ်။
'''




# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

def beautifulTriplets(d, arr):
    # Write your code here
    count = 0
    for i in range(len(arr)-3+1):
        j_count = arr[i+1:len(arr)-2+1].count(arr[i]+d)
        k_count = arr[i+2:len(arr)].count(arr[i]+2*d)
        count += min (j_count, k_count)
        
    return count
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
