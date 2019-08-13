class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        couses = {i : [] for i in range(numCourses)}
        indegree =  [0 for i in range(numCourses)]
        
        for i, j in prerequisites:
            couses[j].append(i)
            indegree[i] += 1
        
        queue = collections.deque()
        count = 0
        
        for key in couses:
            if indegree[key] == 0:
                queue.append(key)
        
        while queue:
            curr_course = queue.popleft()
            count += 1
            for prerequisite in couses[curr_course]:
                indegree[prerequisite]-=1
                if indegree[prerequisite] == 0:
                    queue.append(prerequisite)
                    
        return count == numCourses
         
