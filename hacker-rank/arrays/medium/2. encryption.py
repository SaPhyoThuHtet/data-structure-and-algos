# Encryption
def encryption(s):
    # Write your code here
    s = re.sub(r' ', r'', s)
    L = len(s)
    row = math.floor(math.sqrt(L))
    column = math.ceil(math.sqrt(L))
    
    result = ""
    print(row, column, L)
    
    if(row*column <L):
        row = column
        
    for i in range(column):
            index = i
            for j in range(row):
                if(index < L):
                    result += s[index]
                    index += column
            print(result)
            result += " "  
    #print(result)
    return result 
