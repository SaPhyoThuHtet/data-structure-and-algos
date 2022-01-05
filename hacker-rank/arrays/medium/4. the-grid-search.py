def gridSearch(G, P):
    # Write your code here
    index = 0
    prev = []
    
    for g in G:
        if P[index] in g:
            if(index ==0):
                prev = start_indicies_of_pattern(g, P[0])
                index += 1
            else:
                index, prev = same_code(g, P, prev, index)
            #print("If", prev)
                
            
        elif (index != 0 and P[0] in g):
            index = 0
            index, prev = same_code(g, P, prev, index)
            #print("Elif", prev)
            
        else:
            index = 0
            prev = []
            #print("Else", prev)
                
        
            
        if(index == len(P)):
            return "YES"
            
            
    return "NO"

def same_code(g, P, prev, index):
    if index == 0:
        return 1, start_indicies_of_pattern(g, P[index])
    
    current = start_indicies_of_pattern(g, P[index])
    
    if (len(list(set(current) & set(prev)))>0):
        prev = list(set(current) & set(prev))
        index += 1
    else:
        index = 0
        prev  = []
    return (index, prev)
    
def start_indicies_of_pattern(g,p):
    result = []
    for i in range(0,len(g)-(len(p)-1)):
        if g[i:(i+len(p))] == p:
            #print(g[i:(i+len(p))])
            #print(i)
            #print("--------")
            result.append(i)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
