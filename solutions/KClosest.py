from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for i, point in enumerate(points):
            print(point)
            
            dt = 0
            x, y = point
            dt = (x**2 + y**2)**0.5
            minHeap.append([dt, x, y])

        
        heapq.heapify(minHeap)
        print(minHeap)
        res = []
        while k > 0:
            dt, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -=1

        print(res)

        return res
        #print(first[1])

        #m = int(dist[0])






if __name__ == "__main__":
    S = Solution()
    points = [[1,1],[0,2],[2,0],[2,2]]
    k = 2

    S.kClosest(points, k)
