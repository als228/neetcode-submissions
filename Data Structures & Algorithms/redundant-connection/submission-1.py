class DSU():
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.weight = [1] * (n+1)
    
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, node_a, node_b):
        par_a = self.find(node_a)
        par_b = self.find(node_b)

        if par_a == par_b:
            return False
        
        if self.weight[par_a] > self.weight[par_b]:
            self.parent[par_b] = par_a
            self.weight[par_a] += self.weight[par_b]
        else:
            self.parent[par_a] = par_b
            self.weight[par_b] += self.weight[par_a]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU(len(edges))
        for u, w in edges:
            if not dsu.union(u, w):
                return [u, w]