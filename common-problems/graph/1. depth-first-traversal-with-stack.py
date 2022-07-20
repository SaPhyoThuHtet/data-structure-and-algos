graph = {'a':['c', 'b'], 'b':['d'], 'c':['e'], 'd': ['f'], 'e':[], 'f':[]}


def depth_first_traversal(graph, source):
    stack = [source]
    while (stack):
        current = stack.pop()
        print(current)
        
        for i in graph[current]:
            stack.append(i)
            
depth_first_traversal(graph,'a')
