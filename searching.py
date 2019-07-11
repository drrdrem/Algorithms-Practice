from collections import deque
# Lecture#6; LeetCode#102
# type root: TreeNode
# rtype: List[List[int]]
def BFS(root):
    if not root: return 

    queue, res = deque([root]), []
    while queue:
        level_vertices = []
        for _ in range(len(queue)):
            u = queue.popleft()
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
