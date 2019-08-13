class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        if prerequisites == []: return [i for i in range(numCourses)]
        course = {x : [] for x in range(numCourses)}
        indegree = [0 for _ in range(numCourses)]
        
        for i,j in prerequisites:
            indegree[i] += 1
            course[j].append(i)
            
        print(course, indegree)
            
        order = []
        queue = collections.deque()
        
        for pos in range(len(indegree)):
            if indegree[pos] == 0:
                queue.append(pos)
                
        print(queue)
        
        while queue:
            curr_course_id = queue.popleft()
            order.append(curr_course_id)
            for pres in course[curr_course_id]:
                indegree[pres]-=1
                if indegree[pres] == 0:
                    queue.append(pres)
                    
                    
        return order if len(order) == numCourses else []
                    
                    
                
        
