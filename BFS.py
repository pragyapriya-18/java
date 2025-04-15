from queue import Queue 

graph={2:[5,6],7:[6,3],9:[4,5,6],3:[5,6,7]}
print("graph is")
print(graph)

def bfs(input_graph, source):
    Q=Queue() 
    visited_list = list()
    Q.put(source)
    visited_list.append(source)
    while not Q.empty():
        vertex=Q.get()
        print(vertex,end=" ")
        if vertex in input_graph:
            for u in input_graph[vertex]:
                if u not in visited_list:
                    Q.put(u)
                    visited_list.append(u)  
print("BFS is")
bfs(graph,9)



