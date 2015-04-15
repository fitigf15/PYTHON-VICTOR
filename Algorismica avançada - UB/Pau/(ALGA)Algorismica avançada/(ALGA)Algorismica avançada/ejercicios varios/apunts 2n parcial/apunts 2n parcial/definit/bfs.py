def BFS(graph,root,target):
    q = Queue()
    checked = []
    q.enqueue(root)
    path = 0
    while not q.isEmpty():
        v = q.dequeue()
        if v == target:
           return True
        elif v not in checked:
            for edge in graph[v]:
                if v not in checked:
                    q.enqueue(edge)
            checked.append(v)
    return False
graph = {1: [2, 3],
         2: [1, 4, 5, 6],
         3: [1, 4],
         4: [2, 3, 5],
         5: [2, 4, 6],
         6: [2, 5]}
