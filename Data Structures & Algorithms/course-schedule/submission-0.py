class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # list to track # prereqs for course i
        num_prq = [0 for _ in range(numCourses)]
        # list to track courses dependent on course i
        dependent_crs = [[] for _ in range(numCourses)]

        for crs, prq in prerequisites:
            num_prq[crs] += 1
            dependent_crs[prq].append(crs)
        
        # start with courses that have NO prereqs
        q = deque()
        for i in range(numCourses):
            if num_prq[i] == 0:
                q.append(i)
        
        # track each course taken when # of its prereqs is equal to 0
        courses_taken = 0
        while q:
            crs = q.popleft()
            courses_taken += 1

            for nei in dependent_crs[crs]:
                num_prq[nei] -= 1
                if num_prq[nei] == 0:
                    q.append(nei)
        
        return courses_taken == numCourses