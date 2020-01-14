from collections import deque

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        pre_to_course = {course:[] for course in range(numCourses)}
        in_degree = [0 for _ in range(numCourses)]
        
        for pre, course in prerequisites:
            pre_to_course[pre].append(course)
            in_degree[course] += 1 
            
            
        queue, order = deque([]), []
    
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)

        while queue:
            curr = queue.popleft()
            order.append(curr)      
            
            for next_course in pre_to_course[curr]:
                in_degree[next_course] -= 1 
                if in_degree[next_course] == 0:
                    queue.append(next_course)
                    
        return order[::-1] if len(order) == numCourses else []
