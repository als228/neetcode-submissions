class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for coord in points:
            dist = (coord[0]**2 + coord[1]**2) * -1
            distances.append((dist, coord))
        heapq.heapify(distances)
        while k < len(distances):
            heapq.heappop(distances)
        res = []
        for tp in distances:
            res.append(tp[1])
        
        return res