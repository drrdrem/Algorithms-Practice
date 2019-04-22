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


	
