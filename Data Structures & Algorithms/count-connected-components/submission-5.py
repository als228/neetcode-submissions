class Solution:
    class DSU:
        def __init__(self, n):    
            self.dsu = [i for i in range(n)]
            self.weights = [1] * n
        
        def find(self, node):
            if self.dsu[node] == node:
                return node
            self.dsu[node] = self.find(self.dsu[node])
            return self.dsu[node]

        def union(self, node_a, node_b):
            parent_a = self.find(node_a)
            parent_b = self.find(node_b)

            if parent_a == parent_b:
                return False
            
            if self.weights[parent_a] > self.weights[parent_b]:
                self.dsu[parent_b] = parent_a
                self.weights[parent_a] += self.weights[parent_b]
            else:
                self.dsu[parent_a] = parent_b
                self.weights[parent_b] += self.weights[parent_a]
            return True

    def countComponents(self, n: int, edges: List[List[int]]) -> int:      
        dsu = self.DSU(n)
        res = n
        for edge_a, edge_b in edges:
            if dsu.union(edge_a, edge_b):
                res -= 1
        
        return res