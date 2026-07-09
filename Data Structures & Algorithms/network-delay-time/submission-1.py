class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = []
        visited = set([k])
        nodes = defaultdict(list)

        for start, end_node, w in times:
            nodes[start].append((w, end_node))
        for w, end_node in nodes[k]:
            heapq.heappush(q, (w, end_node))

        res = 0
        while q:
            w, start_node = heapq.heappop(q)
            if start_node not in visited:
                visited.add(start_node)
                res = w
                for new_w, end_node in nodes[start_node]:
                    if end_node not in visited:
                        heapq.heappush(q, (w+new_w, end_node))
        
        return res if len(visited) == n else -1