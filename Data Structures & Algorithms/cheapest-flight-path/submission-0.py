class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build adj list (O(E))
        adj_list = defaultdict(list)
        for start, end, cost in flights:
            adj_list[start].append((cost, end))
        # initialize minheap
        minheap = []
        for cost, end in adj_list[src]:
            heapq.heappush(minheap, (cost, end, 0))
        
        while minheap:
            cost, end_node, stops = heapq.heappop(minheap)
            # base cases
            if stops > k:
                continue
            if end_node == dst:
                return cost
            # keep exploring
            for add_cost, nei in adj_list[end_node]:
                heapq.heappush(minheap, (cost+add_cost, nei, stops+1))

        return -1