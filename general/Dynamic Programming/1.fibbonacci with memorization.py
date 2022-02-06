val = {0:0, 1:1}

def fib(n):
    
    if n in val:
        return val[n]
        
    val[n] = fib(n-1)+fib(n-2)
    
    return val[n]


print(fib(5))
