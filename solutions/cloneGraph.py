class Node:
    def __init__(self, val = 0, neighbors = None) -> None:
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: Node) -> Node:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            #if it's not already in the cloned graph made a new copy
            copy = Node(node.val)

            oldToNew[node] = copy

            #add all the neighbours

            for nei in node.neighbours:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node) if node else None

if __name__ == "__main__":
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    