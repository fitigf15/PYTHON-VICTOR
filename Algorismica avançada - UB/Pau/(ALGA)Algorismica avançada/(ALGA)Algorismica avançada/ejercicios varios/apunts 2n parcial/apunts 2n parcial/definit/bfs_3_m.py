GRAPH = {1 : [2,3], 2:[4,5], 3:[6], 4:None, 5:[7,8], 6:None, 7:None, 8:None}
 
def BFS(start, target, GRAPH):
  'Use a QUEUE to search.'
  print "Source:",source,"Target:",target
  queue = [start]
  visited = []
 
  while len(queue) > 0:
    x = queue.pop(0)
 
    if x == target:
      visited.append(x)
      return visited
    elif x not in visited:
      visited = visited+[x]
      if GRAPH[x] is not None:
         'add nodes at the END of the queue'
         queue = queue + GRAPH[x]
 
  return visited
 
def DFS(start, target, GRAPH):
  'Use a STACK to search.'
  print "Source:",source,"Target:",target
  stack = [start]
  visited = []
 
  while len(stack) > 0:
    x = stack.pop(0)
 
    if x == target:
      visited.append(x)
      return visited
    elif x not in visited:
      visited = visited+[x]
      if GRAPH[x] is not None:
         'add nodes at the top of the stack'
         stack = GRAPH[x] + stack
 
  return visited
 
print "BFS Path",BFS(1,7,GRAPH)
print "DFS Path",DFS(1,7,GRAPH)
print "="*80
print "BFS Path",BFS(1,3,GRAPH)
print "DFS Path",DFS(1,3,GRAPH)

Output
?
1
2
3
4
5
6
7
8
9
10
	
$ python graph.py
BFS Path Source: 1 Target: 7
[1, 2, 3, 4, 5, 6, 7]
DFS Path Source: 1 Target: 7
[1, 2, 4, 5, 7]
================================================================================
BFS Path Source: 1 Target: 3
[1, 2, 3]
DFS Path Source: 1 Target: 3
[1, 2, 4, 5, 7, 8, 3]
