#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here    
    rows = n-1
    columns = n-1
    
    # Main_diagonal
    upper_main = min(n-r_q, c_q-1)
    lower_main = min(r_q-1, n-c_q)
    
    upper_other = min(n-r_q, n-c_q)
    lower_other = min(r_q-1, c_q-1)
    
    print("Rows", rows)
    print("Columns", columns)
    print("Upper Main", upper_main)
    print("Lower Main", lower_main)
    print("Upper Other", upper_other)
    print("Lower Other", lower_other)
    
    dic_upper_main = []
    dic_lower_main = []
    dic_upper_other = []
    dic_lower_other = []
    dic_row_less_than_cq = []
    dic_row_greater_than_cq = []
    dic_col_less_than_rq= []
    dic_col_greater_than_rq= []
    
    for i in obstacles:
        if(i[0] == r_q): #this element is in the row of queen
            #print("Row")
            #print(i)
            if (i[1]<c_q and i[1] not in dic_row_less_than_cq):
                dic_row_less_than_cq.append(i[1])
                #rows -= (i[1])
            elif(i[1]>c_q):
                dic_row_greater_than_cq.append(i[1])
                #rows -= (n-i[1]+1)
                
        elif(i[1] == c_q): #this element is in the column of queen
            #print("Column")
            #print(i)
            if(i[0]>r_q and i[0] not in dic_col_greater_than_rq):
                dic_col_greater_than_rq.append(i[0])
                #columns -= (n-i[0]+1)
            elif(i[0]<r_q and i[0] not in dic_col_less_than_rq):
                dic_col_less_than_rq.append(i[0])
                #columns -= i[0]
             
        elif(abs(r_q-i[0]) == abs(c_q-i[1]) and i[0]>r_q): #upper
            if(i[1]>c_q and i[0] not in dic_upper_other): #upper other
                dic_upper_other.append(i[0])
            elif(i[1]<c_q and i[0] not in dic_upper_main): #upper main
                dic_upper_main.append(i[0])
                
            
            
        elif(abs(r_q-i[0]) == abs(c_q-i[1]) and i[0]<r_q): #lower
            if(i[1]<c_q and i[0] not in dic_lower_other):
                dic_lower_other.append(i[0])
                
            elif(i[1]>c_q and i[0] not in dic_lower_main):
                dic_lower_main.append(i[0])
        
        else:
            print("I am in nothing")
            print(i)
            print()
    r = rows
    c = columns
    if(len(dic_row_less_than_cq) != 0):
         #rows -= (min(dic_row_less_than_cq))
         print("Dic_row_less", min(dic_row_less_than_cq))
         rows -= diagonal(c_q-1, min(dic_row_less_than_cq), c_q)
    if(len(dic_row_greater_than_cq) != 0):
         #rows -= (n-min(dic_row_greater_than_cq)+1)
         print("Dic_row_greater", min(dic_row_greater_than_cq))
         rows -= diagonal(n-c_q, min(dic_row_greater_than_cq), c_q)
    if(len(dic_col_greater_than_rq) != 0):
         #columns -= (n-min(dic_col_greater_than_rq)+1)
         columns -= diagonal(n-r_q, min(dic_col_greater_than_rq), r_q)
    if(len(dic_col_less_than_rq) != 0):
         #columns -= min(dic_col_less_than_rq)  
         columns -= diagonal(r_q-1, min(dic_col_less_than_rq), r_q) 
        
    if(len(dic_upper_main)!=0):
        print("min-upper-main", min(dic_upper_main))
        upper_main -= diagonal(upper_main, min(dic_upper_main), r_q)
    if (len(dic_lower_main) != 0):
        print("min-lower-main", min(dic_lower_main))
        lower_main -= diagonal(lower_main, min(dic_lower_main), r_q)
    if (len(dic_upper_other) != 0):
        print("min_dic_upper_other", min(dic_upper_other), r_q)
        upper_other -= diagonal(upper_other, min(dic_upper_other),r_q)
    if (len(dic_lower_other) != 0):
        print("min_dic_lower_other", min(dic_lower_other))
        lower_other -= diagonal(lower_other, min(dic_lower_other), r_q)
    
    
    print("Rows", rows)
    print("Columns", columns)
    print("Upper Main", upper_main)
    print("Lower Main", lower_main)
    print("Upper Other", upper_other)
    print("Lower Other", lower_other)       
            
    
    #Big Congratualtions
       
            
                
    return rows+columns+ upper_main+ lower_main+ upper_other+ lower_other

def diagonal(num_of_elements, i, r_q):
    dif = abs(r_q-i)
    return num_of_elements -  (dif -1)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
