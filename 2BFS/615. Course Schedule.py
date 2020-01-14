from collections import defaultdict, deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        edges = {course:[] for course in range(numCourses)}
        degree = [0 for i in range(numCourses)]
        
        for course, prerequisite in prerequisites:
            edges[prerequisite].append(course)
            degree[course]+=1
            
        queue, count = deque([]), 0
        
        for course in range(numCourses):
            if degree[course] == 0:
                queue.append(course)
                
        while queue:
            node = queue.popleft()
            count += 1
            
            for x in edges[node]:
                degree[x] -= 1
                if degree[x] == 0:
                    queue.append(x)
                    
        return count == numCourses
            
