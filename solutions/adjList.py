from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        #add source or destination if it dosn't exist
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()

        #add the edge if not exist
        self.adj_list[src].add(dst)

        print(self.adj_list)
        

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        #by BFS
        visited = set()
        q = deque([src])
        while q:
            print(f'Initial queue {q}')
            curr = q.popleft()

            if curr == dst:
                return True
            visited.add(curr)

            for neighbor in self.adj_list.get(curr, []):
                #.get will get the key: value pair from the dict.
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
                    print(f'After queue {q}')

        return False


if __name__ == "__main__":
    S = Graph()

    S.addEdge(1, 2)
    S.addEdge(2, 3)
    S.hasPath(1,3)