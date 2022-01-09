s = "hello"
start = 0
end = len(s)-1
        
while (start <end):
            s = s[0:start]+s[end]+s[start+1:end]+s[start]+s[end+1:]
            start += 1
            end -= 1
            
        
