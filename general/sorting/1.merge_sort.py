# Merge Sort



def merge_sort(arr):
    
    if (len(arr) < 2):
        return arr
        
        
    mid = len(arr)//2    
    left_array = arr[0:mid]
    right_array = arr[mid:]
    #print(left_array, right_array)
    
    return merge(merge_sort(left_array), merge_sort(right_array))
    
    
def merge(l,r):
    result = []
    
    i = 0
    index_l = 0
    index_r = 0
    #print(l,r)
    while (i < min(len(l), len(r)) ):#ဒီနား Update လုပ်ဖို့ လိုသေးတယ်။
        #print(index_l)
        if (l[index_l] < r[index_r]):
            result.append(l[index_l])
            index_l +=1
            
            
        elif (l[index_l] > r[index_r]):
            result.append(r[index_r])
            index_r +=1
            
        else:
             result.append(l[index_l])
             index_l +=1
             result.append(r[index_r])
             index_r +=1
             
        i += 1
            
    #print(index_l)       
    if (index_l != len(l)):
        for i in l[index_l:]:
            result.append(i)
            
            
    if (index_r != len(r)):
        for i in r[index_r:]:
            result.append(i)
            
    #print(result)     
    return result
            
            
        
        
        
    
    
print(merge_sort([2,2,1, 0]))
