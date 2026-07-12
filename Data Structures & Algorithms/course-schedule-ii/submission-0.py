class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        courses = defaultdict(list)

        for course, prereq in prerequisites:
            courses[prereq].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        order = []
        while q:
            curCourse = q.popleft()
            order.append(curCourse)
            for nei in courses[curCourse]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return order if len(order) == numCourses else []