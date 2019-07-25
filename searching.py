import heapq

# Lecture#6; LeetCode#102
# type root: TreeNode
# rtype: List[List[int]]
def BFS(root):
    if not root: return 

    queue, res = [root], []
    while queue:
        level_vertices = []
        for _ in range(len(queue)):
            u = queue.pop(0)
            if u.left:
                queue.append(u.left)
            if u.right:
                queue.append(u.right)
            level_vertices.append(u.val)
        res.append(level_vertices)
    return res


# Lecture#8; LeetCode#106
# type root: TreeNode
# type sum: int
# rtype: bool
def DFS(root, sum):
    if not root: return
    
    stack = [(root, root.val)]
    while stack:
        vertex, accumu_val = stack.pop()
        if not vertex.left and not vertex.right:
            if accumu_val == sum: return True
        if vertex.right:
            stack.append((vertex.right, accumu_val+vertex.right.val))
        if vertex.left:
            stack.append((vertex.left, accumu_val+vertex.left.val))
    return False


# Lecture#7; LeetCode#785
# type graph: List[List[int]]
# rtype: bool
def isBipartite(self, graph):
    visit = [False]*len(graph)
    q = [0];
    while q:
        level = []
        for _ in range(len(q)):
            node = q.pop(0)
            level.append(node)
            visit[node] = True
            for n in graph[node]:
                if not visit[n]:                    
                    q.append(n)
                
        for node in level:
            for n in graph[node]:
                if n in level: return False
    return True



# Lecture#7;
# type graph: dic{list}; c_tuple: list[tuple]
# rtype: list[tuple]
def create_graph(c_tuple):
    # Initilize graph
    graph = {}
    for i, c in enumerate(c_tuple):
        for j, c2 in enumerate(c_tuple[i+1:], start = i+1):
            if c != c2:
                if (c2[0] -c[0])**2 + (c2[1]-c[1])**2 <= (c[2] + c2[2])**2:
                    graph[i] += [j]
                    graph[j] += [i]
    return graph

def DFS(graph, tmp, v, visit, c_tuple): 
  
    visit[v] = True

    # Store the current largest vertex
    if c_tuple[v][2] > tmp[2]: tmp = c_tuple[v]


    for i in graph[v]: 
        if visit[i] == False: 

            # Update the temp res 
            tmp = DFS(graph, tmp, i, visit, c_tuple) 
            
    return tmp

def connected_Components(c_tuple): 
    graph = create_graph(c_tuple)
    
    visit = [False]*len(graph)
    res = [] 
    
    for v in graph: 
        if visit[v] == False: 
            tmp = (0, 0, 0)
            res.append(DFS(graph, tmp, v, visit, c_tuple)) 
            
    return res 



# Lecture#12;
# type graph: dic{dic}; starting_vertex: key
# rtype: shortest_dis: dic
def Dikestra(graph, start_vertex):
    shortest_dis = {vertex: float('infinity') for vertex in graph}
    shortest_dis[start_vertex] = 0

    priority_q = [(0, starting_vertex)]
    while len(priority_q) > 0:
        current_distance, current_vertex = heapq.heappop(priority_q)

        if current_distance > shortest_dis[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < shortest_dis[neighbor]:
                shortest_dis[neighbor] = distance
                heapq.heappush(priority_q, (distance, neighbor))

    return distances