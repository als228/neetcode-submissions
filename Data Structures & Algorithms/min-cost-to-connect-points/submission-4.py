class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        node = 0
        visit = [False] * n
        dist = [float('inf')] * n
        edges = res = 0

        while edges < n-1:
            visit[node] = True
            nextNode = -1

            for i in range(n):
                if visit[i]:
                    continue
                dist[i] = min(dist[i], abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1]))
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            print("res so far is ", res, " and next node was ", points[nextNode])
            node = nextNode
            edges += 1
        
        return res