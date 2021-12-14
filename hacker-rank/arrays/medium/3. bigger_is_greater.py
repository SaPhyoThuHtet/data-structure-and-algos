#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

 # Main is to understand the problem.

def biggerIsGreater(w):
    # Write your code here
    if (len(w) == 1):
        return "no answer"
    
    elif (w[-1] > w[-2]):
        return w[0:-2]+w[-1]+w[-2]
    
    else:
        end = len(w)-2
        
        while (end>0):
    
            if(w[end] > w[end-1]):
                #print(w[end])
                #print(w[end-1])
                #print("end, end-1")
                
                index = None
                min_diff = float('inf')
                status = False
                
                for i in range(end,len(w)):
                    if(w[end-1]<w[i]):
                        print("Here", w[i])
                        if(abs (ord(w[i]) - ord(w[end-1]) ) < min_diff):
                            index=i
                            min_diff = abs ( ord(w[i]) - ord(w[end-1]) )
                            status = True
                #print("Index", index)
                if (status):
                    result = list(w)
                    result[end-1], result[index] = result[index], result[end-1]
                    #print("result", result)
                    
                    return "".join( map(str,result[0:end])  )+"".join( map( str, sorted(result[end:]) ) )
                                      
            
            end = end-1
            
    
                

            
    return "no answer"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
