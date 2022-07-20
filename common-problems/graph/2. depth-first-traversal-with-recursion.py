graph = {'a':['c', 'b'], 'b':['d'], 'c':['e'], 'd': ['f'], 'e':[], 'f':[]}


def depth_first_traversal(graph, source):
    
    
    print(source)
    if (source):
        for neighbor in graph[source]:
            depth_first_traversal(graph, neighbor)
    
        
    
            
depth_first_traversal(graph,'a')
